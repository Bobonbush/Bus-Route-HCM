from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from PathQuery import PathQuery
from geospatial import geospatial
from shapely.geometry import *
from rtree import index



class Program :
    def __init__(self):
        self.VarQueryAnswer = RouteVarQuery()   
        self.StopQueryAnswer = StopQuery()
        self.PathQueryAnswer = PathQuery()

        geospatial.init()


        
    def run(self):
        self.VarQueryAnswer.load_from_json()
        self.StopQueryAnswer.load_from_json()
        self.PathQueryAnswer.load_from_json()


        self.VarQueryAnswer.outputAsCSV(self.VarQueryAnswer.routeVars)
       
        list = self.VarQueryAnswer.SearchByAnything(RouteId = 1)
        self.VarQueryAnswer.outputAsJSON(self.VarQueryAnswer.routeVars)


        self.StopQueryAnswer.outputAsCSV(self.StopQueryAnswer.stop)

        self.StopQueryAnswer.outputAsJSON(self.StopQueryAnswer.stop)

        self.PathQueryAnswer.outputAsJSON(self.PathQueryAnswer.path)
    
        self.PathQueryAnswer.outputAsCSV(self.PathQueryAnswer.path)


        print(geospatial.TransformLatLngToXY(55.0, 12.0))
        print(geospatial.TransformXYToLatLng(308124.3678603405 ,6098907.825005012 ))

        
        
        polygon1 = self.PathQueryAnswer.getPolygon([self.PathQueryAnswer.path[0]])
        polygon2 = self.PathQueryAnswer.getPolygon([self.PathQueryAnswer.path[2]])

        
        union = geospatial.UnionPolygons(polygon1, polygon2)
        geospatial.DrawPolygon(union)


        intersect = geospatial.IntersectPolygons(polygon1, polygon2)
        geospatial.DrawPolygon(intersect)


        difference = geospatial.DifferencePolygons(polygon1, polygon2)
        geospatial.DrawPolygon(difference)


        #print(self.PathQueryAnswer.ConvertFromIndextoCoordinates(self.PathQueryAnswer.SearchPointsRange(10, 0,11, 107)))
        
        
        print(self.PathQueryAnswer.ConvertFromIndextoCoordinates(self.PathQueryAnswer.SearchNearstPoint(10, 0 , 3)))


        #Close all the files after doing query
        self.PathQueryAnswer.StopWorking()
        self.StopQueryAnswer.StopWorking()
        self.VarQueryAnswer.StopWorking()
        

def main() :
    p = Program()
    p.run()



if __name__ == "__main__":
    main()