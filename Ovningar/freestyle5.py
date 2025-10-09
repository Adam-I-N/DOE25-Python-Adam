class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def add_points(self, x):
        self.points += x

    def has_passed(self):
        return self.points >= 50
    

#Skapa studentobjekt
student1 = Student("Adam", 30)
student2 = Student("Carlos", 40)
student3 = Student("Paul", 20)

#Lägg till poäng
student1.add_points(20)
student2.add_points(15)
student3.add_points(29)

#Lägg till studenter i en lista

students = [student1, student2, student3]

name_input = input("Skriv in ditt namn: ").strip().lower() 

found = False
for student in students:
    if student.name.lower() == name_input:
        found = True
        if student.has_passed():
            print(f"You got {student.points}. Congratulations {student.name}, you have passed!")
        else:
            print(f"You got {student.points}. Sorry {student.name} you have failed, do better")
        break

if not found:
    print("Ingen student med det namnet hittades")