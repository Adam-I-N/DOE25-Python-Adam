import time
from sensors import Sensor
from alarms import AlarmManager

class Monitor:
    def __init__(self, alarm_manager: AlarmManager):
        # Tar emot AlarmManager för att kunna kolla larm
        self.alarm_manager = alarm_manager
        self.active = False

        # Här skapas sensorer
        self.cpu_sensor = Sensor("CPU", use_real_data=True)
        self.memory_sensor = Sensor("Minne", use_real_data=True)
        self.disk_sensor = Sensor("Diskanvändning", use_real_data=True)

    def start(self):
        #Startar övervakningen
        self.active = True
        print("Övervakning startad. Tryck Ctrl+C för att avsluta. \n")

        try:
            while self.active:
                cpu = self.cpu_sensor.read()
                memory = self.memory_sensor.read()
                disk = self.disk_sensor.read()

                print(f"CPU: {cpu:.1f}% | Minne: {memory:.1f}% | Diskanvändning: {disk:.1f}%")

                #Kolla larm
                self.check_alarms(cpu, memory, disk)

                time.sleep(2)

        except KeyboardInterrupt:
            self.active = False
            print("\nÖvervakning stoppades av användaren.\n")

    def check_alarms(self, cpu, memory, disk):
        #Kontroll om larm ska triggas
        for alarm in self.alarm_manager.alarms:
            if alarm.alarm_type == "CPU" and cpu > alarm.treshold:
                print(f"*** VARNING: CPU-användning överstiger {alarm.treshold:.1f}% ***")
            elif alarm.alarm_type == "Minne" and memory > alarm.treshold:
                print(f"*** VARNING: Minnesanvändning överstiger {alarm.treshold:.1f}% ***")
            elif alarm.alarm_type == "Diskanvändning" and disk > alarm.treshold:
                print(f"*** VARNING: Diskanvändning överstiger {alarm.treshold:.1f}% ***")