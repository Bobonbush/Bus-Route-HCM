class RouteVar : 
    def __init__(self , RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, Outbound, RunningTime):

        self.properties = {}
        self.properties['RouteId'] = RouteId
        self.properties['RouteVarId'] = RouteVarId
        self.properties['RouteVarName'] = RouteVarName
        self.properties['RouteVarShortName'] = RouteVarShortName
        self.properties['RouteNo'] = RouteNo
        self.properties['StartStop'] = StartStop
        self.properties['EndStop'] = EndStop
        self.properties['Distance'] = Distance
        self.properties['Outbound'] = Outbound
        self.properties['RunningTime'] = RunningTime
    
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

    @property
    def RouteVarName(self):
        return self.properties['RouteVarName']
    
    @RouteVarName.setter
    def RouteVarName(self , RouteVarName):
        self.properties['RouteVarName'] = RouteVarName

    @property
    def RouteVarShortName(self):
        return self.properties['RouteVarShortName']
    
    @RouteVarShortName.setter
    def RouteVarShortName(self , RouteVarShortName):
        self.properties['RouteVarShortName'] = RouteVarShortName

    @property
    def RouteNo(self):
        return self.properties['RouteNo']
    
    @RouteNo.setter

    def RouteNo(self , RouteNo):
        self.properties['RouteNo'] = RouteNo
    
    @property
    def StartStop(self):
        return self.properties['StartStop']
    
    @StartStop.setter
    def StartStop(self , StartStop):
        self.properties['StartStop'] = StartStop
    
    @property
    def EndStop(self):
        return self.properties['EndStop']
    
    @EndStop.setter
    def EndStop(self , EndStop):
        self.properties['EndStop'] = EndStop
    
    @property
    def Distance(self):
        return self.properties['Distance']
    
    @Distance.setter
    def Distance(self , Distance):
        self.properties['Distance'] = Distance

    @property
    def Outbound(self):
        return self.properties['Outbound']
    
    @Outbound.setter
    def Outbound(self , Outbound):
        self.properties['Outbound'] = Outbound

    @property
    def RunningTime(self):
        return self.properties['RunningTime']
    
    @RunningTime.setter
    def RunningTime(self , RunningTime):
        self.properties['RunningTime'] = RunningTime

    

    

    

    
    
    