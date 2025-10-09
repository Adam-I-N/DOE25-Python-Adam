class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Namn: {self.name} . Ålder: {self.age}"

    def greet(self, name_to_greet=None):
        if name_to_greet:
            print(f"Hej {name_to_greet}, jag heter {self.name} och är {self.age} år gammal.")
        else:
            print(f"Hej, mitt namn är {self.name} och jag är {self.age} år gammal.")

    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

p1 = Person("Calle", 31)
p2 = Person("Anna", 25)
p3 = Person("Bertil", 40)
p4 = Person("David", 20)

p1.greet()
p2.greet("Adam")
p3.greet("Eva")
p4.greet()

person_list = [p1, p2, p3, p4]

print(f"{p1.name} är {p1.age} år gammal.")

# range(x) = intervallet 0 upp till x
for i in range(len(person_list)):
    print({person_list[i]})

new_name = input(f"Skriv in nytt namn för {p1.name}: ")
p1.name = new_name
print("Nytt namn är", p1.get_name())

# Better approach
new_name = input(f"Skriv nytt namn för {p1.name}: ")
p1.change_name(new_name)
print("Nytt namn är", p1.get_name())

print(p1)

person_dict = {"Calle": p1, "Anna": p2, "Bertil": p3, "David": p4}