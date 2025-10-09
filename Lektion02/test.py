print("Startar")
def print_menu(menu_choice_number, message_string):
    choice_is_valid = menu_choice_number in [1, 2, 3, 4] #Vi kontrollerar att valet är giltigt
    if not choice_is_valid:
        print("Invalid choice")
        return # Avslutar funktionen om valet är ogiltigt.
    print(f"You selected option.{menu_choice_number}. {message_string}")



menu_is_running = True

volume = 5

while menu_is_running:
    menu_choice = input("Enter a choice (1-3. 4 to quit): ")

    if menu_choice == '1':
        print_menu(int(menu_choice), "TV Settings")


    elif menu_choice == '2':
        print_menu(int(menu_choice), "Choose channel")


    elif menu_choice == '3':
        valid_volume = False
        while not valid_volume:
            print(f"Volume is {volume}")
            print_menu(int(menu_choice), "Change Volume")
            new_volume = int(input("Set volume 0-100: "))
            if 0 <= new_volume <= 100:
                volume = new_volume
                print(f"Volume set to {volume}")
                valid_volume = True
            else:
                print("Volume must be between 0-100")
                continue


    elif menu_choice == '4':
        print_menu(int(menu_choice), "Turning of TV")
        menu_is_running = False
        break
    else:
        print("Invalid choice. ")

print("Program exited. ")