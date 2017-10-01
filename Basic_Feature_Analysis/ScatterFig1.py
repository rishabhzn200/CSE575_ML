
"""
Plot the scatter figure for the following pairs of features: 
(1) SelectByHotkeys vs. AssignToHotkeys, and 
(2) NumberOfPACs vs. GapBetweenPACs, respectively.
"""

import csv
import matplotlib.pyplot as plt

AttributeList = ["GameID","LeagueIndex","Age","HoursPerWeek","TotalHours","APM","SelectByHotkeys","AssignToHotkeys","UniqueHotkeys","MinimapAttacks","MinimapRightClicks","NumberOfPACs","GapBetweenPACs","ActionLatency","ActionsInPAC","TotalMapExplored","WorkersMade","UniqueUnitsMade","ComplexUnitsMade","ComplexAbilitiesUsed"]

def plotScatterFigure(X, Y, filename, xlabel, ylabel):

    plt.scatter(X, Y, c="red", alpha=0.5, edgecolors="black")
    plt.title(xlabel + "_VS_" + ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt._show()

    pass



if __name__ == "__main__":

    inputCsvFile = "./SkillCraft1_Dataset.csv"
    SelectByHotkeys = []
    AssignToHotkeys = []

    NumberOfPACs = []
    GapBetweenPACs = []

    with open(inputCsvFile, "r") as fileObj:
        reader = csv.reader(fileObj, delimiter=',', quotechar='"')
        i = 0
        for row in reader:
            if i==0:
                i = 1
                pass
            else:
                #print(row)
                SelectByHotkeys.append(float(row[AttributeList.index("SelectByHotkeys")]))
                AssignToHotkeys.append(float(row[AttributeList.index("AssignToHotkeys")]))

                NumberOfPACs.append(float(row[AttributeList.index("NumberOfPACs")]))
                GapBetweenPACs.append(float(row[AttributeList.index("GapBetweenPACs")]))

    print(SelectByHotkeys)
    print(AssignToHotkeys)
    print(NumberOfPACs)
    print(GapBetweenPACs)
    #print(str(min(actionInPacs)))
    #print(str(max(actionInPacs)))

    plotScatterFigure(SelectByHotkeys, AssignToHotkeys, "SBHC_vs_ATHK.png", "SelectByHotkeys", "AssignToHotkeys")
    #plotScatterFigure(NumberOfPACs, GapBetweenPACs, "NOP_vs_GBP.png", "NumberOfPACs", "GapBetweenPACs")
    #plotHistogram(actionInPacs, 10, "ActionsPACs.png", "ActionsPACs", "Frequencies")
    #plotHistogram(actionInPacs, 10, "actionInPacs.png")