import os 
import pandas as pd
import requests
from os.path import exists

# Header tab, under “Request Headers” subsection
header = {
"accept": "application/json, text/plain, */*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"origin": "https://www.nba.com",
"referer": "https://www.nba.com/",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
"x-nba-stats-origin": "stats",
"x-nba-stats-token": "true"}

url = "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="

playoff_url = "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2020-21&SeasonSegment=&SeasonType=Playoffs&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="

count = 0
for ii in range(1996,2022):
    if ii >= 2000:
        upperYear = 1+ii-2000
        if upperYear < 10:
            upperYear = "0" + str(upperYear)
    else:
        upperYear = 1+ii-1900
        if upperYear == 100:
            upperYear = "00"
        
    yearString = str(ii) + "-" + str(upperYear)
    currURL = url.replace("2021-22",yearString)
    print("Collecting " + yearString + " stats...")
    count += 1
    #Using Request library to get the data
    #
    # First get regular season
    if not exists("/home/gene/Documents/DataMiningII/Project/getNBAcom/teamNonAdvancedCSV/"+ yearString +"_regular.csv"):
        #vpn = vpnList[count]
        #os.system('expressvpn connect ' + vpn)
        response = requests.get(currURL, headers=header)
        response_json = response.json()
        frame = pd.DataFrame(response_json['resultSets'][0]['rowSet'])
        frame.columns = response_json['resultSets'][0]['headers']
        frame.to_csv("/home/gene/Documents/DataMiningII/Project/getNBAcom/teamNonAdvancedCSV/"+ yearString +"_regular.csv",sep=",",header=frame.columns)

    # Next get playoffs
    if not exists("/home/gene/Documents/DataMiningII/Project/getNBAcom/teamNonAdvancedCSV/"+ yearString +"_playoff.csv"):
        currURL = playoff_url.replace("2020-21",yearString)
        response = requests.get(currURL, headers=header)
        response_json = response.json()
        frame = pd.DataFrame(response_json['resultSets'][0]['rowSet'])
        frame.columns = response_json['resultSets'][0]['headers']
        frame.to_csv("/home/gene/Documents/DataMiningII/Project/getNBAcom/teamNonAdvancedCSV/"+ yearString +"_playoff.csv",sep=",",header=frame.columns)

