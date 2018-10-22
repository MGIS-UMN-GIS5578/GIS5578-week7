# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:52:19 2018

@author: dahaynes
"""

class Raster(object):
    
    def __init__(self, point, res, rows=10, cols=10):
        """
        A nice doc string here
        """
        if isinstance(point, Point):
            self.point = point
            self.x = self.point.x
            self.y = self.point.y
            
        else:
            print("Not a valid point object")
            
        self.resolution = res
        self.rows = rows
        self.cols = cols
    
    def something():
        pass
    
class DataRaster(Raster):

    def __init__(self, point, res, dataset):
        import numpy as np
        self.data = np.array(dataset)
        rows, cols = self.data.shape
        #Old style for inheriting
        #Raster.__init__(self,point, res, rows, cols)
        #New style inheriting using super
        super().__init__(point, res, rows, cols)
        