class Pet:
    def __init__(self,name,tricks):
        self.name = name
        self.tricks = tricks
        self.health = 100  #Note that assignment instructions state not to include health and energy as parameters in init method
        self.energy = 100
    def sleep(self):
        print(f"{self.name.title()} is {self.tricks}! Woo")
        self.energy +=25
    def eat (self):
        print(f"Yummy! {self.name.title()} is eating a great meal!")
        self.energy +=5
        self.health +=10
    def play(self):
        print(f"Watch out! {self.name.title()} is playing in the park.")
        self.health +=5
    def noise(self):
        print(f"*audible* *{self.name.title()} is making noise*")

class Dog(Pet):
    def __init__(self,name,tricks):
        super().__init__(name,tricks)
    def noise(self):
        super().noise()
        print("*Woof* *Woof*")

class Cat(Pet):
    def __init__(self,name,tricks):
        super().__init__(name,tricks)
    def noise(self):
        super().noise()
        print("*Miau* *Miau*")

