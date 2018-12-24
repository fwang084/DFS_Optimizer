from Daily_Scrape import *
import sqlite3

conn = sqlite3.Connection("n.db")
conn.execute("DROP TABLE IF EXISTS daily_players;")
conn.execute("CREATE TABLE daily_players(name, proj_score, price);")

