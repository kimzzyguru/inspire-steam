#Name: Valentine Kimani
#Date: 18/02/2026
#Program to show dictionaries in python

car = {"Model": "Audi",
         "make": "Q8", 
         "colour": "cherry",
           "year": 2025}
print(car)

print(car["Model"])
print(car["year"])

student = {"Alice" : 24,
                "James" : 18, 
               "Mark" : 22, 
               "Daisy" : 19}
for key in student:
    print(key)
for val in student.values():
    print(val)