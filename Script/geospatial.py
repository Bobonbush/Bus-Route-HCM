import pyproj


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

