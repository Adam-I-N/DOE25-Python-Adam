from alarms import AlarmManager
from monitor import Monitor

def main():
    alarm_manager = AlarmManager()
    monitor = Monitor(alarm_manager)

    while True:
        print("\n--- Huvudmeny ---")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Avsluta")

        val = input("Välje ett alternativ: ")

        if val =="1":
            monitor.start()
        elif val =="2":
            print("\nAktuell systemstatus:\n")
            cpu = monitor.cpu_sensor.read()
            memory = monitor.memory_sensor.read()
            disk = monitor.disk_sensor.read()

            print(f"CPU användning: {cpu:.1f}%")
            print(f"Minnesanvändning: {memory:.1f}%")
            print(f"Diskanvändning: {disk:.1f}%")
            input("\nTryck valfri tangent för att gå tillbaka till huvudmeny...")

        elif val == "4":
            alarm_manager.list_alarms()
        elif val == "3":
            while True:
                print("Vilken typ av larm vill du skapa?")
                print("1. CPU | 2. Minne | 3.Diskanvändning | 4. Tillbaka till huvudmeny")

                while True:
                    typ_val = input("Välj 1, 2, 3 eller 4: ")

                    if typ_val =="4":
                        break

                    typ_map = {"1": "CPU", "2": "Minne", "3": "Diskanvändning"}     
                    if typ_val in typ_map:
                        typ = typ_map[typ_val]
                        break
                    else:
                        print("Fel: ange 1, 2, 3 eller 4.") 

                if typ_val =="4":
                    break

                while True:
                    try:
                        nivå = int(input("Tröskelvärde (1-100): "))
                        if 1 <= nivå <= 100:
                            alarm_manager.add_alarm(typ, nivå)
                            break

                        else:                    
                            print("Fel: nivå måste vara mellan 1 och 100")
                    except ValueError:
                        print("Fel: ange en siffra mellan 1-100.")
                break
        elif val == "5":
            print("Programmet avslutas. ")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()