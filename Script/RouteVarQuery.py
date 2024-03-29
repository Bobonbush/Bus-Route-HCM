import RouteVar 
import json
import csv




class RouteVarQuery : 
    
    field = ['Route Id', ' Route Var Id', 'Route Var Name', 'Route Var Short Name', 'Route No', 'Start Stop', 'End Stop', 'Distance', 'Outbound', 'Running Time']
    
    
    csvFile = "OutputCsv/vars.csv"   # csv Output 
    jsonFile = "OutputJson/vars.json"
    

    def __init__(self):
        self.routeVars = []
        RouteVarQuery.csvFile = open(RouteVarQuery.csvFile, 'w' , newline = '', encoding= 'utf-8')
        RouteVarQuery.jsonFile = open(RouteVarQuery.jsonFile, 'w' , encoding= 'utf-8')
    
    def load_from_json(self):

        file = open('Json/vars.json', encoding= 'utf-8' )
        
        
        for line in file : 
            data = json.loads(line); 
            for item in data :
                routevar = RouteVar.RouteVar(item['RouteId'], item['RouteVarId'], item['RouteVarName'], item['RouteVarShortName'], item['RouteNo'], item['StartStop'], item['EndStop'], item['Distance'], item['Outbound'], item['RunningTime'])
                self.routeVars.append(routevar)
        file.close()

    def SearchByAnything(self, **kwargs):
        list = []
        for item in self.routeVars:
            ok = True    
            for key,value in kwargs.items():
                if str(item.properties[key]).lower() == str(value).lower():
                    continue
                ok = False
                
            if(ok == True):
                list.append(item)
        return list
    


    def outputAsCSV(self, list):
        csvfilewriter = csv.writer(RouteVarQuery.csvFile , dialect='excel')
        csvfilewriter.writerow(RouteVarQuery.field )
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


    
    


    def stopWorking(self):
        print("Program has stopped working")
        RouteVarQuery.jsonFile.close()
        RouteVarQuery.csvFile.close()
        exit()
