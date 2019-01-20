#!/usr/bin/python

#######################################
#                                     #
#   Making the UI for the OpenGraph   #
#    Man, Guis suck, so does this     #
#                                     #
#######################################


import matplotlib.pyplot as plt
from Tkinter import *

import serial
import time
import math

import GraphMath

top = Tk()
top.title("OpenGraph")

class Graph():
    def __init__(self, xArray, yArray, xAxisLabel, yAxisLabel):
        self.xArray = xArray
        self.yArray = yArray
        self.xAxisLabel = xAxisLabel
        self.yAxisLabel = yAxisLabel

    def plotData(self):
        plt.plot(self.xArray, self.yArray)
        plt.xlabel(self.xAxisLabel)
        plt.ylabel(self.yAxisLabel)
        plt.title(self.xAxisLabel + " vs. " + self.yAxisLabel)
        plt.show()

##Pthis object places all the items in the page

class MainWindow():
    def __init__(self, datObject, graphObject, widgetArray):
        self.datObject = datObject
        self.graphObject = graphObject
        self.startStopButton = Button(top, text="Start", command=self.datObject.DefineData)
        self.calculations = Button(top, text="Caclulate Statistics", command=self.updateStatistics)
        self.plotData = Button(top, text="Plot Test", command = self.graphObject.plotData)
        self.startStopButton.grid(top, row=0, column=0)
        self.calculations.grid(top, row=1, column=0)
        self.plotData.grid(top, row= 0, column= 1)

        self.objectsArray = widgetArray

        for ob in self.objectsArray:
            ob.placeWidget()

class Stats():
    def __init__(self, name, row, column):
        self.name = name
        self.value = ""
        self.rowPos = row
        self.columnPos = column
        self.labelWidget = Label(top, text= self.name + ": ")
        self.valueWidget = Label(top, text = self.value)

    def update(self, value):
        self.valueWidget.delete('1.0', END)
        self.valueWidget.insert(END, value)

    def placeWidget(self):
        self.labelWidget.grid(top, row=self.rowPos, column=self.columnPos)
        self.valueWidget.grid(top, row=self.rowPos, column=self.columnPos + 1)


objectArray = [Stats("Mean", 2, 0),\
                Stats("Median", 3, 0),\
                Stats("Mode", 4, 0), \
                Stats("Range", 5, 0), \
                Stats("Standard Deviation", 6, 0)]
#graph1 = Graph([1,2,3,6,5], [5,13,5,1,1] , "testX", "testY")
#graph1.plotData()
dataObject = Data()
wandow = MainWindow(dataObject, Graph(dataObject.getX(),dataObject.getY(), "test y", "Time"), objectArray)




top.mainloop()