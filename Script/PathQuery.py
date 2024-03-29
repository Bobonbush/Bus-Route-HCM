from Path import Path
from Path import Point
import pyproj
import json
import csv






class PathQuery:
    field = ['RouteId' , 'RouteVarId']
    csvFile = "OutputCsv/path.csv"
    jsonFile = "OutputJson/path.json"
    def __init__(self):
        self.path = []
        PathQuery.jsonFile = open(PathQuery.jsonFile, 'w' , encoding= 'utf-8')
        PathQuery.csvFile = open(PathQuery.csvFile, 'w' , encoding= 'utf-8')
    def load_from_json(self):

        file = open('Json/paths.json', encoding= 'utf-8' )
        P = pyproj.Proj(proj='utm', zone=31, ellps='WGS84', preserve_units=True)
        G = pyproj.Geod(ellps='WGS84')
        
        for line in file : 
            data = json.loads(line); 
            latitudes = data["lat"]
            longtitudes = data["lng"]
            RouteId = data["RouteId"]
            RouteVarId = data["RouteVarId"]
            self.path.append(Path(RouteId , RouteVarId))

            for lat, lng in zip(latitudes , longtitudes):
                x , y = P(lng, lat);
                point = Point(x, y)
                self.path[self.path.len()].append(point)
        file.close()
    

    def OutputAsCsv(self):
        csvfilewriter = csv.writer(PathQuery.csvFile , dialect='excel')
        csvfilewriter.writerow(PathQuery.field)
        for item in self.path:
            csvfilewriter.writerow([item.RouteId , item.RouteVarId])


    def OutputAsJson(self , list):
        for item in list:
            json.dump(item.properties, PathQuery.jsonFile, ensure_ascii=False)
            PathQuery.jsonFile.write('\n')

    def SearchByAnything(self, **kwargs):
        list = []
        for item in self.path:
            ok = True
            for key, value in kwargs.items():
                if item.properties[key] != value:
                    ok = False
                    break
            if ok:
                list.append(item)
        return list