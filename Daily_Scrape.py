from Initialize import *
from Player import *
from Team import *
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import xlrd

def simple_get(url):
   """ Attempts to get the content at `url` by making an HTTP GET request.
   If the content-type of response is some kind of HTML/XML, return the
   text content, otherwise return None."""
   try:
       with closing(get(url, stream=True)) as resp:
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
   """It is always a good idea to log errors.
   This function just prints them, but you can
   make it do anything."""
   print(e)

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
'''DKSalaries.xls is a local file containing DraftKings salaries for the day'''
salaries = workbook.sheet_by_index(0)

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
        if len(row)>1:
            for t in team_list:
                if row[1] in t.get_names():
                    t.set_possessions(float(row[8]))
    return [item/30 for item in [points_total, rebounds_total, assists_total, steals_total,
                                 blocks_total, threes_total, turnovers_total]]

def assign_team_factors(league_averages):
    """
    Assigns a list of factors to each team: player projections will be calculated by multiplying this
    list of factors by their average stats
    :param league_averages: average team statistics
    :return: None
    """

def find_player_salaries():
    """
    Loops through rows in XLS file until the row doesn't exist, which signifies that all players
    have been added to the list
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

def create_players(salaries):
    """
    Loops through every NBA player, and for those who are playing on the given slate,
    creates a Player object to represent the player, and adds that to player_list
    :return: None
    """
    for tr in player_info_list.select('tr.full_table'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        team_name=row[3]
        for t in team_list:
            if team_name in t.get_names():
                team=t
        price = 0
        for player_dk in salaries:
            if row[0] == player_dk[3]:
                price = row[5]
        if price != 0:
            opponent = figure_out_opponent(row[6][:7], row[7])
            stats = [float(row[28]), float(row[22]), float(row[23]), float(row[24]),
               float(row[25]), float(row[10]), float(row[26])]
            player_list.append(Player(row[0], team, row[1], float(row[6]), opponent, stats, price))

def figure_out_opponent(two_teams, own_team):
    """
    Takes a string in the form (team abbreviation 1)@(team abbreviation 2), and a string
    that is one of the teams, and figures out the other team
    :param two_teams: string representing the matchup (ex. 'CLE@GSW')
    :param own_team: string representing one team (ex. 'GSW')
    :return: the Team instance representing the other team
    """
    if two_teams[:3] == own_team:
        team_to_return = two_teams[4:]
    else:
        team_to_return = two_teams[:3]
    for t in team_list:
        if team_to_return in t.get_names():
            return t

"""
player_salaries = find_player_salaries()
create_players(player_salaries) 
averages = assign_team_stats() 
possessions_total=0
for t in team_list:
    possessions_total += t.get_possessions()
averages.append(float(possessions_total/30))
assign_team_factors(averages)"""
















