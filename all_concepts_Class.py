# Encapsulation
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self.__speed -= 10

    def get_speed(self):
        return self.__speed

# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.__battery_capacity = battery_capacity

    def get_battery_capacity(self):
        return self.__battery_capacity

# Polymorphism
class GasolineCar(Car):
    def __init__(self, make, model, year, fuel_capacity):
        super().__init__(make, model, year)
        self.__fuel_capacity = fuel_capacity

    def get_fuel_capacity(self):
        return self.__fuel_capacity

    # Overriding accelerate method to demonstrate polymorphism
    def accelerate(self):
        self.__speed += 5

# Abstraction
class Vehicle:
    def start_engine(self):
        pass

class ElectricVehicle(Vehicle):
    def start_engine(self):
        print("Starting electric engine")

class GasolineVehicle(Vehicle):
    def start_engine(self):
        print("Starting gasoline engine")

# Using the classes
my_electric_car = ElectricCar("Tesla", "Model S", 2023, 75)
my_gasoline_car = GasolineCar("Toyota", "Camry", 2023, 15)

print("Electric Car:")
print(f"Make: {my_electric_car.get_make()}")
print(f"Model: {my_electric_car.get_model()}")
print(f"Year: {my_electric_car.get_year()}")
print(f"Battery Capacity: {my_electric_car.get_battery_capacity()} kWh")

print("\nGasoline Car:")
print(f"Make: {my_gasoline_car.get_make()}")
print(f"Model: {my_gasoline_car.get_model()}")
print(f"Year: {my_gasoline_car.get_year()}")
print(f"Fuel Capacity: {my_gasoline_car.get_fuel_capacity()} gallons")

my_electric_car.accelerate()
my_gasoline_car.accelerate()
print("\nCurrent Speed of Electric Car:", my_electric_car.get_speed())
print("Current Speed of Gasoline Car:", my_gasoline_car.get_speed())

electric_vehicle = ElectricVehicle()
gasoline_vehicle = GasolineVehicle()

print("\nAbstract Class Example:")
electric_vehicle.start_engine()
gasoline_vehicle.start_engine()
