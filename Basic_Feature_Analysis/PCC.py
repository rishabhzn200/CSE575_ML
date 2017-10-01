"""
For all the attributes from the 6-th attribute to the 20-th attribute, compute the 
Pearson Correlation Coefficient (PCC) between each two different attributes.
Plot the scatter figures for min and max PCC value attribute pairs. 

"""


import csv
import matplotlib.pyplot as plt
import numpy as np

AttributeList = ["GameID","LeagueIndex","Age","HoursPerWeek","TotalHours","APM","SelectByHotkeys","AssignToHotkeys","UniqueHotkeys","MinimapAttacks","MinimapRightClicks","NumberOfPACs","GapBetweenPACs","ActionLatency","ActionsInPAC","TotalMapExplored","WorkersMade","UniqueUnitsMade","ComplexUnitsMade","ComplexAbilitiesUsed"]

Attr6 = "APM"

AttributeList620 = AttributeList[5:] #attributes from 6 to 20th

AttributeAndDataDictionary = {}

PCCMatrix = np.zeros((AttributeList620.__len__(), AttributeList620.__len__()))


def plotScatterFigure(X, Y, filename, xlabel, ylabel, text):
    #plt.hist2d

    plt.scatter(X, Y, c="red", alpha=0.5, edgecolors="black")
    plt.title(xlabel + "_VS_" + ylabel + " " + text)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt._show()

    pass



def CalculatePCC(X,Y):
    return np.corrcoef(X,Y)[0,1];


if __name__ == "__main__":

    inputCsvFile = "./SkillCraft1_Dataset.csv"

    with open(inputCsvFile, "r") as fileObj:
        reader = csv.reader(fileObj, delimiter=',', quotechar='"')

        #for attributeName in AttributeList620:

        i = 0
        for row in reader:
            if i==0:
                i = 1
                pass
            else:
                #print(row)
                for attributeName in AttributeList620:
                    if attributeName not in AttributeAndDataDictionary.keys():
                        AttributeAndDataDictionary[attributeName] = []
                    AttributeAndDataDictionary[attributeName].append(float(row[AttributeList.index(attributeName)]))

            #AttributeAndDataDictionary[attributeName] = newDataList

    indexRow = -1
    indexCol = -1
    PCCmin = 0
    AttrXMin = ""
    AttrYMin = ""

    PCCmax = 0
    AttrXMax = ""
    AttrYMax = ""

    initDone = 0

    for attributeNameX in AttributeAndDataDictionary.keys():
        indexRow = indexRow + 1
        indexCol = -1
        for attributeNameY in AttributeAndDataDictionary.keys():
            indexCol = indexCol + 1

            PX = AttributeAndDataDictionary[attributeNameX].__len__()
            PY = AttributeAndDataDictionary[attributeNameY].__len__()

            if PX != PY:
                c = 10
                pass

            PCC = CalculatePCC(AttributeAndDataDictionary[attributeNameX], AttributeAndDataDictionary[attributeNameY])
            PCCMatrix[indexRow][indexCol] = PCC

            #keep track of min and max PCC
            if attributeNameX != attributeNameY:
                if initDone == 0:
                    PCCmin = PCC
                    AttrXMin = attributeNameX
                    AttrYMin = attributeNameY

                    PCCmax = PCC
                    AttrXMax = attributeNameX
                    AttrYMax = attributeNameY
                    initDone = 1
                else:
                    if PCC < PCCmin:
                        PCCmin = PCC
                        AttrXMin = attributeNameX
                        AttrYMin = attributeNameY

                    if PCC > PCCmax:
                        PCCmax = PCC
                        AttrXMax = attributeNameX
                        AttrYMax = attributeNameY

    a = 20

    outputfileobj = open("matrix.csv", "w")
    outputfileobj.write(",")
    for attributeName in AttributeAndDataDictionary.keys():
        outputfileobj.write(attributeName + ',')
    outputfileobj.write('\n')
    row, col = PCCMatrix.shape
    for i in range(0,row):
        #print(i)
        outputfileobj.write(list(AttributeAndDataDictionary)[i] + ',')
        for j in range(0,col):
            outputfileobj.write(str(PCCMatrix[i][j]) + ",")
        outputfileobj.write("\n")


    outputfileobj.close()


    #Minimum PCC, PCCmin = PCC, AttrXMin = attributeNameX, AttrYMin = attributeNameY
    X_ListMin = AttributeAndDataDictionary[AttrXMin]
    Y_ListMin = AttributeAndDataDictionary[AttrYMin]
    plotScatterFigure(X_ListMin, Y_ListMin, AttrXMin + "_vs_" + AttrYMin +".png", AttrXMin, AttrYMin, "PCC = "+str(PCCmin))

    X_ListMax = AttributeAndDataDictionary[AttrXMax]
    Y_ListMax = AttributeAndDataDictionary[AttrYMax]
    plotScatterFigure(X_ListMax, Y_ListMax, AttrXMax + "_vs_" + AttrYMax + ".png", AttrXMax, AttrYMax, "PCC = "+str(PCCmax))
