if __name__ == "__main__":
    # Write your solution here

    # Class Vehicle: A basic description of any car functions
    class Vehicle:
        # __init__: Initializing shared data
        def __init__(self, manufactured: str, stamp: str, model: str, number_car: str,
                     colour: str, number_of_seats: int) -> None:
            self.manufactured = manufactured
            self.stamp = stamp
            self.model = model
            self.number_car = number_car
            self.colour = colour
            self.number_of_seats = number_of_seats

        # Fill in or change the manufactured variable
        def fill_in_the_manufactured_variable(self, manufactured: str) -> None:
            self.manufactured = manufactured

        # Fill in or change the stamp variable
        def fill_in_the_stamp_variable(self, stamp: str) -> None:
            self.stamp = stamp

        # Fill in or change the model variable
        def fill_in_the_model_variable(self, model: str) -> None:
            self.model = model

        # Fill in or change the number_car variable
        def fill_in_the_number_car_variable(self, number_car: str) -> None:
            self.number_car = number_car

        # Fill in or change the colour variable
        def fill_in_the_colour_variable(self, colour: str) -> None:
            self.colour = colour

        # Fill in or change the number_of_seats variable
        def fill_in_the_number_of_seats_variable(self, number_of_seats: int) -> None:
            self.number_of_seats = number_of_seats

        # Basic description
        def __str__(self) -> str:
            return f"Car model is {self.model}, stamp is {self.stamp}, manufactured is {self.manufactured}."

        # Output of all variables
        def __repr__(self) -> str:
            return f"manufactured is {self.manufactured}, " \
                   f"stamp is {self.stamp}, " \
                   f"model is {self.model}, " \
                   f"number car is {self.number_car}, " \
                   f"colour is {self.colour}, " \
                   f"number of seats are {self.number_of_seats}."

        # Output of information about appearance and condition of the car
        def the_details_in_car(self) -> str:
            return f"Car has: {self.colour} color, {self.number_of_seats} seats."


    # class Passenger_car: Description of passenger cars functions
    class Passenger_car(Vehicle):
        # Extended initializing for passenger cars
        def __init__(self, manufactured: str, stamp: str, model: str, number_car: str,
                     colour: str, number_of_seats: int, trunk_size_in_volume: int) -> None:
            super().__init__(manufactured, stamp, model, number_car, colour, number_of_seats)
            self.trunk_size_in_volume = trunk_size_in_volume

        # Output of all variables (reloading the magic method because + var "trunk_size_in_volume")
        def __repr__(self) -> str:
            return f"manufactured is {self.manufactured}, " \
                   f"stamp is {self.stamp}, " \
                   f"model is {self.model}, " \
                   f"number car is {self.number_car}, " \
                   f"colour is {self.colour}, " \
                   f"number of seats are {self.number_of_seats}, " \
                   f"trunk size in volume = {self.trunk_size_in_volume}."

        # Output of information about appearance and condition of the passenger car
        def the_details_in_car(self) -> str:
            return f"Car has: {self.colour} color, {self.number_of_seats} seats and " \
                   f"{self.trunk_size_in_volume} trunk size in volume (in centimeters^3)."


    # class Cargo_truck: Description of cargo trucks functions
    class Cargo_truck(Vehicle):
        # Extended initializing for cargo trucks
        def __init__(self, manufactured: str, stamp: str, model: str, number_car: str,
                     colour: str, number_of_seats: int, container_size_in_volume: int) -> None:
            super().__init__(manufactured, stamp, model, number_car, colour, number_of_seats)
            self.container_size_in_volume = container_size_in_volume

        # Output of all variables (reloading the magic method because + var "container_size_in_volume")
        def __repr__(self) -> str:
            return f"manufactured is {self.manufactured}, " \
                   f"stamp is {self.stamp}, " \
                   f"model is {self.model}, " \
                   f"number car is {self.number_car}, " \
                   f"colour is {self.colour}, " \
                   f"number of seats are {self.number_of_seats}, " \
                   f"container size in volume = {self.container_size_in_volume}."

        # Output of information about appearance and condition of the cargo truck
        def the_details_in_car(self) -> str:
            return f"Car has: {self.colour} color, {self.number_of_seats} seats and " \
                   f"{self.container_size_in_volume} container size in volume (in centimeters^3)."

    pass
