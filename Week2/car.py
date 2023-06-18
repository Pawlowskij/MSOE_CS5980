# Create car class that stores all information about a car with a nickname set to None (2)
class Car():
    
    def __init__(self, aspiration, body_style, city_mpg, compression_ratio, curb_weight, drive_wheels,
                 engine_location, engine_size, engine_type, fuel_system, fuel_type, height,
                 highway_mpg, horsepower, length, make, normalized_losses, num_of_cylinders,
                 num_of_doors, peak_rpm, price, stroke, symboling, wheel_base, width):
    
        self.aspiration = aspiration
        self.body_style = body_style
        self.city_mpg = city_mpg
        self.compression_ratio = compression_ratio
        self.curb_weight = curb_weight
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.engine_size = engine_size
        self.engine_type = engine_type
        self.fuel_system = fuel_system
        self.fuel_type = fuel_type
        self.height = height
        self.highway_mpg = highway_mpg
        self.horsepower = horsepower
        self.length = length
        self.make = make
        self.normalized_losses = normalized_losses
        self.num_of_cylinders = num_of_cylinders
        self.num_of_doors = num_of_doors
        self.peak_rpm = peak_rpm
        self.price = price
        self.stroke = stroke
        self.symboling = symboling
        self.wheel_base = wheel_base
        self.width = width
        self.car_nickname = None
    
