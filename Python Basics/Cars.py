class Car:
    """A simple attempt to represent a car."""
    def __init__(self, company, model, year):
        """Initialize attributes to describe a car."""
        self.company = company
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Initialize an attribute with a default value
        self._tank = 50

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.company} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        if self.odometer_reading < 0:
            print(f"Sorry, the odometer reading can't be negative.")
        elif self.odometer_reading == 0:
            print(f"This car has just been bought.")
        else:
            print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Print a statement of Gas Tank Capacity."""
        print(f"The gas tank capacity of {self.company}, model: {self.model} is {self._tank} liters.")

    @property
    def tank(self):
        """Property to get the tank capacity."""
        return self._tank

    @tank.setter
    def tank(self, value):
        """Setter to deny any update on the tank capacity."""
        print(f"Sorry, you can't update the tank capacity of {self.company}, model: {self.model}")


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go approximately {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, company, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(company, model, year)
        self.battery = Battery()
