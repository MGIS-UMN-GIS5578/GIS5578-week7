# GIS 5578 Week 7: Object Orientated Programming

### Purpose
The purpose of this lab to understand the intricacies of object orientated programming
Please take your time to answer the questions below using this code.

```python
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
```    

### Questions
Please 
1. What are the basic elements necessary for defining a class? Write it.
1. Describe in your own words what a class is?
1. What does the statement “import numpy as np” do in the function dataLoader?
1. What is the proper way to call a method (class-function)? From within the class definition. Also explain why.
1. How does this differ from calling a class method on an instance.
1. Finish the function gridStatistics?
1. Name all properties / variables that are belonged to the class grid
1. How do you initiate the object grid? What information must you provide it?
1. When an object/class is initiated what always runs?
1. Write a new function that will iterate through every column and row and provide the statistics.
1. Write the function columnStatistics.
1. What are all the functions of the class?
1. Which functions require external/user input? What are the benefits/drawbacks of having specific functions that handle external input?
1. Modify the function getRowStats so that it repeats until you enter in a valid row
1. Why do we return self.arrayStatistics(theArray) and what is it returning?
