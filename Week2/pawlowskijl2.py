# Week 1 project for calculating a selected car's fuel economy
# given a .json list then compare it to all indices of the df
# https://github.com/Pawlowskij/MSOE_CS5980

import pandas as pd
import tabulate

from car import Car

# Function to calculate fuel economy (6)
def calculate_fuel_econ(car_selection_index, df, percent_city):
    
    selected_car = df.iloc[car_selection_index]
    car_city_mpg = selected_car["city-mpg"]
    car_hwy_mpg = selected_car["highway-mpg"]
    percent_hwy = 1-percent_city
    car_combined_mpg = (car_city_mpg*percent_city)+(car_hwy_mpg*percent_hwy)

    return car_combined_mpg

# Load in .json file as Dataframe (2)
df = pd.read_json("autos.json")
total_car_indices = len(df.index)-1


# Create a list to store all Car objects 
cars_list=[]
for i in df.index:
    car_entry = Car(
    df['aspiration'][i], df['body-style'][i], df['city-mpg'][i], df['compression-ratio'][i], df['curb-weight'][i], df['drive-wheels'][i],
    df['engine-location'][i], df['engine-size'][i], df['engine-type'][i], df['fuel-system'][i], df['fuel-type'][i], df['height'][i],
    df['highway-mpg'][i], df['horsepower'][i], df['length'][i], df['make'][i], df['normalized-losses'][i], df['num-of-cylinders'][i],
    df['num-of-doors'][i], df['peak-rpm'][i], df['price'][i], df['stroke'][i], df['symboling'][i], df['wheel-base'][i], df['width'][i])
    car_entry.car_nickname
    cars_list.append(car_entry)
    


for car in cars_list[0:5]:
    flag = True
    while flag == True:
        user_nickname=str(input("Please enter a Nickname for the car (no spaces): "))
        if len(user_nickname) >= 2 and " " not in user_nickname:
            car.car_nickname = user_nickname
            flag = False
        else:
            print("Nickname must be at least 2 characters long and include no spaces")
            
for car in cars_list[0:5]:
    print(f"Car Nickname: {car.car_nickname}, City MPG: {car.city_mpg}, Car Make: {car.make},"
          f"Car Price: {car.horsepower}")














"""

# Print small summary of DF (2)
print(df[["make","drive-wheels", "city-mpg", "highway-mpg", "horsepower"]].to_markdown())

# Print total number of cars (1)
print(f"\nTotal number of cars: {total_car_indices+1}. (Total indices: {total_car_indices}).")

# Ask for integer value within the bounds of the df (3)
flag=True
while flag==True:
    car_selection_index = input(f"\nPlease enter a valid vehicle index between 0 and {total_car_indices}: ")
    if car_selection_index.isdigit() and 0 <= int(car_selection_index) <= total_car_indices:
        car_selection_index = int(car_selection_index)
        flag=False
    else:
        print("Invalid index entered.")

# Print summary of car selection (4)
car_selection = df.iloc[car_selection_index]
print("\n\nSelected Car:\n")
print(car_selection)


# Ask for percent of city driving (5)
flag=True
while flag==True:
    try:
        percent_city = float(input("\nWhat percentage of your driving is in the city (0-100): "))
        if percent_city.is_integer() and 0 <= percent_city <=100:
            percent_city = int(percent_city)/100
            flag=False
        elif 0 <= percent_city <= 100:
            percent_city=percent_city/100
            flag=False
        else:
            print("Input must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid percentage.")   
        
# Calculate selected car's fuel econ using calculation function (6)
selected_car_total_mpg = calculate_fuel_econ(car_selection_index, df, percent_city)
selected_car_total_mpg = round(selected_car_total_mpg,2)

# Calculate avg. fuel econ of all df cars vs. selectecd car at highway percentage (7)
total_df_mpg = 0
for i in range(total_car_indices+1):
    total_df_mpg += calculate_fuel_econ(i,df,percent_city)
    # print(total_df_mpg)
    
df_total_mpg = round(total_df_mpg/(total_car_indices+1),2)


print("\nTotal DF Combined MPG: ",df_total_mpg)
print("Selected Car's Combined MPG: ",selected_car_total_mpg)

# Compare fuel econ of selected car to the average of the df's combined fuel econ at given highway driving percent
if selected_car_total_mpg > df_total_mpg:
    print(f"\nThe selected car's combined fuel economy of {selected_car_total_mpg}mpg",
             f"is better than the list's average of {df_total_mpg}mpg at",
              f"{percent_city*100}% city driving")
elif selected_car_total_mpg < df_total_mpg:
    print(f"\nThe selected car's combined fuel economy of {selected_car_total_mpg}mpg",
             f"is worse than the list's average of {df_total_mpg}mpg at",
              f"{percent_city*100}% city driving")
else:
    print(f"\nThe selected car's combined fuel economy of {selected_car_total_mpg}mpg",
             f"is the same as the list's average of {df_total_mpg}mpg at",
              f"{percent_city*100}% city driving")
              
"""