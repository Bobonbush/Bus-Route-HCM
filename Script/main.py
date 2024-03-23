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
        while(True) :
            statement = input( 'Route Var (1) /  Stops (2) / quit (3) : ' )
            if(statement == '1'):
                self.VarsQuery()
                continue
            elif(statement == '2'):
                self.StopsQuery()
                continue
            elif(statement == '3'):
                break
            elif(statement == '4'):
                self.Path.DebugOutput()
                continue
            print("invalid input")
            
    
    def StopsQuery(self):
        while(True):
            ans = []
            statement = input("Enter what you want to search for:  " + " StopId(1)" + " Code(2)" + " Name(3)" + " StopType(4)" + " Zone(5)" + " Ward(6)" + " AddressNo(7)" + " Street(8)" + " SupportDisability(9)" + " Status(10)" + " Lng(11)" + " Lat(12)" + " Search(13)" + " Routes(14)" + " Exit (15)" + " : ")
            if statement == "1":
                StopId = input("Enter the StopId: ")
                ans = self.StopAnwer.SearchByAnything("StopId", StopId)
            elif statement == "2":
                Code = input("Enter the Code: ")
                ans = self.StopAnwer.SearchByAnything("Code", Code)
            elif statement == "3":
                Name = input("Enter the Name: ")
                ans = self.StopAnwer.SearchByAnything("Name", Name)
            elif statement == "4":
                StopType = input("Enter the StopType: ")
                ans = self.StopAnwer.SearchByAnything("StopType", StopType)
            elif statement == "5":
                Zone = input("Enter the Zone: ")
                ans = self.StopAnwer.SearchByAnything("Zone", Zone)
            elif statement == "6":
                Ward = input("Enter the Ward: ")
                ans = self.StopAnwer.SearchByAnything("Ward", Ward)
            elif statement == "7":
                AddressNo = input("Enter the AddressNo: ")
                ans = self.StopAnwer.SearchByAnything("AddressNo", AddressNo)
            elif statement == "8":
                Street = input("Enter the Street: ")
                ans = self.StopAnwer.SearchByAnything("Street", Street)
            elif statement == "9":
                SupportDisability = input("Enter the SupportDisability: ")
                ans = self.StopAnwer.SearchByAnything("SupportDisability", SupportDisability)
            elif statement == "10":
                Status = input("Enter the Status: ")
                ans = self.StopAnwer.SearchByAnything("Status", Status)
            elif statement == "11":
                Lng = input("Enter the Lng: ")
                ans = self.StopAnwer.SearchByAnything("Lng", Lng)
            elif statement == "12":
                Lat = input("Enter the Lat: ")
                ans = self.StopAnwer.SearchByAnything("Lat", Lat)
            elif statement == "13":
                Search = input("Enter the Search: ")
                ans = self.StopAnwer.SearchByAnything("Search", Search)
            elif statement == "14":
                Routes = input("Enter the Routes: ")
                ans = self.StopAnwer.SearchByAnything("Routes", Routes)
            elif statement == "15":
                break
            else :
                print("Invalid input")
                continue
            
            while(True):
                statement = input("Choose the Output format: " + "console(1)" + " csv(2)" + " json(3)" + " :")
                if statement == "1":
                    self.StopAnwer.OutputDebug()
                    break
                elif statement == "2":
                    self.StopAnwer.outputAsCSV(ans)
                    break
                elif statement == "3":
                    self.StopAnwer.outputAsJSON(ans)
                    break
                else :
                    print("Invalid input")
                    continue

    def VarsQuery(self):
        while(True) :
            statement = input("Enter what you want to search for: "+ "RouteId(1) " + "RouteVarId(2) " + "RouteVarName(3) " + "RouteVarShortName(4) " + "RouteNo(5) " + "StartStop(6) " + "EndStop(7) " + "Distance(8) " + "Outbound(9) " + "RunningTime(10) " "Exit(11) " + " : ")
            ans = []
            if statement == "1":
                RouteId = input("Enter the RouteId: ")
                ans = self.QueryAnswer.SearchByAnything("RouteId", RouteId)
            elif statement == "2":
                RouteVarId = input("Enter the RouteVarId: ")
                ans = self.QueryAnswer.SearchByAnything("RouteVarId", RouteVarId)
            elif statement == "3":
                RouteVarName = input("Enter the RouteVarName: ")
                ans = self.QueryAnswer.SearchByAnything("RouteVarName", RouteVarName)
            elif statement == "4":
                RouteVarShortName = input("Enter the RouteVarShortName: ")
                ans = self.QueryAnswer.SearchByAnything("RouteVarShortName", RouteVarShortName)
            elif statement == "5":
                RouteNo = input("Enter the RouteNo: ")
                ans = self.QueryAnswer.SearchByAnything("RouteNo", RouteNo)
            elif statement == "6":
                StartStop = input("Enter the StartStop: ")
                ans = self.QueryAnswer.SearchByAnything("StartStop", StartStop)
            elif statement == "7":
                EndStop = input("Enter the EndStop: ")
                ans = self.QueryAnswer.SearchByAnything("EndStop", EndStop)
            elif statement == "8":
                Distance = input("Enter the Distance: ")
                ans = self.QueryAnswer.SearchByAnything("Distance", Distance)
            elif statement == "9":
                Outbound = input("Enter the Outbound: ")
                if(Outbound.lower() == "true"):
                    Outbound = True
                else:
                    Outbound = False
                ans = self.QueryAnswer.SearchByAnything("Outbound", Outbound)
            elif statement == "10":
                RunningTime = input("Enter the RunningTime: ")
                ans = self.QueryAnswer.SearchByAnything("RunningTime", RunningTime)
            elif statement == "11":
                break
            else :
                print("Invalid input")
                continue

            while(True):
                statement = input("Choose the Output format: " + "console(1)" + " csv(2)" + " json(3)" + " :")
                if statement == "1":
                    self.QueryAnswer.OutputDebug()
                    break
                elif statement == "2":
                    self.QueryAnswer.outputAsCSV(ans)
                    break
                elif statement == "3":
                    self.QueryAnswer.outputAsJSON(ans)
                    break
                else :
                    print("Invalid input")
                    continue


def main() :
    p = Program()
    p.run()



main()