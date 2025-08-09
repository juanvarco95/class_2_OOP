class Dog:
    def __init__(self, name: str, age: int):
        self.name = name      # instance attribute
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says: Woof!"

# Uso
d = Dog("Rex", 3)
print(d.name)        # Rex
print(d.bark())      # Rex says: Woof!