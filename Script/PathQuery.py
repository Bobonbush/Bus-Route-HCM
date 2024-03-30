from Path import Path
import json
import csv


class PathQuery :
    
    field = ['lat', 'lng', 'RouteId', 'RouteVarId']
    jsonFile = 'OutputJson/Path.json'
    csvFile = 'OutputCsv/Path.csv'

    def __init__(self):
        self.path = []
        PathQuery.csvFile = open(PathQuery.csvFile, 'w' , newline = '', encoding= 'utf-8')
        PathQuery.jsonFile = open(PathQuery.jsonFile, 'w' , encoding= 'utf-8')
    

    def load_from_json(self):
        file = open('Json/paths.json', encoding= 'utf-8' )
        for line in file : 
            data = json.loads(line); 
            lat = data['lat']
            lng = data['lng']
            
            RouteId = data['RouteId']
            RouteVarId = data['RouteVarId']
            
            self.path.append(Path(lat, lng, RouteId, RouteVarId))
        file.close()

    def SearchByAnything(self, **kwargs):
        list = []
        for item in self.path:
            ok = True    
            for key,value in kwargs.items():
                if str(item.properties[key]).lower() == str(value).lower():
                    continue
                ok = False
                
            if(ok == True):
                list.append(item)
        return list
    
    def outputAsCSV(self, list):
        csvfilewriter = csv.writer(PathQuery.csvFile , dialect='excel')
        csvfilewriter.writerow(PathQuery.field )
        for item in list :
            csvfilewriter.writerow([item.lat, item.lng, item.RouteId, item.RouteVarId])
    

    def outputAsJSON(self, list):
        for item in list:
            json.dump(item.properties, PathQuery.jsonFile, ensure_ascii=False)
            PathQuery.jsonFile.write('\n')


    def OutputDebug(self):
        for item in self.path:
            print(item.lat)
            print(item.lng)
            print(item.RouteId)
            print(item.RouteVarId)
