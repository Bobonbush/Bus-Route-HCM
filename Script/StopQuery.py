from Stop import Stop
import json
import csv

class StopQuery :
    csvfile = "OutputCsv/stops.csv"
    jsonfile = "OutputJson/stops.json"
    field = ['StopId', 'Code', 'Name', 'StopType', 'Zone', 'Ward', 'AddressNo', 'Street', 'SupportDisability', 'Status', 'Lng', 'Lat', 'Search', 'Routes']
    def __init__(self):
        self.stops = []
        StopQuery.jsonfile = open(StopQuery.jsonfile, 'w' , encoding= 'utf-8')
        StopQuery.csvfile = open(StopQuery.csvfile, 'w' , encoding= 'utf-8')
    
    def load_from_json(self):
        file = open('Json/stops.json', encoding= 'utf-8' )
        for line in file : 
            data = json.loads(line);
            for item in data["Stops"] :
                stop = Stop(item['StopId'], item['Code'], item['Name'], item['StopType'], item['Zone'], item['Ward'], item['AddressNo'], item['Street'], item['SupportDisability'], item['Status'], item['Lng'], item['Lat'], item['Search'], item['Routes'])
                self.stops.append(stop)
        file.close()
    
    def OutputDebug(self):
        for item in self.stops:
            print(item.StopId)
            print(item.Code)
            print(item.Name)
            print(item.StopType)
            print(item.Zone)
            print(item.Ward)
            print(item.AddressNo)
            print(item.Street)
            print(item.SupportDisability)
            print(item.Status)
            print(item.Lng)
            print(item.Lat)
            print(item.Search)
            print(item.Routes)
    
    def SearchByAnything(self, **kwargs):
        list = []
        for item in self.stops:
            ok = True
            for key, value in kwargs.items():
                if str(item.properties[key]) == str(value):
                    continue
                ok = False
            if(ok):
                list.append(item)
        return list
    




    def SearchByStopId(self, StopId):
        list = []
        for item in self.stops:
            if item.StopId == StopId:
                list.append(item)
        return list
    
    def SearchByCode(self, Code):
        list = []
        for item in self.stops:
            if item.Code == Code:
                list.append(item)
        return list
    
    def SearchByName(self, Name):
        list = []
        for item in self.stops:
            if item.Name == Name:
                list.append(item)
        return list
    
    def SearchByStopType(self, StopType):
        list = []
        for item in self.stops:
            if item.StopType == StopType:
                list.append(item)
        return list
    
    def SearchByZone(self, Zone):
        list = []
        for item in self.stops:
            if item.Zone == Zone:
                list.append(item)
        return list
    
    def SearchByWard(self, Ward):
        list = []
        for item in self.stops:
            if item.Ward == Ward:
                list.append(item)
        return list
    
    def SearchByAddressNo(self, AddressNo):
        list = []
        for item in self.stops:
            if item.AddressNo == AddressNo:
                list.append(item)
        return list
    
    def SearchByStreet(self, Street):
        list = []
        for item in self.stops:
            if item.Street == Street:
                list.append(item)
        return list
    
    def SearchBySupportDisability(self, SupportDisability):
        list = []
        for item in self.stops:
            if item.SupportDisability == SupportDisability:
                list.append(item)
        return list
    
    def SearchByStatus(self, Status):
        list = []
        for item in self.stops:
            if item.Status == Status:
                list.append(item)
        return list
    
    def SearchByLng(self, Lng):
        list = []
        for item in self.stops:
            if item.Lng == Lng:
                list.append(item)
        return list
    
    def SearchByLat(self, Lat):
        list = []
        for item in self.stops:
            if item.Lat == Lat:
                list.append(item)
        return list
    
    def SearchBySearch(self, Search):
        list = []
        for item in self.stops:
            if item.Search == Search:
                list.append(item)
        return list
    
    def SearchByRoutes(self, Routes):
        list = []
        for item in self.stops:
            if item.Routes == Routes:
                list.append(item)
        return list
    
    def outputAsCSV(self, ans):
        writer = csv.DictWriter(StopQuery.csvfile, fieldnames=StopQuery.field)
        writer.writeheader()
        for item in ans:
            writer.writerow(item.properties)
    
    def outputAsJSON(self, ans):
        for item in ans:
            json.dump(item.properties, StopQuery.jsonfile, ensure_ascii=False)
            StopQuery.jsonfile.write('\n')
    
    def StopWorking(self):
        print("Stop Working")
        StopQuery.jsonfile.close()
        StopQuery.csvfile.close()
        exit()



    
