from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from PathQuery import PathQuery
from geospatial import geospatial
from Path import Path
import heapq
import queue
import csv
import json


class EdgeInfo:
    def __init__(self, Destination, path , Time, Distance):
        self._Destination = Destination
        self._path = path
        self._Time = Time
        self._Distance = Distance
        
    
    @property
    def Destination(self):
        return self._Destination
    
    @Destination.setter
    def Destination(self, value):
        self._Destination = value

    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, value):
        self._path = value

    @property
    def Time(self):
        return self._Time
    
    @Time.setter
    def Time(self, value):
        self._Time = value

    @property
    def Distance(self):
        return self._Distance
    
    @Distance.setter
    def Distance(self, value):
        self._Distance = value

class Graph :
    def __init__(self):
        self.vertices = {}
        self.routeVarQuery = RouteVarQuery()
        self.stopQuery = StopQuery()
        self.pathQuery = PathQuery()

        self.routeVarQuery.load_from_json()
        self.stopQuery.load_from_json()
        self.pathQuery.load_from_json()
        geospatial.init()

        self.RouteVarList = []

        self.cnt = []
        
    

    def LoadGraph(self):
        for routeVar in self.routeVarQuery.routeVars :
            self.RouteVarList.append((routeVar.RouteId,  routeVar.RouteVarId))
        

        for stop in self.stopQuery.stop:
            self.vertices[stop.StopId] = []
        

        for (RouteId, RouteVarId) in self.RouteVarList:
            PathList = self.pathQuery.SearchByAnything(RouteId = RouteId, RouteVarId = RouteVarId)
            StopList = self.stopQuery.SearchByAnything(RouteId = RouteId, RouteVarId = RouteVarId)
            RouteList = self.routeVarQuery.SearchByAnything(RouteId = RouteId, RouteVarId = RouteVarId)

            self.stopQuery.drawPoint(StopList)

            assert(len(PathList) == 1)
            PathList = PathList[0]
            j = 0
            TotalDistance = 0
            TotalTime = 0

            BusVelocity = RouteList[0].Distance/RouteList[0].RunningTime

            for i in range(1 , len(StopList)):  
                
                bestindex = min(j+1, len(PathList.lng)-1)
                CurrentPoint =  geospatial.TransformLatLngToXY(StopList[i].Lat , StopList[i].Lng)       # Stop I

                for index in range(j+1 , len(PathList.lng)):
                    ConsiderPoint = geospatial.TransformLatLngToXY(PathList.lat[bestindex] , PathList.lng[bestindex])
                    NextPoint = geospatial.TransformLatLngToXY(PathList.lat[index] , PathList.lng[index])

                    if(i == len(StopList)-1 and index == len(PathList.lng)-1):
                        bestindex = index

                    if geospatial.Distance(CurrentPoint, NextPoint) < geospatial.Distance(CurrentPoint, ConsiderPoint): 
                        bestindex = index
                Time = 0
                Distance = 0
                pathLng = []
                pathLat = []

                while(j < bestindex):
                    
                    pathLng.append(PathList.lng[j])
                    pathLat.append(PathList.lat[j])

                    CurrentPoint = geospatial.TransformLatLngToXY(PathList.lat[j] , PathList.lng[j])
                    NextPoint = geospatial.TransformLatLngToXY(PathList.lat[j+1] , PathList.lng[j+1])
                    Distance += geospatial.Distance(CurrentPoint, NextPoint)
                    TotalDistance += geospatial.Distance(CurrentPoint, NextPoint)
                    Time += geospatial.Distance(CurrentPoint, NextPoint) / BusVelocity
                    TotalTime += geospatial.Distance(CurrentPoint, NextPoint) / BusVelocity
                    j+= 1
                
                pathLng.append(PathList.lng[j])
                pathLat.append(PathList.lat[j])

                Time *= 60              # Seconds

                self.vertices[StopList[i-1].StopId].append(EdgeInfo(StopList[i].StopId, Path(pathLat, pathLng,RouteId,  RouteVarId), Time, Distance))
            
            self.cnt = {node : 0 for node in self.vertices}
    

    
    def Dijktra(self, start):
        Time = {node: float('inf') for node in self.vertices}
        Time[start] = 0
        
        cntPrev = {node: 0 for node in self.vertices}
        cntAfter = {node: 0 for node in self.vertices}

        pq = [(0, start)]

        cntPrev[start] = 1

        while pq :
            current_distance, current_vertex = heapq.heappop(pq)
        
            if current_distance > Time[current_vertex]:
                continue

            for edge in self.vertices[current_vertex]:
                TimeCost = current_distance + edge.Time

                if TimeCost < Time[edge.Destination]:
                    Time[edge.Destination] = TimeCost
                    heapq.heappush(pq, (TimeCost, edge.Destination))
                    cntPrev[edge.Destination] = cntPrev[current_vertex]
                elif TimeCost == Time[edge.Destination]:
                    cntPrev[edge.Destination] += cntPrev[current_vertex]
    
        listNode =[]
        for node , value in Time.items():
            listNode.append((node, value))
        listNode.sort( key=lambda x: x[1], reverse=True)

        for i in range(0 , len(listNode)):
            u = listNode[i][0]
            value = listNode[i][1]
            if(value == float('inf')):
                continue
            
            for edge in self.vertices[u]:
                v = edge.Destination 
                if(Time[u] + edge.Time == Time[v]):
                    cntAfter[u] += cntAfter[v]
            
            cntAfter[u] += 1
        

        for node , value in Time.items():
            if(value == float('inf')):
                continue
            assert(cntPrev[node] >= 1)
            assert(cntAfter[node] >= 1)
            self.cnt[node] += cntPrev[node] * cntAfter[node] 

        return Time
    
    
    

    def AllPairShortestPath(self):
        AllShortestPairFile = open('OutputCsv/AllPairShortestPath.csv', 'w' , encoding= 'utf-8')
        csvfilewriter = csv.writer(AllShortestPairFile , dialect='excel')
        
        field = ['Source (Stop Id)', 'Destination (Stop Id)', 'Time (Second)']
        csvfilewriter.writerow(field )
        

        self.cnt = {node: 0 for node in self.vertices}



        for stop, value in self.vertices.items():
            distance = self.Dijktra(stop)
            for stopDestinate, Time in distance.items():
                if(Time == float('inf') or stop == stopDestinate):
                    continue
                csvfilewriter.writerow([stop, stopDestinate, Time])
        AllShortestPairFile.close()

        cnt = self.cnt
        

        self.cnt = []
        for node, value in cnt.items():
            self.cnt.append((value, node))
        self.cnt.sort(key = lambda x: x[0], reverse=True)
    

    def PrintTopImportant(self, k ):
        k = min(k , len(self.cnt)-1)
        for i in range(k):
            print(self.cnt[i][1], self.cnt[i][0])
    

    
