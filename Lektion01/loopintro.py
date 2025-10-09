# ett "=" betyder att det är en assignment, alltså app_is_running är like med True
app_is_running = True
# två "=" betyder att medans OM det är = True så ska något hända.
while app_is_running == True:
    print("Menyval 1")
    print("Menyval 2")
    print("Menyval 3")
    menu_choice = input("Vilken Meny?:")

    if (menu_choice == "1"):
        print("Välkommen till Meny 1")
    elif (menu_choice == "2"):
        print("Välkommen till Meny 2")
    elif (menu_choice == "3"):
        print("Välkommen till Meny 3")
    else:
        print("Avslutar")
        app_is_running = False