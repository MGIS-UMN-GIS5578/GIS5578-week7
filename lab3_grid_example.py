# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:04:57 2018

@author: dahaynes
"""

class mygrid(object):

    def __init__(self, inputdata):
        self.data = self.dataLoader(inputdata)
        self.shape = self.data.shape
        self.rows, self.cols = self.shape

    def dataLoader(self, inputdata):
        import numpy as np
        if type(inputdata) == list:
            data = np.array(inputdata, dtype=np.integer)
            #self.data = np.array(inputdata)
            #inputdata is a list
        elif isinstance(inputdata, str):
            data = np.array(self.convertCSVtolist(inputdata, dtype=np.integer))
        else:
            print("invalid data type")
        return data

    def convertCSVtolist(self, filepath):
        import csv
        outdata = []
        with open(filepath, 'rb') as fin:
            reader = csv.reader(fin)
            for row in reader:
                outdata.append(row)
        return outdata

    def gridStatistics(self):
        pass
            
    def getInput(self, phrase, ):
        value = input(phrase)
        return value
    
    def arrayStatistics(self,theArray):
        theMin = theArray.min()
        theMax = theArray.max()
        theMean = theArray.mean()
        print(theMin, theMax, theMean)
        return theMin, theMax, theMean

    def getRowStats(self,):
        row  = int(self.getInput("Please enter the row: "))
        if row >= 0 and row <= self.rows:
            theArray = self.data[row,:]
            return self.arrayStatistics(theArray)
        else:
            print("Entered an in invalid value")
    
    def getStats(self, row=Ellipsis, col=Ellipsis):
        """
        Ellipsis is a numpy object that will substitute for ":"
        """
        pass
    
        
