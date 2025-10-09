from datetime import date
name = input("Hej, vad heter du?: ")
age = int(input(f"Hej {name} Hur gammal är du?: "))
print(f"Okej, du heter {name} och du är {age} år gammal")
years_to_100 = 100 - age
print(f"Om {years_to_100} år är du 100 år gammal!")
har_fyllt_år = input("Har du redan fyllt år i år ja/nej: ")
current_year = date.today().year
if har_fyllt_år == "ja":
    birth_year = current_year - age
else:
    birth_year = current_year - age - 1

print(f"Du är född år {birth_year}")