import pyproj
from shapely.geometry import *
import json
from rtree import index
from shapely.ops import nearest_points
import math


class geospatial :
    
    @staticmethod
    def init():
        geospatial.LatLngCRS = pyproj.CRS("EPSG:4326")
        geospatial.XYCRS = pyproj.CRS("EPSG:3405")
        geospatial.TransformerXYtoLatLng = pyproj.Transformer.from_crs(geospatial.XYCRS, geospatial.LatLngCRS, always_xy=True)
        geospatial.TransformerLatLngToXY = pyproj.Transformer.from_crs(geospatial.LatLngCRS, geospatial.XYCRS, always_xy=True)
        

    @staticmethod
    def TransformLatLngToXY(lat , lng ):
        x, y = geospatial.TransformerLatLngToXY.transform(lng, lat)
        return x,y
    
    
    @staticmethod
    def TransformXYToLatLng(x , y ):
        lat, lng = geospatial.TransformerXYtoLatLng.transform(x, y)
        return lat,lng
    
    @staticmethod
    def Distance(x , y):
        return math.sqrt((x[0] - y[0] ) ** 2 + (x[1] - y[1]) ** 2) 
    
    @staticmethod
    def TimeTravel(Velocity , Distance):
        return Distance / Velocity


    @staticmethod
    def UnionPolygons(polygon1, polygon2):
        return polygon1.union(polygon2)
    
    @staticmethod
    def IntersectPolygons( polygon1, polygon2):
        return polygon1.intersection(polygon2)
    
    @staticmethod
    def DifferencePolygons( polygon1, polygon2):
        return polygon1.difference(polygon2)
    

    @staticmethod
    def DrawPolygon(polygon):
        with open("OutputJson/Geojson.json", 'w' , encoding= 'utf-8') as file :
            geojson = mapping(polygon)
            geojson = json.dumps(geojson )
            file.write(geojson)
            file.close()

    
                   
class RTreeQuery:
    
    
    def __init__(self):
        self.idx = index.Index()
        self.values = []
    def Insert(self, data_points):
        for i, (lat, lon) in enumerate(data_points):
            self.idx.insert(i, (lat, lon, lat, lon))
            self.values.append((lat ,lon))
    

    def Delete(self, id):
        self.idx.delete(2)
    

    def Search(self, min_longitude, min_latitude, max_longitude, max_latitude):
        search_bounds = box(min_longitude, min_latitude, max_longitude, max_latitude)

        # Perform range search
        result_ids = list(self.idx.intersection(search_bounds.bounds)) 
        
        return result_ids

        

    def NearstPoint(self, lat, lon , num):
        return list(self.idx.nearest((lat , lon) , num))            # Number of nearest points
        


    
    


