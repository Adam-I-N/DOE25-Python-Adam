import time
studenter = []

while True:
    print("\nVälj ett alternativ:")
    print("1. Lägg till student")
    print("2. Lista alla studenter")
    print("3. Sök student")
    print("4. Räkna genomsnittsålder")
    print("5. Avsluta")

    val = input("Skriv ditt val (1-3): ")

    if val == "1":
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
    elif val == "5":
        print("Avslutar programmet, Hej då!")
        time.sleep(2)
        break

    elif val == "3":
        namn_att_söka = input("Vad heter studenten?: ")
        hittad = False

        for student in studenter:
            if student["namn"].lower() == namn_att_söka.lower():
                print(f"Hittade {student['namn']}, {student['ålder']} år")
                hittad = True
                break

        if not hittad:
            print("Studenten finns inte i registret.")
            time.sleep(2)


    elif val == "4":
        if len(studenter) == 0:
            print("Det finns inga studenter att räkna på.")
        else:
            total_ålder = 0
            for student in studenter:
                total_ålder += student['ålder']
            genomsnitt = total_ålder / len(studenter)
            print(f"Genomsnittsåldern är: {genomsnitt:.1f} år")
            time.sleep(2)

    else:
        print("Ogiltigt val. Välj 1,2,3,4 eller 5. ")
