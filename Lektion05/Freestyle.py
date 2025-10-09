class Sensor:
    count = 0

    def __init__(self, name):
        self.name = name
        Sensor.count += 1
        print(f"Sensor count={Sensor.count}")
    
    def __str__(self):
        return f"Sensor {self.name}, Sensor number {Sensor.count}"
    
s1 = Sensor("CPU")
s2 = Sensor("Temp")

print(s1)
print(s2)