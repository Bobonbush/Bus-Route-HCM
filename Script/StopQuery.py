from Stop import Stop
import json
import csv

class StopQuery :
    csvfile = "OutputCsv/stops.csv"
    jsonfile = "OutputJson/stops.json"
    field = ['StopId', 'Code', 'Name', 'StopType', 'Zone', 'Ward', 'AddressNo', 'Street', 'SupportDisability', 'Status', 'Lng', 'Lat', 'Search', 'Routes' , 'RouteId', 'RouteVarId']
    def __init__(self):
        self.stop = []
        StopQuery.jsonfile = open(StopQuery.jsonfile, 'w'  , encoding= 'utf-8')
        StopQuery.csvfile = open(StopQuery.csvfile, 'w' , newline = '', encoding= 'utf-8')
    
    def load_from_json(self):
        file = open('Json/stops.json', encoding= 'utf-8' )
        for line in file : 
            data = json.loads(line);
            
            for item in data["Stops"] :
                self.stop.append(Stop(item['StopId'], item['Code'], item['Name'], item['StopType'], item['Zone'], item['Ward'], item['AddressNo'], item['Street'], item['SupportDisability'], 
                                      item['Status'], item['Lng'], item['Lat'], item['Search'], item['Routes'] , data['RouteId'], data['RouteVarId']))
        file.close()

    def SearchByAnything(self, **kwargs):
        list = []
        for item in self.stop:
            ok = True
            for key, value in kwargs.items():
                if str(item.properties[key]).lower() == str(value).lower():
                    continue
                ok = False
            if(ok):
                list.append(item)
        return list

    def outputAsCSV(self, list):
        
        csvfilewriter = csv.writer(StopQuery.csvfile , dialect='excel')
        csvfilewriter.writerow(StopQuery.field )
        for item in list :
            csvfilewriter.writerow([item.StopId, item.Code, item.Name, item.StopType, item.Zone, item.Ward, item.AddressNo, item.Street, item.SupportDisability, item.Status, item.Lng, item.Lat, item.Search, item.Routes , item.RouteId , item.RouteVarId])
            
    def outputAsJSON(self, list):
        for item in list:
            json.dump(item.properties, StopQuery.jsonfile, ensure_ascii=False)
            StopQuery.jsonfile.write('\n')
    
    
    def OutputDebug(self):
        for item in self.stop:
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
                print(item.RouteId)
                print(item.RouteVarId)
    
    
    

    
    
    def StopWorking(self):
        print("Stop Working")
        StopQuery.jsonfile.close()
        StopQuery.csvfile.close()
        exit()



    
