# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    def __init__(self, fuel, color, terrain):
        self.fuel = fuel
        self.color = color
        self.terrain = terrain

    def __str__(self):
        return f'{self.fuel}, {self.color}, best used in {self.terrain}'


class FlightVehicle(Vehicle):
    def __init__(self, fuel, color, terrain, maxAltitude):
        super().__init__(fuel, color, terrain)
        self.maxAltitude = maxAltitude

    def __str__(self):
        return super().__str__() + f', its max altitude is {self.maxAltitude}'


class Airplane(FlightVehicle):
    def __init__(self, fuel, color, terrain, maxAltitude, airport):
        super().__init__(fuel, color, terrain, maxAltitude)
        self.airport = airport

    def __str__(self):
        return super().__str__() + f' and its flying out of {self.airport}'


Boeing727 = Airplane("jetfuel", "white and red", "air",
                     "pretty dang high", "La Guardia, NYC")

print('Boeing 727:', Boeing727)


class GroundVehicle(Vehicle):
    def __init__(self, fuel, color, terrain, maxMPH):
        super().__init__(fuel, color, terrain)
        self.maxMPH = maxMPH

    def __str__(self):
        return super().__str__() + f', can go up to {self.maxMPH} miles per hour!'


class Car(GroundVehicle):
    def __init__(self, fuel, color, terrain, maxMPH, make):
        super().__init__(fuel, color, terrain, maxMPH)
        self.make = make

    def __str__(self):
        return super().__str__() + f' It is made by {self.make}'


class Motorcycle(GroundVehicle):
    def __init__(self, fuel, color, terrain, maxMPH, deathTrap):
        super().__init__(fuel, color, terrain, maxMPH)
        self.deathTrap = deathTrap

    def __str__(self):
        return super().__str__() + f' is it a deathtrap? {self.deathTrap}'


TeslaModelS = Car("electricity", "gray", "pavement", 155, "Tesla")

print('Tesla Model S:', TeslaModelS)

Ducati = Motorcycle("gas", "red", "pavement",  202, "absolutely")
print('Ducati Panigale R:', Ducati)
