# Week 2 project for creating a list of car objects, giving the first
# five instances a nickname, calculating the min, max and average price
# of the cars in the list and  plotting price vs horsepower.
# https://github.com/Pawlowskij/MSOE_CS5980

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from car import Car

# Load in .json file as Dataframe (3)
df = pd.read_json("autos.json")


# Create a list to store all Car objects and instantiate them in this list (4) 
cars_list=[]
for i in df.index:
    car_entry = Car(
    df['aspiration'][i], df['body-style'][i], df['city-mpg'][i], df['compression-ratio'][i], df['curb-weight'][i], df['drive-wheels'][i],
    df['engine-location'][i], df['engine-size'][i], df['engine-type'][i], df['fuel-system'][i], df['fuel-type'][i], df['height'][i],
    df['highway-mpg'][i], df['horsepower'][i], df['length'][i], df['make'][i], df['normalized-losses'][i], df['num-of-cylinders'][i],
    df['num-of-doors'][i], df['peak-rpm'][i], df['price'][i], df['stroke'][i], df['symboling'][i], df['wheel-base'][i], df['width'][i])
    car_entry.car_nickname
    cars_list.append(car_entry)
    

# Ask the user for a nickname with 2 characters or more (5)
for car in cars_list[0:5]:
    flag = True
    while flag == True:
        user_nickname=str(input("Please enter a Nickname for the car (no spaces): "))
        if len(user_nickname) >= 2 and " " not in user_nickname:
            car.car_nickname = user_nickname
            flag = False
        else:
            print("\nNickname must be at least 2 characters long and include no spaces.")   
print("\n")


# Print first 5 car objects of car list (6)
for car in cars_list[0:5]:
    print(f"Car Nickname: {car.car_nickname}, City MPG: {car.city_mpg}, Car Make: {car.make}, "
          f"Car Price: {car.price}")


# Calculate the average, min and max price of all cars (7)
car_cost=0
car_cost_max = float("-inf")
car_cost_min = float("inf")

cars_with_price = len(cars_list)
for car in cars_list:
    if pd.isnull(car.price):
        cars_with_price -= 1

    else:
        car_cost += car.price

        if car.price > car_cost_max:
            car_cost_max = car.price
            
        if car.price < car_cost_min:
            car_cost_min = car.price
            
average_car_price = car_cost/cars_with_price
average_car_price = round(average_car_price,2)

print(f"\n{cars_with_price} of {len(cars_list)} cars have prices.")        
print(f"Min price of total cars with price values: {car_cost_min}")
print(f"Max price of total cars with price values {car_cost_max}")
print(f"Average price of total cars with price values: {average_car_price}.") 


# Graph price vs horsepower (8)
y = np.array(df["price"])
x = np.array(df["horsepower"])
plt.scatter(x, y)
plt.xlabel("price")
plt.ylabel("horsepower")
plt.title("price vs. horsepower")
plt.show()
