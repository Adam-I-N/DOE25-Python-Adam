import json


class Alarm:
    def __init__(self, alarm_type, treshold):
        self.alarm_type = alarm_type
        self.treshold = treshold

    
    def __str__(self):
        return f"{self.alarm_type} larm {self.treshold}%"
    

class AlarmManager:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm_type, treshold):
        """
        Lägger till ett nytt larm i listan.
        alarm_type: "CPU", _"Memory" eller "Disk"
        treshold: siffra mellan 0 och 100
        """

        alarm = Alarm(alarm_type, treshold)
        self.alarms.append(alarm)
        print(f"Larm för {alarm_type} satt till {treshold}%.")

    
    def list_alarms(self):
        #Skriver ut alla larm sorterad efter typ
        if not self.alarms:
            print("inga larm är konfigurerade ännu.")
            return
        
        sorted_alarms = sorted(self.alarms, key=lambda a: a.alarm_type)

        for alarm in sorted_alarms:
            print(alarm)