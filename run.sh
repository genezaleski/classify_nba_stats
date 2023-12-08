#!/bin/sh

#First scrape NBA.com
python getNBAcom/scrapeNBAcomAdvanced.py
python getNBAcom/scrapeNBAcomAdvancedTeam.py
python getNBAcom/scrapeNBAcomRegular.py
python getNBAcom/scrapeNBAcomTeamRegular.py

#Next, create dataset with labels for the classifier to read
python createMasterDataset.py

#Finally, run classifier and create plots
python classifier.py
