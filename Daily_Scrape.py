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
workbook = xlrd.open_workbook('DKSalaries.xls')
'''DKSalaries.xls is a local file containing DraftKings salaries for the day'''
salaries = workbook.sheet_by_index(0)
def create_players():
    """
    Loops through every NBA player, creates a Player object to represent the player, and adds to player_list
    :return: None
    """
    for tr in player_info_list.select('tr.full_table'):
        td = tr.find_all('td')
        row = [i.get_text() for i in td]
        team_name=row[3]
        for t in team_list:
            if t.get_name()==team_name:
                team=t
        stats=[row[28], row[22], row[23], row[24], row[25], row[10], row[26]]
        player_list.append(Player(row[0], team, row[1], row[6], stats))
create_players()







