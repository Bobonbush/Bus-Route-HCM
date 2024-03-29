from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from Path import Path



class Program :
    def __init__(self):
        self.QueryAnswer = RouteVarQuery()   
        self.StopAnwer = StopQuery()
        self.Path = Path()
        
    def run(self):
        self.QueryAnswer.load_from_json()
        self.StopAnwer.load_from_json()
        self.Path.load_from_json()
        self.Path.DebugOutput()


def main() :
    p = Program()
    p.run()



main()