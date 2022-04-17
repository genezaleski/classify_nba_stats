import os

datapath = "/home/gene/Documents/DataMiningII/Project/images/abbrevs.txt"
url = "http://stats.nba.com/media/img/teams/logos/season/2016-17/"
url2 = "_logo.svg"

with open(datapath,'r') as abbrevs:
    for team in abbrevs:
        os.system("wget " + url + team.strip() + url2)
