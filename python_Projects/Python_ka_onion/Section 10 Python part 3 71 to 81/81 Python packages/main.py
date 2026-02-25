#Module?
#What is Module?
#Why we need it?
# How does it work?

from west  import america,germany,italy
from east import china


def car_assembly():
    print(f"{america.body()},{china.chasis()},{germany.engine()} and {italy.tyer()} makes a car")
    




car_assembly()