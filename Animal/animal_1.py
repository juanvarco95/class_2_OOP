class Animal:
    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} makes a sound"

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name: str, age: str, breed: str):
        super().__init__(name, age, breed)
    
    def speak(self) -> str:
        return f"{self.name} says: Woof!"
    
class Cat(Animal):  # Dog inherits from Animal
    def __init__(self, name: str, age: str, breed: str):
        super().__init__(name, age, breed)
    
    def speak(self) -> str:
        return f"{self.name} says: Mew!"

dog_1 = Dog(name = 'Ciko',
            age = 4,
            breed = 'German Shepherd')

cat_1 = Cat(name = 'Luna',
            age = 2,
            breed = 'Siamese')

print(dog_1.speak())  
print(cat_1.speak())   
print(cat_1.speak())   
print(cat_1.speak())   