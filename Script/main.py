from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from PathQuery import PathQuery
from geospatial import geospatial



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

    
        self.PathQueryAnswer.drawPolygon(self.PathQueryAnswer.path)

        #Close all the files after doing query
        self.PathQueryAnswer.StopWorking()
        self.StopQueryAnswer.StopWorking()
        self.VarQueryAnswer.StopWorking()
        

def main() :
    p = Program()
    p.run()



if __name__ == "__main__":
    main()