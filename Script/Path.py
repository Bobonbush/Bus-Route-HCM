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
    
    def __init__(self, RouteId, RouteVarId) :
        self.points = [] 
        self.properties ['RouteId'] = RouteId
        self.properties['RouteVarId'] = RouteVarId
    
    @property 
    def RouteId(self):
        return self.properties['RouteId']
    
    @RouteId.setter
    def RouteId(self, RouteId):
        self.properties['RouteId'] = RouteId
    

    @property
    def RouteVarId(self):
        return self.properties['RouteVarId']
    
    @RouteVarId.setter
    def RouteVarId(self, RouteVarId) :
        self.properties['RouteVarId'] = RouteVarId
    

    

    def DebugOutput(self):
        
        for item in self.points:
            print(item.x , end = ' ')
            print(item.y)

    
