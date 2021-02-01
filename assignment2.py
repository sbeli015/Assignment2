#class Assignment2:
#Task 1 Constructor
class AgeClass():
    num = 1

    def __init__(self,i):
        self.num = i

    def age(self):
        print(self.num)

#Task 2 Welcome

class WelcomeClass():
    name = "polp"
    year = 1886

    def __init__(self, i, j):
        self.name = i
        self.year = j

    def sayWelcome(self):
        print("Welcome to the assignment, " + self.name +
        "! Haven't seen you for" + self.year + "YYYY years!")
