import random #Behövs för slumpmässiga värden

class Sensor:
    #Konstruktor: skapar ett Sensor-objekt med typ och initial nivå
    def __init__(self, type):
        self.type = type