import json
from datetime import datetime

current_time = datetime.now()
time_stamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
with open("shelter.json", "r") as file:
    data = json.load(file)

def print_log():
    '''This function prints out the shelter's records.'''
    skip_items = ["radio_working"]
    for key, value in data.items():
        if key in skip_items:
            continue
        print(f"{key} : {value}")
    if data["radio_working"] == True:
        print("Radio : Working")
    elif data["radio_working"] == False:
        print("Radio : Not Working")
    
def new_str(userin):
    '''This function replaces a chosen string in the log with user input.'''
    old = data[userin]
    newstr = input("Enter the new value: ")
    while newstr.isdigit() == True or newstr.strip() == "":
        print("Invalid")
        newstr = input("Enter the new value: ")
    data[userin] = newstr
    with open("shelter_change.txt", "a") as file:
        file.write(f"{time_stamp}| {userin} changed from {old} to {newstr}\n")

def new_num(userin):
    '''This function replaces a chosen number in the log with user input.'''
    old = data[userin]
    num = input("Enter the new value: ")
    while num.isdigit() == False or num.strip() == "" or int(num) < 0:
        print("Invalid")
        num = input("Enter the new value: ")
    data[userin] = num
    with open("shelter_change.txt", "a") as file:
        file.write(f"{time_stamp}| {userin} changed from {old} to {num}\n")
        
def new_num_under_100(userin):
    '''This function replaces a chosen number in the log with user input.'''
    old = data[userin]
    num = input("Enter the new value: ")
    while num.isdigit() == False or num.strip() == "" or int(num) <0 or int(num) >100:
        print("Invalid")
        num = input("Enter the new value: ")
    data[userin] = num 
    with open("shelter_change.txt", "a") as file:
        file.write(f"{time_stamp}| {userin} changed from {old} to {num}\n")

def new_bool(userin):
    '''This function replaces a boolean chosen by the user.'''
    old = data[userin]
    x = input("Enter the new value (y/n): ")
    if x.lower == "y":
        data["radio_working"] = True
    elif x.lower == "n":
        data["radio_working"] = False
    else:
        print("Invalid.")
    
    if data["radio_working"] == True:
        new = "Working"
    else:
        new = "Not working"
    with open("shelter_change.txt", "a") as file:
        file.write(f"{time_stamp}| Radio changed from {old} to {new}\n")

def change_value():
    '''This function gets what input from the user to see what will be changed'''
    userin = input("Enter the value you'd like to change: ")
    while userin.isdigit == True or userin.strip() == "":
        print("Invalid. (Enter the name of the value. Check underscores!)")
        userin = input("Enter the value you'd like to change: ")
    if userin.strip().lower() == "shelter_name" or userin.strip().lower() == "leader":
        new_str(userin)
    elif userin.strip().lower() == "food" or userin.strip().lower() == "survivors" or userin.strip().lower() == "water":
        new_num(userin)
    elif userin.strip().lower() == "barricade_health":
        new_num_under_100(userin)
    elif userin.strip().lower() == "radio":
        userin = "radio_working"
        new_bool(userin)
    else: 
        print("Nothing was changed.")
        with open("shelter_change.txt", "a") as file:
            file.write(f"{time_stamp} | nothing changed\n")

def view_changes():
    '''This function prints out the change log'''
    with open("shelter_change.txt", "r") as file:
        content = file.read()
    print(content)
   

def main():
    menu = input("""
1. View shelter information
2. Change a shelter value
3. View change log
4. Quit
""")
    while True:
        if menu == "1":
            print_log()
            menu = input("""
1. View shelter information
2. Change a shelter value
3. View change log
4. Quit
""")
        elif menu == "2":
            change_value()
            menu = input("""
1. View shelter information
2. Change a shelter value
3. View change log
4. Quit
""")
        elif menu == "3":
            view_changes()
            menu = input("""
1. View shelter information
2. Change a shelter value
3. View change log
4. Quit
""")
        elif menu == "4":
            break
        else:
            print("invalid input")
            menu = input("""
1. View shelter information
2. Change a shelter value
3. View change log
4. Quit
""")

if __name__ == "__main__":
    main()