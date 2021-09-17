import sys
sys.path.append('./modules')
import pet
import ninja



Bruno = pet.Dog("Bruno", "jumping")
Mario = ninja.Ninja("Mario", "Jimenez", "a ball", "kibbles", Bruno)
Missy = pet.Cat("Missy", "food hunting")
Ana = ninja.Ninja("Ana","Abarca","wool","tuna",Missy)
Mario.feed()
Mario.walk()
Mario.bathe()
Ana.bathe()