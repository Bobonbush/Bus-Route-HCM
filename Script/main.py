from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from Path import Path



class Program :
    def __init__(self):
        self.VarQueryAnswer = RouteVarQuery()   
        self.StopQueryAnswer = StopQuery()
        
    def run(self):
        self.VarQueryAnswer.load_from_json()
        self.StopQueryAnswer.load_from_json()
       
        self.VarQueryAnswer.outputAsCSV(self.VarQueryAnswer.routeVars)
       
        list = self.VarQueryAnswer.SearchByAnything(RouteId = 1)
        self.VarQueryAnswer.outputAsJSON(self.VarQueryAnswer.routeVars)


        self.StopQueryAnswer.outputAsCSV(self.StopQueryAnswer.stop)

        self.StopQueryAnswer.outputAsJSON(self.StopQueryAnswer.stop)



def main() :
    p = Program()
    p.run()



main()