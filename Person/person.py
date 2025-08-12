class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def teach(self) -> str:
        return f"{self.name} is teaching {self.subject}."

class Student(Person):
    def __init__(self, name: str, age: int, grade_level: str):
        super().__init__(name, age)
        self.grade_level = grade_level

    def study(self) -> str:
        return f"{self.name} is studying in grade {self.grade_level}."

t = Teacher("Alice", 40, "Math")
s = Student("Bob", 20, "12th")
print(t.teach())
print(s.study())
