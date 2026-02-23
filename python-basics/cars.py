#Name: Valentine Kimani
#Date: 23/02/2026
#Program to show classes in python

class Car():
    # attributes of the car
    def __init__(self,model,make,color,year):
        self.model =model
        self.make =make
        self.color =color
        self.year =year
    #print car detail
    def print_details(self,model,make,color,year):
        print(f"{make} {model} of color {color} was manufactured in the year {year}")
 

 #instantiate a class object
my_car = Car("Atenza","Mazda","Red","2022")
dads_car = Car("Land Cruiser","Toyota","Black","2025")

my_car.print_details("Atenza","Mazda","Red","2022")


   

