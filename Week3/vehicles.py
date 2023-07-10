# Imports for abstract methods
from abc import ABC, abstractmethod

# Define abstract class Vehicle
class Vehicle(ABC):

    def __init__(self, fuel_capactiy, miles_per_gallon, passengers):
        self.fuel_capactiy = fuel_capactiy
        self.miles_per_gallon = miles_per_gallon
        self.passengers = passengers

    @abstractmethod
    def get_range(self):
        pass

# Define class Car of abstract class Vehicle with horsepower
class Car(Vehicle):
    def __init__(self, fuel_capactiy, miles_per_gallon, passengers, horsepower):
        super().__init__(fuel_capactiy, miles_per_gallon, passengers)
        self.horsepower = horsepower

    def get_range(self):
        return self.fuel_capactiy * self.miles_per_gallon
    
# Define class Train of abstract class Vehicle with rail_type
class Train(Vehicle):
    def __init__(self, fuel_capactiy, miles_per_gallon, passengers, rail_type):
        super().__init__(fuel_capactiy, miles_per_gallon, passengers)
        self.rail_type = rail_type

    def get_range(self):
        return self.fuel_capactiy * self.miles_per_gallon
    
# Define class Plane of abstract class Vehicle with 10% less range
class Plane(Vehicle):
    def __init__(self, fuel_capactiy, miles_per_gallon, passengers):
        super().__init__(fuel_capactiy, miles_per_gallon, passengers)
    
    def get_range(self):
        return self.fuel_capactiy * self.miles_per_gallon * 0.9

