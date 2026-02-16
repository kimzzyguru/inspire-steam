#Name: Valentine Kimani
#Date: 13/02/2026
#Program to show for loops in python
import math

for x in range (0,360,30):
    print(math.cos (x))
for x in range (0,360,30):
    print(math.sin (x))

for x in range (0,360,30):
    print(math.tan (x))
for i in range (10,0,-1):
    print(i)
for y in range (-180,+180,30):
      print(f"sine of {y}={math.sin (y)}")
for y in range (-180,+180,30):
      print(f"cosine of {y}={math.cos (y)}")
for y in range (-180,+180,30):
     print("-------------------------------")
     print(f"angle={y}")
     print(f"sine of {y}={math.sin (y)}")
     print(f"cosine of {y}={math.cos (y)}")
        
     print(f"tangent of {y}={math.tan (y)}")