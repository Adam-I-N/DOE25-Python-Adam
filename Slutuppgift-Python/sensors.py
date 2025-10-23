import random
import psutil

class Sensor: #Created Sensor class
    def __init__(self, type_of_usage, use_real_data=False):
        self.type_of_usage = type_of_usage
        self.use_real_data = use_real_data

    def read(self):
        if self.use_real_data:
            if self.type_of_usage == "CPU":
                return psutil.cpu_percent()
            
            elif self.type_of_usage =="Memory":
                return psutil.virtual_memory().percent
            
            elif self.type_of_usage == "Disk usage":
                return psutil.disk_usage("/").percent
        
        else:
            return random.randint(0,100)