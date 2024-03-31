from shapely.geometry import *


# Creating a Point
point = Point(0, 0)
print("Point:", point)

# Creating a LineString
line = LineString([(0, 0), (1, 1), (2, 2)])
print("LineString:", line)

# Creating a Polygon
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print("Polygon:", polygon)

# Accessing attributes of geometric objects
print("Point coordinates:", point.x, point.y)
print("LineString length:", line.length)
print("Polygon area:", polygon.area)
print("Polygon centroid:", polygon.centroid)
print("Polygon bounding box:", polygon.bounds)