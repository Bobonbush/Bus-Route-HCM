from RouteVarQuery import RouteVarQuery
from StopQuery import StopQuery
from PathQuery import PathQuery
from geospatial import geospatial
from shapely.geometry import *
from rtree import index
from graph import Graph

class Program :
    def __init__(self):
        self.graph = Graph()
        



        
    def run(self):
        self.graph.LoadGraph()
        self.graph.AllPairShortestPath()
        self.graph.PrintTopImportant(20)

                
            

            
            
            
        

def main() :
    p = Program()
    p.run()



if __name__ == "__main__":
    main()