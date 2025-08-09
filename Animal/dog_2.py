class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age  # "protected" internal attribute

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

dog_1 = Dog("Rex", 3)
print(dog_1.age)
dog_1.age = 5 
print(dog_1.age)
# dog_1.age = -1 
# print(dog_1.age)