import RouteVar 
import json
import csv




class RouteVarQuery : 
    
    field = ['Route Id', ' Route Var Id', 'Route Var Name', 'Route Var Short Name', 'Route No', 'Start Stop', 'End Stop', 'Distance', 'Outbound', 'Running Time']
    csvFile = "vars.csv"   # csv Output 
    jsonFile = "vars.json"  # json Output
    

    def __init__(self):
        self.routeVars = []
        RouteVarQuery.jsonFile = open(RouteVarQuery.jsonFile, 'w' , encoding= 'utf-8')
        RouteVarQuery.csvFile = open(RouteVarQuery.csvFile, 'w' , encoding= 'utf-8')
    def load_from_json(self):

        file = open('Json/vars.json', encoding= 'utf-8' )
        
        
        for line in file : 
            data = json.loads(line); 
            for item in data :
                routevar = RouteVar.RouteVar(item['RouteId'], item['RouteVarId'], item['RouteVarName'], item['RouteVarShortName'], item['RouteNo'], item['StartStop'], item['EndStop'], item['Distance'], item['Outbound'], item['RunningTime'])
                self.routeVars.append(routevar)
        file.close()
    
    def searchByRouteId(self , routeId):
        list = []
        for item in self.routeVars:
            if item.RouteId == routeId:
                list.append(item)
        return list
    
    def searchByRouteVarId(self , routeVarId):
        list = []
        for item in self.routeVars:
            if item.RouteVarId == routeVarId:
                list.append(item)
        return list
    
    def searchByRouteVarName(self , routeVarName):
        list = []
        for item in self.routeVars:
            if item.RouteVarName == routeVarName:
                list.append(item)
        return list
    
    def searchByRouteVarShortName(self , routeVarShortName):
        list = []
        for item in self.routeVars:
            if item.RouteVarShortName == routeVarShortName:
                list.append(item)
        return list
    
    def searchByRouteNo(self , routeNo):
        list = []
        for item in self.routeVars:
            if item.RouteNo == routeNo:
                list.append(item)
        return list
    
    def searchByStartStop(self , startStop):
        list = []
        for item in self.routeVars:
            if item.StartStop == startStop:
                list.append(item)
        return list
    
    def searchByEndStop(self , endStop):
        list = []
        for item in self.routeVars:
            if item.EndStop == endStop:
                list.append(item)
        return list
    
    def searchByDistance(self , distance):
        list = []
        for item in self.routeVars:
            if item.Distance == distance:
                list.append(item)
        return list
    
    def searchByOutbound(self , outbound):
        list = []
        for item in self.routeVars:
            if item.Outbound == outbound:
                list.append(item)
        return list
    
    def searchByRunningTime(self , runningTime):
        list = []
        for item in self.routeVars:
            if item.RunningTime == runningTime:
                list.append(item)
                
        return list
    


    def outputAsCSV(self, list):
            csvfilewriter = csv.writer(RouteVarQuery.csvFile, dialect = 'excel')
            csvfilewriter.writerow(RouteVarQuery.field)
            for item in list :
                csvfilewriter.writerow([item.RouteId, item.RouteVarId, item.RouteVarName, item.RouteVarShortName, item.RouteNo, item.StartStop, item.EndStop, item.Distance, item.Outbound, item.RunningTime])
    
    def outputAsJSON(self, list):
            for item in list:
                
                json.dump(item.properties, RouteVarQuery.jsonFile, ensure_ascii=False)
                RouteVarQuery.jsonFile.write('\n')

    def OutputDebug(self):
        for item in self.routeVars:
            print(item.RouteId)
            print(item.RouteVarId)
            print(item.RouteVarName)
            print(item.RouteVarShortName)
            print(item.RouteNo)
            print(item.StartStop)
            print(item.EndStop)
            print(item.Distance)
            print(item.Outbound)
            print(item.RunningTime)
            print("\n")
    def SearchByAnything(self, information, value):
        list = []
        for item in self.routeVars:
            if str(item.properties[information]) == str(value):
                list.append(item)
        return list

    def stopWorking(self):
        print("Program has stopped working")
        RouteVarQuery.jsonFile.close()
        RouteVarQuery.csvFile.close()
        exit()
