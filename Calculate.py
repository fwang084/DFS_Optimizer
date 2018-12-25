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




