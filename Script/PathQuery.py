from Path import Path
import json
import csv
from shapely.geometry import *
from geospatial import RTreeQuery


class PathQuery :
    
    field = ['lat', 'lng', 'RouteId', 'RouteVarId']
    jsonFile = 'OutputJson/Path.json'
    csvFile = 'OutputCsv/Path.csv'
    
    def __init__(self):
        self.path = []
        PathQuery.csvFile = open(PathQuery.csvFile, 'w' , newline = '', encoding= 'utf-8')
        PathQuery.jsonFile = open(PathQuery.jsonFile, 'w' , encoding= 'utf-8')
        self.index = RTreeQuery()
 

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
        self.LoadDatatoRTree() ## Load data to RTree


                 

    def LoadDatatoRTree(self):
        data_points = []
        for item in self.path:
            for (latitude, longitude) in zip(item.lat, item.lng):
                data_points.append((latitude, longitude))
        self.index.Insert(data_points)


    def SearchPointsRange(self, lat1, lng1, lat2, lng2):        # [(lat1, lng1) to (lat2 ,lng2)]
        return self.index.Search(lat1, lng1, lat2, lng2)
    
    def SearchNearstPoint(self, lat, lng , num):
        return self.index.NearstPoint(lat, lng , num)
    
    def ConvertFromIndextoCoordinates(self , list):
        points = []
        for item in list:
            points.append(self.index.values[item])
        
        return points

    





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

    def drawPoint(self, list):
        with open("OutputJson/Geojson.json", 'w' , encoding= 'utf-8') as file :
            
            points = []
            for item in list :
                for (longitude, latitude) in zip(item.lng, item.lat):
                    points.append({
                            "type": "Point",
                            "coordinates": [longitude, latitude]
                    })
            geojson = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": point,
                        "properties": {}  # You can add properties if needed
                    }
                    for point in points
                ]
            }
            json.dump(geojson , file , ensure_ascii=False)
            
            file.close()

    def drawLineString(self, list):
        with open("OutputJson/Geojson.json", 'w' , encoding= 'utf-8') as file :
            
            points = []
            for item in list :
                coord = []
                for (longitude, latitude) in zip(item.lng, item.lat):
                    coord.append([longitude, latitude])
                points.append({
                        "type": "LineString",
                        "coordinates": coord
                })
            geojson = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": point,
                        "properties": {}  # You can add properties if needed
                    }
                    for point in points
                ]
            }
            json.dump(geojson , file , ensure_ascii=False)
            
            file.close()


    
    def drawPolygon(self, list):
        with open("OutputJson/Geojson.json", 'w' , encoding= 'utf-8') as file :
            
            points = []
            for item in list :
                coord = []
                for (longitude, latitude) in zip(item.lng, item.lat):
                    coord.append([longitude, latitude])
                points.append({
                        "type": "Polygon",
                        "coordinates": [coord]
                })
            geojson = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": point,
                        "properties": {}  # You can add properties if needed
                    }
                    for point in points
                ]
            }
            json.dump(geojson , file , ensure_ascii=False)
            
            file.close()
    


    def getPolygon(self, list):
        points = []
        for item in list :
            for (longitude, latitude) in zip(item.lng, item.lat):
                points.append([longitude, latitude])
        points = Polygon(points).buffer(0)

        return points
    


        




    def OutputDebug(self):
        for item in self.path:
            print(item.lat)
            print(item.lng)
            print(item.RouteId)
            print(item.RouteVarId)

    def StopWorking(self):
        PathQuery.csvFile.close()
        PathQuery.jsonFile.close()

        
