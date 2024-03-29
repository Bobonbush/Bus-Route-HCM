class Stop :
    def __init__(self, StopId, Code, Name, StopType, Zone, Ward, AddressNo, Street, SupportDisability, Status, Lng, Lat, Search, Routes , RouteId , RouteVarId):
        self.properties = {}
        self.properties['StopId'] = StopId
        self.properties['Code'] = Code
        self.properties['Name'] = Name
        self.properties['StopType'] = StopType
        self.properties['Zone'] = Zone
        self.properties['Ward'] = Ward
        self.properties['AddressNo'] = AddressNo
        self.properties['Street'] = Street
        self.properties['SupportDisability'] = SupportDisability
        self.properties['Status'] = Status
        self.properties['Lng'] = Lng
        self.properties['Lat'] = Lat
        self.properties['Search'] = Search
        self.properties['Routes'] = Routes
        self.properties['RouteId'] = RouteId
        self.properties['RouteVarId'] = RouteVarId
    @property
    def StopId(self):
        return self.properties['StopId']
    
    @StopId.setter
    def StopId(self , stopId):
        self.properties['StopId'] = stopId
    
    @property
    def Code(self):
        return self.properties['Code']
    
    @Code.setter
    def Code(self , code):
        self.properties['Code'] = code
    
    @property
    def Name(self):
        return self.properties['Name']
    
    @Name.setter
    def Name(self , name):
        self.properties['Name'] = name
    
    @property
    def StopType(self):
        return self.properties['StopType']
    
    @StopType.setter
    def StopType(self , stopType):
        self.properties['StopType'] = stopType

    @property
    def Zone(self):
        return self.properties['Zone']
    
    @Zone.setter
    def Zone(self , zone):
        self.properties['Zone'] = zone

    @property
    def Ward(self):
        return self.properties['Ward']
    
    @Ward.setter
    def Ward(self , ward):
        self.properties['Ward'] = ward
    
    @property
    def AddressNo(self):
        return self.properties['AddressNo']
    
    @AddressNo.setter
    def AddressNo(self , addressNo):
        self.properties['AddressNo'] = addressNo
    
    @property
    def Street(self):
        return self.properties['Street']
    
    @Street.setter
    def Street(self , street):
        self.properties['Street'] = street
    
    @property
    def SupportDisability(self):
        return self.properties['SupportDisability']
    
    @SupportDisability.setter
    def SupportDisability(self , supportDisability):
        self.properties['SupportDisability'] = supportDisability
    
    @property
    def Status(self):
        return self.properties['Status']
    
    @Status.setter
    def Status(self , status):
        self.properties['Status'] = status

    @property
    def Lng(self):
        return self.properties['Lng']
    
    @Lng.setter
    def Lng(self , lng):
        self.properties['Lng'] = lng
    
    @property
    def Lat(self):
        return self.properties['Lat']
    
    @Lat.setter
    def Lat(self , lat):
        self.properties['Lat'] = lat
    
    @property
    def Search(self):
        return self.properties['Search']
    
    @Search.setter
    def Search(self , search):
        self.properties['Search'] = search
    
    @property
    def Routes(self):
        return self.properties['Routes']
    
    @Routes.setter
    def Routes(self , routes):
        self.properties['Routes'] = routes
    
    @property
    def RouteId(self):
        return self.properties['RouteId']
    
    @RouteId.setter
    def RouteId(self , routeId):
        self.properties['RouteId'] = routeId

    @property
    def RouteVarId(self):
        return self.properties['RouteVarId']
    
    @RouteVarId.setter
    def RouteVarId(self , routeVarId):
        self.properties['RouteVarId'] = routeVarId


