# Imports for abstract methods
from typing import Protocol

# Define abstract class Vehicle
class Vehicle(Protocol):
        def get_range(self) -> float:
            pass

# Define class Car of abstract class Vehicle with horsepower
class Car:
    def __init__(self, fuel_capactiy, miles_per_gallon, passengers, horsepower):
        self.fuel_capactiy = fuel_capactiy
        self.miles_per_gallon = miles_per_gallon
        self.passengers = passengers
        self.horsepower = horsepower

    def get_range(self) -> float:
        return self.fuel_capactiy * self.miles_per_gallon
    
# Define class Train of abstract class Vehicle with rail_type
class Train:
    def __init__(self, fuel_capactiy, miles_per_gallon, passengers, rail_type):
        self.fuel_capactiy = fuel_capactiy
        self.miles_per_gallon = miles_per_gallon
        self.passengers = passengers
        self.rail_type = rail_type

    def get_range(self) -> float:
        return self.fuel_capactiy * self.miles_per_gallon
    
# Define class Plane of abstract class Vehicle with 10% less range
class Plane:
    def __init__(self, fuel_capactiy, miles_per_gallon, passengers):
        self.fuel_capactiy = fuel_capactiy
        self.miles_per_gallon = miles_per_gallon
        self.passengers = passengers

    def get_range(self) -> float:
        return self.fuel_capactiy * self.miles_per_gallon * 0.9





# Import Vehicle abstract class and Car, Train and Plane sub-classes


# Function to check for valid numerical entry while instantiating instance of Vehicle
def get_user_input_value(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return user_input
        else:
            print("Please enter a valid whole number")
            
# Function to get string entry while instantiating instance of Vehicle, specifically for 
# the train rail_type.  Currently has no entry exception          
def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("Please enter a rail type")
    
# Function to create an instance of Car       
def create_car() -> Car:
    fuel_capactiy = int(get_user_input_value("\nwhat is the fuel capacity (gal)?: "))
    miles_per_gallon = int(get_user_input_value("what is the fuel economy (mpg)?: "))
    passengers = int(get_user_input_value("How many passengers are in the vehicle?: "))
    horsepower = int(get_user_input_value("What is the horsepower?: "))
    
    return Car(fuel_capactiy, miles_per_gallon, passengers, horsepower)

# Function to create an instance of Train   
def create_train() -> Train:
    fuel_capactiy = int(get_user_input_value("\nwhat is the fuel capacity (gal)?: "))
    miles_per_gallon = int(get_user_input_value("what is the fuel economy (mpg)?: "))
    passengers = int(get_user_input_value("How many passengers are in the vehicle?: "))
    rail_type = get_user_input("What is the rail type?: ")
    
    return Train(fuel_capactiy, miles_per_gallon, passengers, rail_type)

# Function to create an instance of Plane   
def create_plane() -> Plane:
    fuel_capactiy = int(get_user_input_value("\nwhat is the fuel capacity (gal)?: "))
    miles_per_gallon = int(get_user_input_value("what is the fuel economy (mpg)?: "))
    passengers = int(get_user_input_value("How many passengers are in the vehicle?: "))

    return Plane(fuel_capactiy, miles_per_gallon, passengers)

# Crate a list of Vehicles and append them to a list
user_garage = []

# Loop to ask the user to create a vehicle and enter the vehicle's characteristics
flag = True
while flag == True:
    user_selection = input("\nPlease enter a selection: \n1 to create a car"
                "\n2 to create a train"
                " \n3 to create a plane"
                " \n4 to quit")
    if user_selection == "1":
        car = create_car()
        user_garage.append(car)
        
    elif user_selection == "2":
        train = create_train()
        user_garage.append(train)
        
    elif user_selection == "3":
        plane = create_plane()
        user_garage.append(plane)
        
    elif user_selection == "4":
        flag = False
    
    else:
        print("Please enter a valid option.")
        
# Loop to print the vehicle's the user created and the vehicle's range          
i = 1
for vehicle in user_garage:
    vehicle_type = type(vehicle).__name__
    vehicle_range = vehicle.get_range()
    print(f"Vehicle {i}: {vehicle_type} has range {vehicle_range}")
    i+=1
    