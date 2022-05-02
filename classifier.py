import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from xgboost import XGBClassifier 
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import BorderlineSMOTE

def classify(datapath,label,drops,title):
    data = pd.read_csv(datapath,sep=',')

    accuracies = []
    stats      = []
    allNames   = {} 

    y = data[label]
    oversample = BorderlineSMOTE()
    nope1,testingYears,nope2,testingMVPs = train_test_split(data["YEAR"],data["TEAM_NAME"],random_state=42,stratify=y,test_size=0.4)
    testingMVPs = testingMVPs.to_numpy() 
    testingYears = testingYears.to_numpy()
    for columnName,columnData in data.iteritems():
        if columnName in drops:
            continue
        elif "Unnamed" in columnName:
            continue
        elif "RANK" in columnName:
            continue
        elif columnName == label:
            continue

        print(columnName)
        X = data[columnName]
        X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,stratify=y,test_size=0.4)

        X_train,y_train = oversample.fit_resample(X_train.to_frame(),y_train) 

        xg = XGBClassifier()
        xg.fit(X_train.squeeze(),y_train)
        predictions = xg.predict(X_test)

        idx2   = np.where(y_test == 1)[0]
        pred   = predictions[idx2]
        testIdx = np.where(pred == 1)[0]
        allNames[columnName] = testingMVPs[idx2][testIdx]
        actual = y_test.loc[y_test == 1]
        pdIdx  = y_test.loc[y_test == 1].index.values
        relIdx = idx2 

        if len(set(pred)) == 1:
            continue

#        out = classification_report(y_test,predictions,output_dict=True)
        out = classification_report(actual,pred,output_dict=True)
        accuracies.append(out['accuracy'])
        stats.append(columnName)

    #Sort accuracies for plotting
    idx = np.argsort(accuracies)
    sortedLbl = []
    #Plot accuracies
    for ii in range(0,len(idx)):
        plt.bar(ii,accuracies[idx[ii]])
        sortedLbl.append(stats[idx[ii]])
    plt.xticks(range(len(sortedLbl)),sortedLbl,size='small',rotation='vertical')
    plt.ylabel("Accuracy")
    plt.ylim(min(accuracies)-0.1,1)
    plt.title(title)
    plt.show()

    yaxis = []
    nameOut = []
    for ii in range(0,len(relIdx)):
        jj = relIdx[ii]
        test = str(testingYears[jj]) + " | " + (testingMVPs[jj])
        print(test)
        nameOut.append(testingMVPs[jj])
        yaxis.append(test)

    plt.yticks(range(len(yaxis)),yaxis,size='small')
    plt.ylabel("Year | " + label)

    xaxis = []
    count = 0
    for ii in range(len(sortedLbl)-5,len(sortedLbl)):
        xaxis.append(sortedLbl[ii])
        names = allNames[sortedLbl[ii]]
        for jj in range(0,len(yaxis)):
            if nameOut[jj] in names:
                plt.plot(count,jj,'gP')
            else:
                plt.plot(count,jj,'rx')
        count += 1

    plt.title('Correct Predictions - Top 5 Stats for ' + label)
    plt.xticks(range(len(xaxis)),xaxis,size='small')
    plt.show()



if __name__ == "__main__":
    drops  = ["MVP","FINALS_MVP","PLAYER_NAME","NICKNAME","TEAM_ABBREVIATION","CFPARAMS","PLAYER_ID","TEAM_ID","AGE","YEAR","CFID"]
    #pPlayoff = "/home/gene/Documents/DataMiningII/Project/labelledCSV/player_playoff.csv"
    pRegular = "/home/gene/Documents/DataMiningII/Project/labelledCSV/player_regular.csv"
    #labels = ["WIN","LOSE"]
    #tPlayoff = "/home/gene/Documents/DataMiningII/Project/labelledCSV/team_playoff.csv"
    tRegular = "/home/gene/Documents/DataMiningII/Project/labelledCSV/team_regular.csv"
    #classify(pRegular,"ALL_STAR",drops,"Predictions of All Star players using different stats") 
    #drops  = ["ALL_STAR","FINALS_MVP","PLAYER_NAME","NICKNAME","TEAM_ABBREVIATION","CFPARAMS","PLAYER_ID","TEAM_ID","AGE","YEAR"]
    #classify(pRegular,"MVP",drops,"Preditcting MVPs using different stats") 
    #drops  = ["MVP","ALL_STAR","PLAYER_NAME","NICKNAME","TEAM_ABBREVIATION","CFPARAMS","PLAYER_ID","TEAM_ID","AGE","YEAR"]
    #classify(pRegular,"FINALS_MVP",drops,"Predicting Finals MVPs using different stats") 
    drops  = ["LOSE","TEAM_NAME","NICKNAME","TEAM_ABBREVIATION","CFPARAMS","PLAYER_ID","TEAM_ID","AGE","YEAR","CFID"]
    classify(tRegular,"WIN",drops,"Preditcting NBA Champions using different stats") 
    drops  = ["WIN","TEAM_NAME","NICKNAME","TEAM_ABBREVIATION","CFPARAMS","PLAYER_ID","TEAM_ID","AGE","YEAR","CFID"]
    classify(tRegular,"LOSE",drops,"Predicting NBA Finals Losers using different stats") 
