class Dog:
    # species = "Canis familiaris"  # class attribute shared by all instances
    
    def __init__(self, name: str, age: int, specie: str):
        self.name = name      # instance attribute
        self.age = age
        self.specie = specie
        
    def bark(self) -> str:
        return f"{self.name} says: Woof!"

dog_1 = Dog(name = "Rex", 
            age = 3, 
            specie = "German Shepard")
print(dog_1.name)  
print(dog_1.age)  
print(dog_1.bark())      