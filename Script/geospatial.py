import pyproj
from shapely.geometry import *
import json


class geospatial :
    
    @staticmethod
    def init():
        geospatial.LatLngCRS = pyproj.CRS("EPSG:4326")
        geospatial.XYCRS = pyproj.CRS("EPSG:3045")
        
        

    @staticmethod
    def TransformLatLngToXY(lat , lng ):
        transformer = pyproj.Transformer.from_crs(geospatial.LatLngCRS, geospatial.XYCRS, always_xy=True)
        x, y = transformer.transform(lng, lat)
        return x,y
    
    @staticmethod
    def TransformXYToLatLng(x , y ):
        transformer = pyproj.Transformer.from_crs(geospatial.XYCRS, geospatial.LatLngCRS, always_xy=True)
        lat, lng = transformer.transform(x, y)
        return lat,lng
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


