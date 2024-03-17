from Stop import Stop
import json
import csv

class StopQuery :
    csvfile = "stops.csv"
    jsonfile = "stops.json"
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
    
    def SearchByAnything(self, information, value):
        list = []
        for item in self.stops:
            if str(item.properties[information]) == str(value):
                list.append(item)
        print(list.__len__())
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



    
