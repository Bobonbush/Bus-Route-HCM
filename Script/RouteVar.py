class RouteVar : 
    def __init__(self , RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, Outbound, RunningTime):
        self._RouteId = RouteId
        self._RouteVarId = RouteVarId
        self._RouteVarName = RouteVarName
        self._RouteVarShortName = RouteVarShortName
        self._RouteNo = RouteNo
        self._StartStop = StartStop
        self._EndStop = EndStop
        self._Distance = Distance
        self._Outbound = Outbound
        self._RunningTime = RunningTime

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
        return self._RouteId
    
    @RouteId.setter
    def RouteId(self , routeId):
        self._RouteId = routeId
    
    @property
    def RouteVarId(self):
        return self._RouteVarId
    
    @RouteVarId.setter
    def RouteVarId(self , routeVarId):
        self._RouteVarId = routeVarId
    
    @property
    def RouteVarName(self):
        return self._RouteVarName 

    @RouteVarName.setter
    def RouteVarName(self , routeVarName):
        self._RouteVarName = routeVarName

    @property
    def RouteVarShortName(self):
        return self._RouteVarShortName

    @RouteVarShortName.setter
    def RouteVarShortName(self, routeVarShortName):
        self._RouteVarShortName = routeVarShortName

    @property
    def RouteNo(self):
        return self._RouteNo

    @RouteNo.setter
    def RouteNo(self, routeNo):
        self._RouteNo = routeNo

    @property
    def StartStop(self):
        return self._StartStop

    @StartStop.setter
    def StartStop(self, startStop):
        self._StartStop = startStop

    @property
    def EndStop(self):
        return self._EndStop

    @EndStop.setter
    def EndStop(self, endStop):
        self._EndStop = endStop

    @property
    def Distance(self):
        return self._Distance

    @Distance.setter
    def Distance(self, distance):
        self._Distance = distance

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, outbound):
        self._Outbound = outbound

    @property
    def RunningTime(self):
        return self._RunningTime
    
    @RunningTime.setter
    def RunningTime(self, runningTime):
        self._RunningTime = runningTime

    

    
    
    