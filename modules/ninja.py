import pet

class Ninja:
    def __init__( self, first_name , last_name , treats , pet_food , pet  = pet.Pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        print(f"{self.first_name.title()} and {self.pet.name.title()} are going to the park!")
        print(f"{self.first_name.title()} is bringing {self.treats}")
        self.pet.play()
    def feed(self):
        print(f"{self.first_name.title()} is feeding {self.pet.name.title()} with {self.pet_food}")
        self.pet.eat()
    def bathe(self):
        print(f"{self.first_name.title()} is going to bathe {self.pet.name.title()}!")
        self.pet.noise()

        

    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

