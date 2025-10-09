class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} accelererar. Ny hastighet: {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"{self.brand} bromsar. Ny hastighet {self.speed} km/h")

#Skapar bilar
car1 = Car("volvo", 50)
car2 = Car("BMW", 70)

#Testa metoder

car1.accelerate()
car2.accelerate()
car1.brake()
car2.brake()
car2.accelerate()