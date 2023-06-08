import pandas as pd

#Load in .json file as Dataframe
df = pd.read_json("autos.json")

#Function to calculate fuel economy

def CalcFuelEcon(carSelection, df, percentCity):
    pass
    
#Print small summary of DF
print(df[["make","drive-wheels", "city-mpg", "highway-mpg"]].to_markdown())

#Print total cars in DF
totalCars = len(df.index)-1
print(f'\nTotal number of cars: {totalCars}')

#Ask for integer value within the bounds of the DF
while True:
    carSelection = input("\nPlease select a vehicle index: ")
    
    if carSelection.isdigit() and int(carSelection) <= totalCars:
        carSelection = int(carSelection)
        break

#Print all details of input car index    
print(df.iloc[carSelection])



