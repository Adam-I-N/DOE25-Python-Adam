class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
       
    def brake(self):
        if (self.speed <= 0):
            return 0
        else:
            self.speed -= 10
            return self.speed
        
car1 = Car("Audi", 100)
car2 = Car("Volvo", 50)
        
def change_speed(car_obj, should_accelerate):

    if should_accelerate == True:
        new_speed = car_obj.accelerate()
    else:
        if car_obj.speed <= 0:
            new_speed = 0
            print("Car's speed is already 0, can't brake.")
        else:
            new_speed = car_obj.brake()
            print(f"Ny hastighet för {car_obj.brand} is {new_speed}")
    print(new_speed)


        
accelerate = input("Do you want to accelerate or brake? a/b: ")

if accelerate == "a": # User wants to accelerate
    change_speed(car1, True)
else:  # User wants to brake
    change_speed(car1, False)
