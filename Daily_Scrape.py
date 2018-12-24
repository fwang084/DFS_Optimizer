from Initialize import *
from Player import *
from Team import *
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import xlrd

def simple_get(url):
    """
    Attempts to get the content at 'url' by making an HTTP GET request.
    If the content-type of response is HTML/XML, return the text content, otherwise return None."""
    try:
        with closing(get(url, stream = True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
def is_good_response(resp):
    """ Returns True if the response seems to be HTML, False otherwise."""
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)
def log_error(e):
    print(e)

def find_player_salaries(salaries):
    """
    Loops through rows in XLS file until the row doesn't exist, which signifies that all players
    have been added to the list
    :param salaries: XLS file containing DraftKings salary information
    :return: list of lists, with each nested list containing DraftKings information for a player
    """
    row_num = 1
    players=[]
    while True:
        try:
            players.append([a.value for a in salaries.row(row_num)])
            row_num += 1
        except IndexError:
            return players

def assign_team_stats():
    """
    Loops through each row in tables from the team data websites, finds which team the row
    is in reference to, and assigns relevant statistics to that team
    :return: Average of each of these statistics
    """
    points_total = 0
    threes_total = 0
    for tr in team_defense_list.select('tr.oddrow'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        for t in team_list:
            if row[1] in t.get_names():
                t.set_points_allowed(float(row[2]))
                t.set_threes_allowed(float(row[6]))
                points_total += float(row[2])
                threes_total += float(row[6])
    for tr in team_defense_list.select('tr.evenrow'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        for t in team_list:
            if row[1] in t.get_names():
                t.set_points_allowed(float(row[2]))
                t.set_threes_allowed(float(row[6]))
                points_total += float(row[2])
                threes_total += float(row[6])

    rebounds_total = 0
    for tr in team_rebounds_list.select('tr.oddrow'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        for t in team_list:
            if row[1] in t.get_names():
                t.set_rebounds_allowed(float(row[10]))
                rebounds_total += float(row[10])
    for tr in team_rebounds_list.select('tr.evenrow'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        for t in team_list:
            if row[1] in t.get_names():
                t.set_rebounds_allowed(float(row[10]))
                rebounds_total += float(row[10])

    assists_total = 0
    steals_total = 0
    blocks_total = 0
    turnovers_total = 0
    for tr in team_misc_list.select('tr.oddrow'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        for t in team_list:
            if row[1] in t.get_names():
                t.set_assists_allowed(float(row[3]))
                t.set_steals_allowed(float(row[5]))
                t.set_blocks_allowed(float(row[7]))
                t.set_opp_turnovers(float(row[9]))
                assists_total += float(row[3])
                steals_total += float(row[5])
                blocks_total += float(row[7])
                turnovers_total += float(row[9])
    for tr in team_misc_list.select('tr.evenrow'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        for t in team_list:
            if row[1] in t.get_names():
                t.set_assists_allowed(float(row[3]))
                t.set_steals_allowed(float(row[5]))
                t.set_blocks_allowed(float(row[7]))
                t.set_opp_turnovers(float(row[9]))
                assists_total += float(row[3])
                steals_total += float(row[5])
                blocks_total += float(row[7])
                turnovers_total += float(row[9])

    for tr in team_possessions_list.select('tr.odd'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        if len(row) > 1:
            for t in team_list:
                if row[1] in t.get_names():
                    t.set_possessions(float(row[8]))
    for tr in team_possessions_list.select('tr.even'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        if len(row) > 1:
            for t in team_list:
                if row[1] in t.get_names():
                    t.set_possessions(float(row[8]))
    return [item/30 for item in [points_total, rebounds_total, assists_total, steals_total,
                                 blocks_total, threes_total, turnovers_total]]

def assign_team_factors(league_averages):
    """
    Assigns a list of factors to each team: player projections will be calculated by multiplying this
    list of factors by their average stats. Method of computation is based on experience and is fluid
    :param league_averages: average team statistics
    :return: None
    """
    assert (len(league_averages) == 8), "league_average should contain 8 averages"
    points_average = league_averages[0]
    rebounds_average = league_averages[1]
    assists_average = league_averages[2]
    steals_average = league_averages[3]
    blocks_average = league_averages[4]
    threes_average = league_averages[5]
    turnovers_average = league_averages[6]
    possessions_average =league_averages[7]
    for t in team_list:
        points_sum = (t.get_possessions()/possessions_average) + 3*(t.get_points_allowed()/points_average) + 1
        points_factor = points_sum / 5
        rebounds_sum = 2*(t.get_rebounds_allowed()/rebounds_average) + 1
        rebounds_factor = rebounds_sum / 3
        assists_sum = (t.get_possessions()/possessions_average) + 3*(t.get_assists_allowed()/assists_average) + 1
        assists_factor = assists_sum / 5
        steals_sum = (t.get_steals_allowed()/steals_average) + 1
        steals_factor = steals_sum / 2
        blocks_sum = (t.get_blocks_allowed()/blocks_average) + 1
        blocks_factor = blocks_sum / 2
        threes_sum = 2*(t.get_threes_allowed()/threes_average) + 1
        threes_factor = threes_sum / 3
        turnovers_sum = (t.get_opp_turnovers()/turnovers_average) + 1
        turnovers_factor = turnovers_sum / 2
        t.set_factors([points_factor, rebounds_factor, assists_factor, steals_factor,
                       blocks_factor, threes_factor, turnovers_factor])

def create_players(salaries):
    """
    Loops through every NBA player, and for those who are playing on the given slate,
    creates a Player object to represent the player, and adds that to player_list
    :param salaries: list of lists, with each nested list containing DraftKings player info
    :return: None
    """
    for tr in player_info_list.select('tr.full_table'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        team_name = row[3]
        for t in team_list:
            if team_name in t.get_names():
                team = t
        price = 0
        for player_dk in salaries:
            if row[0] == player_dk[2]:
                price = row[5]
                matchup = player_dk[6][:7]
                positions = player_dk[0]
        if price != 0:
            opponent = figure_out_opponent(matchup, team.get_names()[0])
            factors = opponent.get_factors()
            avg_stats = [float(row[28]), float(row[22]), float(row[23]), float(row[24]),
                         float(row[25]), float(row[10]), float(row[26])]
            proj_stats = multiply_lists(factors, avg_stats)
            proj_score = generate_projection(proj_stats)
            player_list.append(Player(row[0], team, positions, float(row[6]), opponent,
                                      avg_stats, proj_stats, price, proj_score))

def figure_out_opponent(two_teams, own_team):
    """
    Takes a string in the form (team abbreviation 1)@(team abbreviation 2), and a string
    that is one of the teams, and figures out the other team
    :param two_teams: string representing the matchup (ex. 'CLE@GSW')
    :param own_team: string representing one team (ex. 'GSW')
    :return: the Team instance representing the other team
    """
    assert (len(two_teams) == 7), "two_teams should have the form 'CLE@GSW'"
    assert (two_teams[3] == '@'), "two_teams should have the form 'CLE@GSW'"
    assert (len(own_team) == 3), "one_team should have the form GSW"
    if two_teams[:3] == own_team:
        team_to_return = two_teams[4:]
    else:
        team_to_return = two_teams[:3]
    for t in team_list:
        if team_to_return in t.get_names():
            return t

def multiply_lists(lst1, lst2):
    """
    Takes two equal-length lists which contain float values
    :return: list containing values in corresponding positions multiplied
    """
    assert (len(lst1) == len(lst2)), "the two lists must have the same length"
    new_lst=[]
    for i in range(len(lst1)):
        new_lst.append(lst1[i]*lst2[i])
    return new_lst
def generate_projection(stats):
    """
    Sets a player's projected points by taking in a list of projected stats and calculating their points
    using DraftKings rules: 1pt per point, 1.25:assist, 1.5:rebound, 2:steal, 2:block, 0.5:3-pointer, -0.5:turnover
    Additional bonus of 1.5 for a double-double and 3 for a triple-double
    :param stats: list of: points, rebounds, assists, steals, blocks, 3s, turnovers
    :return: None
    """
    doubles = 0
    doubles_bonus = 0
    for x in stats[:5]:
        if x >= 10:
            doubles += 1
    if doubles >= 3:
        doubles_bonus = 4.5
    elif doubles == 2:
        doubles_bonus = 1.5
    return stats[0] + 1.25*stats[1] + 1.5*stats[2] + 2*stats[3] + 2*stats[4] + 0.5*stats[5] - 0.5*stats[6] + doubles_bonus

player_info = simple_get("https://www.basketball-reference.com/leagues/NBA_2019_per_game.html")
player_info_list = BeautifulSoup(player_info, 'html.parser')

team_defense = simple_get("http://www.espn.com/nba/statistics/team/_/stat/defense-per-game")
team_defense_list = BeautifulSoup(team_defense, 'html.parser')

team_rebounds = simple_get("http://www.espn.com/nba/statistics/team/_/stat/rebounds-per-game")
team_rebounds_list = BeautifulSoup(team_rebounds, 'html.parser')

team_miscellaneous = simple_get("http://www.espn.com/nba/statistics/team/_/stat/miscellaneous-per-game")
team_misc_list = BeautifulSoup(team_miscellaneous, 'html.parser')

team_possessions = simple_get("https://www.nbastuffer.com/2018-2019-nba-team-stats/")
team_possessions_list = BeautifulSoup(team_possessions, 'html.parser')

workbook = xlrd.open_workbook('DKSalaries.xls')
"""DKSalaries.xls is a local file containing DraftKings salaries for the day"""
salaries_list = workbook.sheet_by_index(0)

player_salaries = find_player_salaries(salaries_list)
averages = assign_team_stats()
possessions_total=0
for t in team_list:
    possessions_total += t.get_possessions()
averages.append(float(possessions_total/30))
assign_team_factors(averages)
create_players(player_salaries)




















