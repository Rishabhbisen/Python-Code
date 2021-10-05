class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"the value of {self.number} squar is {self.number**2}")

    def cube(self):
        print(f"the value of {self.number} cube  is {self.number**3}")

    def squareRoot(self):
        print(f"the value of {self.number} squar is {self.number**0.5}")

    @staticmethod
    def greet():
        print("****welcome to new programming world****")


a = Calculator(9)
a.greet()
a.square()
a.cube()
a.squareRoot()

print("************")


# secod example
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"train name is {self.name}")
        print(f"the seats are availabe in train {self.seats}")

    def getfare(self):
        print(f" the price of the tilat is rs {self.fare}")

    def booktikat(self):
        if(self.seats > 0):
            print(
                f"your tikat bokked susefully and seat nomber is {self.seats}")
            self.seats = self.seats-1
        else:
            print(" train is full try for tatkal")


rajdhani = Train("rajdhani sf speacle", 90, 2)
rajdhani.getstatus()
rajdhani.booktikat()
rajdhani.booktikat()
rajdhani.getstatus()
rajdhani.getfare()
