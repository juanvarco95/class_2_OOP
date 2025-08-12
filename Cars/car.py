class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        return f"{self.brand} {self.model} engine started."

class ElectricCar(Car):
    def __init__(self, brand: str, model: str, year: int, battery_size: int):
        super().__init__(brand, model, year)  # call Car.__init__
        self.battery_size = battery_size

    def start_engine(self) -> str:
        return f"{self.brand} {self.model} is silent... ready to go!"

class GasolineCar(Car):
    def __init__(self, brand: str, model: str, year: int, tank_capacity: float):
        super().__init__(brand, model, year)
        self.tank_capacity = tank_capacity

    def start_engine(self) -> str:
        return f"{self.brand} {self.model} engine roars to life!"

cars = [
    ElectricCar("Tesla", "Model 3", 2024, 75),
    GasolineCar("Toyota", "Corolla", 2023, 50)
]
for c in cars:
    print(c.start_engine())
