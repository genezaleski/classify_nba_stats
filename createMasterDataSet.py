import os
import glob
import re
import numpy as np
import pandas as pd

def combineCSV(datapath):
    extension = 'csv'
    os.chdir(datapath)
    all_filenames = [ii for ii in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

def addYearColumn(datapath):
    extension = 'csv'
    os.chdir(datapath)
    all_filenames = [ii for ii in glob.glob('*.{}'.format(extension))]
    for csv in all_filenames:
        yearString = csv.split("_")[0]
        yearString = yearString[0] + yearString[1] + yearString[5] + yearString[6]
        if yearString == "1900":
            yearString = "2000"
        if yearString.isdigit():
            df = pd.read_csv(csv)
            df["YEAR"] = yearString
            df.to_csv(csv,index=False)

def combineCSVColumns(pathA,pathB,outpath):
    extension = 'csv'
    os.chdir(pathA)
    aFiles = [ii for ii in glob.glob('*.{}'.format(extension))]
    os.chdir(pathB)
    bFiles = [ii for ii in glob.glob('*.{}'.format(extension))]

    for csv in aFiles:
        f1 = pd.read_csv(pathA + csv)
        f2 = pd.read_csv(pathB + csv)
        # Change Player ID to Team ID and vice versa
        outfile = pd.merge(f1,f2,on="TEAM_ID",how="inner",suffixes=("","_drop"))
        outfile.drop([col for col in outfile.columns if 'drop' in col], axis=1, inplace=True)
        outfile.to_csv(outpath + csv)

def assignLabels():

    #Player Labels
    aspath = "/home/gene/Documents/DataMiningII/Project/labels/allStars.txt"
    finalMVPs = "/home/gene/Documents/DataMiningII/Project/labels/finalsMvps.txt"
    MVPpath   = "/home/gene/Documents/DataMiningII/Project/labels/mvps.txt"

    #Team labels
    champpath = "/home/gene/Documents/DataMiningII/Project/labels/finalsChamps.txt"
    finalLpath= "/home/gene/Documents/DataMiningII/Project/labels/finalsLoss.txt"

    #CSV to assign labels to
    combinedPlayerPlayoff = "/home/gene/Documents/DataMiningII/Project/cleanCSV/playoffsPlayer/player_playoffs.csv"
    combinedTeamPlayoff = "/home/gene/Documents/DataMiningII/Project/cleanCSV/playoffsTeam/team_playoffs.csv"
    combinedPlayerReg = "/home/gene/Documents/DataMiningII/Project/cleanCSV/regularSeasonPlayer/player_regular.csv"
    combinedTeamReg = "/home/gene/Documents/DataMiningII/Project/cleanCSV/regularSeasonTeam/team_regular.csv"

#    playerRegularSeason = pd.read_csv(combinedPlayerReg)
#    playerRegularSeason["ALL_STAR"] = 0
#    playerRegularSeason["MVP"] = 0
#    playerRegularSeason["FINALS_MVP"] = 0

#    playerPlayoffs = pd.read_csv(combinedPlayerPlayoff)
#    playerPlayoffs["ALL_STAR"] = 0
#    playerPlayoffs["MVP"] = 0
#    playerPlayoffs["FINALS_MVP"] = 0

    teamRegularSeason = pd.read_csv(combinedTeamReg)
    teamRegularSeason["WIN"] = 0 
    teamRegularSeason["LOSE"] = 0 

    teamPlayoffs      = pd.read_csv(combinedTeamPlayoff)
    teamPlayoffs["WIN"] = 0
    teamPlayoffs["LOSE"] = 0

    #create list of accolades by year, then load csvs, then create accolade columns in csv
#    with open(aspath,'r') as allStarsFile:
#        for line in allStarsFile:
#            allStars = line.split(",")
#            year = int(allStars[0].strip())
#            allStars = allStars[1:]
#            for player in allStars:
#                nidx = playerRegularSeason[playerRegularSeason['PLAYER_NAME']==player.strip()].index.values
#                yidx = playerRegularSeason[playerRegularSeason['YEAR']==year].index.values 
#                nidx1 = playerPlayoffs[playerPlayoffs['PLAYER_NAME']==player.strip()].index.values
#                yidx1 = playerPlayoffs[playerPlayoffs['YEAR']==year].index.values 
#                regIdx = np.intersect1d(nidx,yidx)
#                playoffIdx = np.intersect1d(nidx1,yidx1)
#                if regIdx.size > 0:
#                    playerRegularSeason['ALL_STAR'][regIdx[0]] = 1
#                if playoffIdx.size > 0:
#                    playerPlayoffs['ALL_STAR'][playoffIdx[0]] = 1
#
#    with open(MVPpath,'r') as allStarsFile:
#        for line in allStarsFile:
#            allStars = line.split(",")
#            year = int(allStars[0].strip())
#            allStars = allStars[1:]
#            for player in allStars:
#                nidx = playerRegularSeason[playerRegularSeason['PLAYER_NAME']==player.strip()].index.values
#                yidx = playerRegularSeason[playerRegularSeason['YEAR']==year].index.values 
#                nidx1 = playerPlayoffs[playerPlayoffs['PLAYER_NAME']==player.strip()].index.values
#                yidx1 = playerPlayoffs[playerPlayoffs['YEAR']==year].index.values 
#                regIdx = np.intersect1d(nidx,yidx)
#                playoffIdx = np.intersect1d(nidx1,yidx1)
#                if regIdx.size > 0:
#                    playerRegularSeason['MVP'][regIdx[0]] = 1
#                if playoffIdx.size > 0:
#                    playerPlayoffs['MVP'][playoffIdx[0]] = 1
#
#    with open(finalMVPs,'r') as allStarsFile:
#        for line in allStarsFile:
#            allStars = line.split(",")
#            year = int(allStars[0].strip())
#            allStars = allStars[1:]
#            for player in allStars:
#                nidx = playerRegularSeason[playerRegularSeason['PLAYER_NAME']==player.strip()].index.values
#                yidx = playerRegularSeason[playerRegularSeason['YEAR']==year].index.values 
#                nidx1 = playerPlayoffs[playerPlayoffs['PLAYER_NAME']==player.strip()].index.values
#                yidx1 = playerPlayoffs[playerPlayoffs['YEAR']==year].index.values 
#                regIdx = np.intersect1d(nidx,yidx)
#                playoffIdx = np.intersect1d(nidx1,yidx1)
#                if regIdx.size > 0:
#                    playerRegularSeason['FINALS_MVP'][regIdx[0]] = 1
#                if playoffIdx.size > 0:
#                    playerPlayoffs['FINALS_MVP'][playoffIdx[0]] = 1

#    playerRegularSeason.to_csv("player_regular.csv", index=False, encoding='utf-8-sig')
#    playerPlayoffs.to_csv("player_playoff.csv", index=False, encoding='utf-8-sig')

    with open(champpath,'r') as allStarsFile:
        for line in allStarsFile:
            allStars = line.split(",")
            year = int(allStars[0].strip())
            allStars = allStars[1:]
            for player in allStars:
                nidx = teamRegularSeason[teamRegularSeason['TEAM_NAME']==player.strip()].index.values
                yidx = teamRegularSeason[teamRegularSeason['YEAR']==year].index.values 
                nidx1 = teamPlayoffs[teamPlayoffs['TEAM_NAME']==player.strip()].index.values
                yidx1 = teamPlayoffs[teamPlayoffs['YEAR']==year].index.values 
                regIdx = np.intersect1d(nidx,yidx)
                playoffIdx = np.intersect1d(nidx1,yidx1)
                if regIdx.size > 0:
                    teamRegularSeason['WIN'][regIdx[0]] = 1
                if playoffIdx.size > 0:
                    teamPlayoffs['WIN'][playoffIdx[0]] = 1

    with open(finalLpath,'r') as allStarsFile:
        for line in allStarsFile:
            allStars = line.split(",")
            year = int(allStars[0].strip())
            allStars = allStars[1:]
            for player in allStars:
                nidx = teamRegularSeason[teamRegularSeason['TEAM_NAME']==player.strip()].index.values
                yidx = teamRegularSeason[teamRegularSeason['YEAR']==year].index.values 
                nidx1 = teamPlayoffs[teamPlayoffs['TEAM_NAME']==player.strip()].index.values
                yidx1 = teamPlayoffs[teamPlayoffs['YEAR']==year].index.values 
                regIdx = np.intersect1d(nidx,yidx)
                playoffIdx = np.intersect1d(nidx1,yidx1)
                if regIdx.size > 0:
                    teamRegularSeason['LOSE'][regIdx[0]] = 1
                if playoffIdx.size > 0:
                    teamPlayoffs['LOSE'][playoffIdx[0]] = 1

    teamRegularSeason.to_csv("team_regular.csv", index=False, encoding='utf-8-sig')
    teamPlayoffs.to_csv("team_playoff.csv", index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    playerAdvPath = '/home/gene/Documents/DataMiningII/Project/getNBAcom/baseAdvancedCSV/'
    playerNonPath = '/home/gene/Documents/DataMiningII/Project/getNBAcom/nonAdvancedCSV/'
    teamAdvPath = '/home/gene/Documents/DataMiningII/Project/getNBAcom/teamAdvancedCSV/'
    teamNonPath = '/home/gene/Documents/DataMiningII/Project/getNBAcom/teamNonAdvancedCSV/'

    #
    # Add column to each csv indicating which year the data is from.
    # This will differentiate rows once the data is combined.
    #
    #addYearColumn(playerAdvPath)
    #addYearColumn(playerNonPath)
    #addYearColumn(teamAdvPath)
    #addYearColumn(teamNonPath)

    #
    # Combine Advanced and non Advanced data entries for each player.
    #
    #combineCSVColumns(playerAdvPath + "regular/",playerNonPath + "regular/","/home/gene/Documents/DataMiningII/Project/cleanCSV/regularSeasonPlayer/")
    #combineCSVColumns(playerAdvPath + "playoff/",playerNonPath + "playoff/","/home/gene/Documents/DataMiningII/Project/cleanCSV/playoffsPlayer/")
    #combineCSVColumns(teamAdvPath + "regular/",teamNonPath + "regular/","/home/gene/Documents/DataMiningII/Project/cleanCSV/regularSeasonTeam/")
    #combineCSVColumns(teamAdvPath + "playoff/",teamNonPath + "playoff/","/home/gene/Documents/DataMiningII/Project/cleanCSV/playoffsTeam/")
    
    #
    #combine the csvs so they can be labelled in one csv 
    #
    #combineCSV("/home/gene/Documents/DataMiningII/Project/cleanCSV/regularSeasonPlayer/")
    #combineCSV("/home/gene/Documents/DataMiningII/Project/cleanCSV/playoffsPlayer/")
    #combineCSV("/home/gene/Documents/DataMiningII/Project/cleanCSV/regularSeasonTeam/")
    #combineCSV("/home/gene/Documents/DataMiningII/Project/cleanCSV/playoffsTeam/")

    assignLabels()
