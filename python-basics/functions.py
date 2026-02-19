#Name: Valentine Kimani
#Date: 19/02/2026
#Program to cook an egg

def cook_egg():
    oil= "20ml"
    pan = True
    moto = True
    eggs= 2

    print(f"The pan is {pan}, and the fire is {moto}, add {oil} amount of oil and cook {eggs} eggs")
print("Here is statement 1")
print("Here is statement 2")
cook_egg()
print("Here is statement 3")

#ride fare creating a function
def create_fare(route, distance,is_rush_hour):
    fare= 5*distance
    if is_rush_hour == True:
        fare= fare*1.5
    print(f"Your fare to {route} is {fare}")
    return fare

rush_hour = True
returned_fare = create_fare("Juja_Allsops",7, rush_hour)
print(f"The returned fare is:
     {returned_fare}")

create_fare("Juja_Allsops",7, rush_hour)

#passing a list as a parameter
def write_all_interest(interests):
    for interest in interests:
        print(f"I am interested in {interest}")
all_interests = ["coding", "sports", "music", "art"]

write_all_interest(all_interests)
