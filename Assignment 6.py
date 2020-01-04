# Question 5:Write a code in python in which create a class named it Car which have 5 attributes such like (model, color and name etc.) and 3
# methods. And create 5 object instance from that class.
class Car():

    # instance attributes
    def __init__(self, Brand, Model, Color, Max_Speed, Fuel_type):
        self.Brand = 'Kia'
        self.Model = 'Sportage'
        self.Color = 'Red'
        self.Max_Speed = 157
        self.Fuel_type = 'Gasoline'

    # instance method
    def Sports_Car(self):
        return "{} is best sports car.".format(self.Model)

    def speed(self):
        return "{} is the maximum speed of Sportage.".format(self.Max_Speed)

    def fuel(self, fuel):
        return "{} is derived from {}".format(self.Fuel_type, fuel)


test = Car("test", 10, 15, 20, 25)
# call our instance methods
print(test.Sports_Car())
print(test.speed())
print(test.fuel("Octave."))