import time
studenter = []

while True:
    print("\nVälj ett alternativ:")
    print("1. Lägg till student")
    print("2. Lista alla studenter")
    print("3. Avsluta")

    val = input("Skriv ditt val (1-3): ")

    if val == "1":
        time.sleep(1)
        namn = input("Skriv in studentens namn: ")
        ålder = int(input("Skriv in studentens ålder: "))
    
        student = {
            "namn": namn,
            "ålder": ålder
        }

        studenter.append(student)
        print(f"{namn} har lagts till.")

    elif val == "2":
        if len(studenter) == 0:
            print("Inga studenter har lagts till ännu.")
        else:
            print("\nLista över studenter: ")
            for student in studenter:
                print(f"Namn: {student['namn']}, Ålder: {student['ålder']}")
    elif val == "3":
        print("Avslutar programmet, Hej då!")
        time.sleep(2)
        break
    
    else:
        print("Ogiltigt val. Välj 1,2 eller 3. ")
