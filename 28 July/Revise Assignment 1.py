class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.a = 3.14 * (self.radius ** 2)
        return self.a

    def circumference(self):
        PIE = 3.14
        self.c = 2 * PIE * self.radius
        return self.c

    def display(self):
        self.area()
        self.circumference()
        print('area is ', self.a, ' circuf is ', self.c)


r = int(input("Enter radius of circle: "))
fnc = circle(r)
print("Area of circle:", (fnc.area()))
