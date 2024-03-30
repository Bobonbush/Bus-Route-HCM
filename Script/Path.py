class Path:
    def __init__(self , lat , lng ,  RouteId, RouteVarId):
        self.properties = {}
        self.properties['lat'] = lat
        self.properties['lng'] = lng
        self.properties['RouteId'] = RouteId
        self.properties['RouteVarId'] = RouteVarId
    
    @property
    def lat(self):
        return self.properties['lat']
    
    @lat.setter
    def lat(self , lat):
        self.properties['lat'] = lat

    @property
    def lng(self):
        return self.properties['lng']
    
    @lng.setter
    def lng(self , lng):
        self.properties['lng'] = lng
    
    @property
    def RouteId(self):
        return self.properties['RouteId']
    
    @RouteId.setter
    def RouteId(self , RouteId):
        self.properties['RouteId'] = RouteId
    
    @property
    def RouteVarId(self):
        return self.properties['RouteVarId']
    
    @RouteVarId.setter
    def RouteVarId(self , RouteVarId):
        self.properties['RouteVarId'] = RouteVarId
    

    

    