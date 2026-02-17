#Name: Valentine Kimani
#Date: 16/02/2026
#Program to calculate geometric progression

# Calculating sine cosine and tangent of angles from -180 to +180 with a step of 30 degrees in tabular form

import math

for y in range (-180,+180,30):
      print(f"sine of {y}={math.sin (y)}")
for y in range (-180,+180,30):
      print(f"cosine of {y}={math.cos (y)}")
for y in range (-180,+180,30):
      print(f"tangent of {y}={math.tan (y)}")
print("----------------------------------")
print("Angle(y)   |   Sine(y)        |  Cosine(y)               |   Tangent(y)")
for y in range (-180,+180,30):
      print(f"|{y}|  {math.sin (y)}|     {math.cos (y)}|     {math.tan (y)}")
      print(f" {y} \t {math.sin (y)} \t {math.cos (y)} \t {math.tan (y)}")
     
        
