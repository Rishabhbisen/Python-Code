class employ:
    conpany = " google"

    def __init__(self, name, salary, subunit):  # this init method called contructor
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employe is created")

    def getdata(self):
        print(f"the name of the employ is {self.name}")
        print(f"salary of the employ is {self.salary}")
        print(f"subunit of the employ is {self.subunit}")


'''
    @staticmethod     #in this method we will not use ( self )
    def hello():
        print("good mourning")
rishabh = employ()
rishabh.hello()'''

rishabh = employ("rishabh", 100, "youtube")
rishabh.getdata()


# example
class programmer:
    conpany = "microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getdata(self):
        print(
            f"the name of the employ is {self.name} and product is {self.product}")


rishabh = programmer("rishabh", "instagram")
rishi = programmer("rishi", "github")
rishabh.getdata()
rishi.getdata()
