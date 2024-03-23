import pyproj
import json
import math



class Point :
    def __init__(self, x, y):
        self._x = x ;
        self._y = y ;
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y
    
    @y.setter

    def y(self, y):
        self._y = y
class Path :

    R = 6371.0 # radius of the earth in km
    def __init__(self) :
        self.points = []
    


    def load_from_json(self):

        file = open('Json/paths.json', encoding= 'utf-8' )
        for line in file : 
            data = json.loads(line); 
            for item in data :
                lat = item['Lat']
                lng = item['Lng']
                xCoord = [(Path.R * math.radians(longtitude - lng[0])) for longtitude in lng]
                yCoord = [(Path.R * math.log(math.tan(math.pi/4 + math.radians(latitude)/2))) for latitude in lat]
                for x, y in zip(xCoord , yCoord):
                    point = Point(x, y)
                    self.points.append(point)
        file.close()

    def DebugOutput(self):
        for item in self.points:
            print(item.x)
            print(item.y)
