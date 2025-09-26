import time

# [0, 1, 2]. I koden är 3 alltså hur många siffor som räknas. Den börjar på noll och slutar då på 2.
for j in range(3):
    print(j)

#[5, 4, 3, 2, 1]. 
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Klar")