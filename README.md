# GIS 5578 Week 7: Object Orientated Programming

### Purpose
The purpose of this lab to understand the intricacies of object orientated programming
Please take your time to answer the questions below using this code.

```python
class Raster(object):
    
    def __init__(self, thePoint, res, rows=10, cols=10):
        """
        A nice doc string here
        """
        if isinstance(thePoint, Point):
            self.thePoint = thePoint
            self.x = self.thePoint.x
            self.y = self.thePoint.y
            
        else:
            print("Not a valid point object")
            
        self.resolution = res
        self.rows = rows
        self.cols = cols
    
    def something():
        pass
    
class DataRaster(Raster):

    def __init__(self, thePoint, res, dataset):
        import numpy as np
        self.data = np.array(dataset)
        rows, cols = self.data.shape
        #Old style for inheriting
        #Raster.__init__(self,point, res, rows, cols)
        #New style inheriting using super
        super().__init__(thePoint, res, rows, cols)
```    

### Questions
Please 
1. What are the basic elements necessary for defining a class? Write it.
1. Describe in your own words what a class is?
1. What is the proper way to call a method (class-function)? From within the class definition. Also explain why.
1. How does this differ from calling a class method on an instance.
1. Name all properties / variables that are belonged to the Raster class.
1. How do you initiate the Raster grid? What information must you provide it?
1. When an object/class is initiated how do you make sure a method always runs?
1. Think about lab 3, write a method that calculates the statistics.
1. Which functions require external/user input? What are the benefits/drawbacks of having specific functions that handle external input?
1. Write a method getRowStats so that it asks for user input until you enter in a valid row
1. How do we return data from the class method?
