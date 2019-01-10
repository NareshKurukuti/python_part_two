class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name  = name

mydog = Dog(breed = "Lab", name = "Sammy")
# mydog = Dog("Lab","Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)


# Find the Area of the Circle

class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
# print('\nCircle Radius :')
# print(myc.radius)
# print('\nCircle Area with Radius of 3 :')
# print(myc.area())
# myc.set_radius(999)
print('\nCircle Area by set the radius is 999 with help of set_radius() :')
print(myc.area())