
"""
Plot the frequency histogram on ’GapBetweenPACs’ and ’ActionsInPAC’ attributes, respectively. 
"""

import csv
import matplotlib.pyplot as plt

AttributeList = ["GameID","LeagueIndex","Age","HoursPerWeek","TotalHours","APM","SelectByHotkeys","AssignToHotkeys","UniqueHotkeys","MinimapAttacks","MinimapRightClicks","NumberOfPACs","GapBetweenPACs","ActionLatency","ActionsInPAC","TotalMapExplored","WorkersMade","UniqueUnitsMade","ComplexUnitsMade","ComplexAbilitiesUsed"]

def plotHistogram(xlistData, numbins, filename, xlabel, ylabel):

    diffMaxMin = int(max(xlistData) - min(xlistData))
    binWidth = int(diffMaxMin/numbins)

    bins = range(0, int(max(xlistData) + 2 * binWidth), binWidth)

    plt.hist(xlistData, normed=False, bins=bins, orientation="vertical", ec = "black", range=(0,int(max(xlistData) + binWidth)))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    #plt._show()
    plt.clf()


    pass



if __name__ == "__main__":

    inputCsvFile = "./SkillCraft1_Dataset.csv"
    gapPacs = []
    actionInPacs = []
    with open(inputCsvFile, "r") as fileObj:
        reader = csv.reader(fileObj, delimiter=',', quotechar='"')
        i = 0
        for row in reader:
            if i==0:    #Skip first row
                i = 1
                pass
            else:
                #print(row)
                gapPacs.append(float(row[AttributeList.index("GapBetweenPACs")]))
                actionInPacs.append(float(row[AttributeList.index("ActionsInPAC")]))
    print(gapPacs)
    print(actionInPacs)
    print(str(min(gapPacs)))
    print(str(max(gapPacs)))
    print(str(min(actionInPacs)))
    print(str(max(actionInPacs)))

    plotHistogram(gapPacs, 30, "GapBetweenPACs.png", "GapBetweenPACs", "Frequencies")
    plotHistogram(actionInPacs, 10, "ActionsPACs.png", "ActionsPACs", "Frequencies")

