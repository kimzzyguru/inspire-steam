#Name: Valentine Kimani
#Date: 23/02/2026
#Program to show inheritance in python

class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food
    def grow(self):
       self.weight *= 1.1
       print(f"The animal weighs {self.weight}kgs")

    def eat(self):
        print(f"The animal eats {self.food}")


class Dog(Animal):
    def __init__(self,species,weight,food,color,height,breed):
        super().__init__(species,weight,food)
        self.color = color
        self.breed = breed
        self.height = height
       

    def barks(self):
       print(f"The dog says woof woof")


class Horse(Animal):
    def __init__(self,species,weight,food):
        super().__init__(species,weight,food)
    
        

    def neighs(self):
        print(f"The horse says neigh neigh")

# Create a dog
dog = Dog("Dog", 20, "Dog food", "Brown", 50, "Labrador")
dog.eat()
dog.grow()
dog.barks()

# Create a Horse
horse = Horse("Horse", 150, "Hay")
horse.eat()
horse.grow()
horse.neighs()

