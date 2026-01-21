import math
x1 = int(input("Enter the value of x1 : "))
x2 = int(input("Enter the value of x2 : "))
y1 = int(input("Enter the value of y1 : "))
y2 = int(input("Enter the value of y2 : "))
distance_between_two_points = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Distance between two points : ",distance_between_two_points)