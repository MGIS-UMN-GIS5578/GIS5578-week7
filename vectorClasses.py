# -*- coding: utf-8 -*-
"""
Created updated Thu Oct 22 2018

@author: dahaynes
"""

class Point(object):
    
    def __init__(self,x,y):
        for c, i in enumerate([x,y]):
            flag = self.CheckValues(i)
            if flag:
                if c == 0: self.x = x
                if c == 1: self.y = y
            else:
                print("Error not a valid point")
                self.__del__()   
                

    def __del__(self):
        pass
        #if self.name: del self.name
        
    
    def __str__(self):
        """ 
        This returns the string representation of the point
        """
        return "X:%s , Y:%s" % (self.x, self.y)
        
    def CheckValues(self, theValue):
        """
        This method determines if the value is a valid floating point number
        """
        if str(theValue).isdigit(): 
            return 1
        else:
            print("invalid value")
            return 0
        
    def SetName(self,theName):
        """
        This function sets the name of the point
        """
        self.name = theName
    
    def ChangeValue(self, x=None, y=None):
        if x and self.CheckValues(x):
            self.x = x
        elif y:
            self.y = y
        else:
            pass
        
        self.PrintXYLocation()
    
    def PrintXYLocation(self):
        """
        This is a function
        """
        print(self.x, self.y)

        
class Line(object):
    
    def __init__(self,start,end):
        
        self.start = start
        self.end = end
        self.CalcLength()
        
    def CalcLength(self,):
        
        X1 = self.start.x
        X2 = self.end.x
        
        Y1 = self.start.y
        Y2 = self.end.y      
        
        #This formula calculates the hypotenuse for two points.
        self.length = ((X2-X1)**2 + (Y2-Y1)**2)**.5
        return self.length

class Polygon(object):
    
    def __init__(self, *args):
        
        
        self.linesegments = args
        self.line1, self.line2, self.line3, = self.linesegments
#        self.line1 = line1
#        self.line2 = line2
#        self.line3 = line3
        
    
    def CalculatePerimeter(self,):
        
        self.perimeter = 0
        for l in  [self.line1, self.line2, self.line3]:
            self.perimeter += l.CalcLength()

    def CalculateArea(self,):
        self.listofPoints = []
        for l in  [self.line1, self.line2, self.line3]:
            self.listofPoints.append( (l.start.x,l.start.y) )
            self.listofPoints.append( (l.end.x,l.end.y) )
        
        self.uniquePoints = set(self.listofPoints)
        
        a,b,c = list(self.uniquePoints)
        
        self.area = abs( a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1])+ c[0]*(a[1]-b[1]) ) /2
