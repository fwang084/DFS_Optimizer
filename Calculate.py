from Daily_Scrape import *
import sqlite3

conn = sqlite3.Connection("n.db")
conn.execute("DROP TABLE IF EXISTS daily_players;")
conn.execute("CREATE TABLE daily_players(name, proj_score, price);")
for p in player_list:
    conn.execute("INSERT INTO daily_players VALUES (?, ?, ?)", (p.get_name(), p.get_proj_score(), p.get_price()))

def find_best_value():
    """
    Finds the best projected score per price players
    :return: A list of 40 tuples, with each tuple consisting of player name and 1000 * proj_score/price
    """
    print(conn.execute("SELECT name, 1000 * proj_score/price FROM daily_players ORDER BY -proj_score/price LIMIT 40;").fetchall())

def optimal_lineup(remaining_players, lineup):
    """
    Tree recursive method to find the optimal lineup given a player budget of $50000
    :param remaining_players: players that can still be added to the lineup
    :param lineup: players that are already added to the lineup
    :return: list of players in the order [PG, SG, G, SF, PF, F, C, UTIL]
    """
    if remaining_players == []:
        for i in lineup:
            if i is None:
                return 0
        return lineup
    else:
        player = remaining_players[0]
        string_position = player.get_positions()
        positions = []
        while string_position != '':
            current_position = string_position[0]
            position = string_position[1:]
            if string_position == '':
                positions.append(current_position)
            elif string_position[0] == "/":
                positions.append(current_position)
                string_position = string_position[1:]
            else:
                current_position = current_position + string_position[0]
                positions.append(current_position)
                string_position = string_position[1:]

def position_converter(string_position):
    positions = []
    while string_position != '':
        if string_position[0] == "/":
            string_position = string_position[1:]
        current_position = string_position[0]
        string_position = string_position[1:]
        if string_position == '':
            positions.append(current_position)
        elif string_position[0] == "/":
            positions.append(current_position)
            string_position = string_position[1:]
        else:
            current_position = current_position + string_position[0]
            positions.append(current_position)
            string_position = string_position[1:]
    return positions

def lineup_score(players_chosen):
    """
    Sums the projected scores of the players in a list
    :param players_chosen: either 0 or a list representing a DraftKings lineup
    :return: Projected score of the lineup
    """
    if players_chosen == 0:
        return 0
    else:
        proj_score = 0
        for p in players_chosen:
            proj_score += p.get_proj_score()
        return proj_score








