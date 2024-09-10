import time
print("")
print("---------------------")
print("D&D Character Creator")
print("---------------------")
print("")
print("")

def char_creation():
    char_name = "none"
    char_Gender = "none"
    char_age = "none"
    char_race = "none"
    char_sub_race = "none"
    char_class = "none"
    char_sub_class = "none"
    print("------------------")
    print("Character Creation")
    print("------------------")
    char_name = input("Character Name: ")
    print("")
    
    print("Character gender")
    print("| 1 - Male | 2 - Female | 3 - Other |")
    char_Gender = input("Character Gender: ")
    
    if char_Gender == "1":
        char_Gender = "Male"
    elif char_Gender == "2":
        char_Gender = "Female"
    elif char_Gender == "3":
        char_Gender = "Other"
    else:
        print("Invalid Character")
        print("Restarting Character editor")
        time.sleep(0.5)
        print("")
        return char_creation()
    print("")
    char_age = input("Character Age: ")
    
    print("")
    print("Character Race")
    print("| 1 - Human | 2 - Elf | 3 - Dwarf | 4 - Orc | 5 - Tiefling | 6 - DragonBorn | 7 - Halfling | 8 - Half-Elf | 9 - Gnome | 10 - Half-Orc |")
    char_race = input("Character Race: ")
    
    if char_race == "1":
        char_race = "Human"
    elif char_race == "2":
        char_race = "Elf"
    elif char_race == "3":
        char_race = "Dwarf"
    elif char_race == "4":
        char_race = "Orc"
    elif char_race == "5":
        char_race = "Tiefling"
    elif char_race == "6":
        char_race = "DragonBorn"
    elif char_race == "7":
        char_race = "Halfling"
    elif char_race == "8":
        char_race = "Half-Elf"
    elif char_race == "9":
        char_race = "Gnome"
    elif char_race == "10":
        char_race = "Half-Orc"
    else:
        print("Invalid race")
        return char_creation()
    
    if char_race == "Human":
        print("Human Sub-Races")
        print("| 1 - Northerner | 2 - Desert Nomad | 3 - Islander | 4 - Highlander | 5 - Steppe Warrior | 6 - Eastern | 7 - Southern Plains | 8 - Forest Dweller | 9 - Mediterranean | 10 - Tundra Survivor |")
        char_sub_race = input("Character Sub-Race: ")

        if char_sub_race == "1":
            char_sub_race = "Northerner"
        elif char_sub_race == "2":
            char_sub_race = "Desert Nomad"
        elif char_sub_race == "3":
            char_sub_race = "Islander"
        elif char_sub_race == "4":
            char_sub_race = "Highlander"
        elif char_sub_race == "5":
            char_sub_race = "Steppe Warrior"
        elif char_sub_race == "6":
            char_sub_race = "Eastern"
        elif char_sub_race == "7":
            char_sub_race = "Southern Plains"
        elif char_sub_race == "8":
            char_sub_race = "Forest Dweller"
        elif char_sub_race == "9":
            char_sub_race = "Mediterranean"
        elif char_sub_race == "10":
            char_sub_race = "Tundra Survivor"
        else:
            print("Invalid Sub-Race")
            return char_creation()

    if char_race == "Tiefling":
        print("Tiefling Sub-Races")
        print("| 1 - Infernal Tiefling | 2 - Abyssal Tiefling |")
        char_sub_race = input("Character Sub-Race: ")

        if char_sub_race == "1":
            char_sub_race = "Infernal Tiefling"
        elif char_sub_race == "2":
            char_sub_race = "Abyssal Tiefling"
        else:
            print("Invalid Sub-Race")
            return char_creation()

    if char_race == "DragonBorn":
        print("Dragonborn Sub-Races")
        print("| 1 - Black | 2 - Blue | 3 - Red | 4 - Green | 5 - White | 6 - Gold | 7 - Silver | 8 - Bronze | 9 - Copper | 10 - Brass |")
        char_sub_race = input("Character Sub-Race: ")

        if char_sub_race == "1":
            char_sub_race = "Black"
        elif char_sub_race == "2":
            char_sub_race = "Blue"
        elif char_sub_race == "3":
            char_sub_race = "Red"
        elif char_sub_race == "4":
            char_sub_race = "Green"
        elif char_sub_race == "5":
            char_sub_race = "White"
        elif char_sub_race == "6":
            char_sub_race = "Gold"
        elif char_sub_race == "7":
            char_sub_race = "Silver"
        elif char_sub_race == "8":
            char_sub_race = "Bronze"
        elif char_sub_race == "9":
            char_sub_race = "Copper"
        elif char_sub_race == "10":
            char_sub_race = "Brass"
        else:
            print("Invalid Sub-Race")
            return char_creation()

    if char_race == "Halfling":
        print("Halfling Sub-Races")
        print("| 1 - Lightfoot Halfling | 2 - Stout Halfling | 3 - Ghostwise Halfling |")
        char_sub_race = input("Character Sub-Race: ")

        if char_sub_race == "1":
            char_sub_race = "Lightfoot Halfling"
        elif char_sub_race == "2":
            char_sub_race = "Stout Halfling"
        elif char_sub_race == "3":
            char_sub_race = "Ghostwise Halfling"
        else:
            print("Invalid Sub-Race")
            return char_creation()

    if char_race == "Half-Elf":
        print("Half-Elf typically has no sub-races but you can choose traits from their elven heritage.")
        char_sub_race = "None"

    if char_race == "Gnome":
        print("Gnome Sub-Races")
        print("| 1 - Forest Gnome | 2 - Rock Gnome | 3 - Deep Gnome |")
        char_sub_race = input("Character Sub-Race: ")

        if char_sub_race == "1":
            char_sub_race = "Forest Gnome"
        elif char_sub_race == "2":
            char_sub_race = "Rock Gnome"
        elif char_sub_race == "3":
            char_sub_race = "Deep Gnome "
        else:
            print("Invalid Sub-Race")
            return char_creation()

    if char_race == "Elf":
        print("Elf Sub-Races")
        print("| 1 - High Elf | 2 - Wood Elf  | 3 - Dark Elf (Drow) | 4 - Eladrin | 5 - Sea Elf  | 6 - Shadar-kai |")
        char_sub_race = input("Character Sub-Race: ")

        if char_sub_race == "1":
            char_sub_race = "High Elf"
        elif char_sub_race == "2":
            char_sub_race = "Wood Elf"
        elif char_sub_race == "3":
            char_sub_race = "Dark Elf"
        elif char_sub_race == "4":
            char_sub_race = "Eladrin"
        elif char_sub_race == "5":
            char_sub_race = "Sea Elf"
        elif char_sub_race == "6":
            char_sub_race = "Shadar-kai"
        else:
            print("Invalid Sub-Race")
            return char_creation()

    if char_race == "Dwarf":
        print("Dwarf Sub-Races")
        print("| 1 - Hill Dwarf | 2 - Mountain Dwarf  | 3 - Duergar (Gray Dwarf) |")
        char_sub_race = input("Character Sub-Race: ")

        if char_sub_race == "1":
            char_sub_race = "Hill Dwarf"
        elif char_sub_race == "2":
            char_sub_race = "Mountain Dwarf"
        elif char_sub_race == "3":
            char_sub_race = "Duergar (Gray Dwarf)"
        else:
            print("Invalid Sub-Race")
            return char_creation()

    print("")
    print("Character Class")
    print("| 1 - Barbarian | 2 - Bard | 3 - Cleric | 4 - Druid | 5 - Fighter | 6 - Monk | 7 - Paladin | 8 - Ranger | 9 - Rogue | 10 - Warlock | 11 - Wizard | 12 - Artificer |")
    char_class = input("Character Class: ")

    if char_class == "1":
        char_class = "Barbarian"
    elif char_class == "2":
        char_class = "Bard"
    elif char_class == "3":
        char_class = "Cleric"
    elif char_class == "4":
        char_class = "Druid"
    elif char_class == "5":
        char_class = "Fighter"
    elif char_class == "6":
        char_class = "Monk"
    elif char_class == "7":
        char_class = "Paladin"
    elif char_class == "8":
        char_class = "Ranger"
    elif char_class == "9":
        char_class = "Rogue"
    elif char_class == "10":
        char_class = "Warlock"
    elif char_class == "11":
        char_class = "Wizard"
    elif char_class == "12":
        char_class = "Artificer"
    else:
        print("Invalid Class")
        return char_creation()
    
    if char_class == "Barbarian"
        print("")
        print("Barbarian Sub-Class's")
        

    return char_name, char_Gender, char_age, char_race, char_sub_race, char_class, char_sub_class

char_name, char_Gender, char_age, char_race, char_sub_race, char_class, char_sub_class = char_creation()

print("----------------------------")
print(f"Character Name: {char_name}")
print(f"Character Gender: {char_Gender}")
print(f"Character Age: {char_age}")
print(f"Character Race: {char_race}")
print(f"Character Sub-Race: {char_sub_race}")
print(f"Character Class: {char_class}")
print("----------------------------")
print("")
def confirm():
    last_action = input("Is This Correct? y/n: ")
    if last_action == "y":
        print("")
    elif last_action == "n":
        char_creation()
        confirm()
    else:
        print("Unknown Character")
        confirm()
confirm()
print("")
time.sleep(0.5)

def Stats():
    print("There are 6 stats.")
    print("strength, dexterity, constitution, intelligence, wisdom, and charisma.")
    time.sleep(0.5)
    print("All Stats Start at 0")
    time.sleep(0.5)
    print("You have 32 points to invest")
    time.sleep(0.5)
    print("")
    strength = int(input("How many points in Strength: "))
    dexterity = int(input("How many points in Dexterity: "))
    constitution = int(input("How many points in Constitution: "))
    intelligence = int(input("How many points in Intelligence: "))
    wisdom = int(input("How many points in Wisdom: "))
    charisma = int(input("How many points in Charisma: "))

    if strength + dexterity + constitution + intelligence + wisdom + charisma > 32:
        print("")
        print("You spent more than 32 Points.")
        print("")
        Stats()
    else:
        print("")

    return strength, dexterity, constitution, intelligence, wisdom, charisma

strength, dexterity, constitution, intelligence, wisdom, charisma = Stats()

print(f"Strength Stat: {strength}")
print(f"Dexterity Stat: {dexterity}")
print(f"Constitution Stat: {constitution}")
print(f"Intelligence Stat: {intelligence}")
print(f"Wisdom Stat: {wisdom}")
print(f"Charisma Stat: {charisma}")
print("")

def confirm_2():
    last_action = input("Is This Correct? y/n: ")
    if last_action == "y":
        print("")
    elif last_action == "n":
        Stats()
        confirm_2()
    else:
        print("Unknown Character")
        confirm_2()
confirm_2()
print("")

print("------Character Info--------")
print(f"Character Name: {char_name}")
print(f"Character Gender: {char_Gender}")
print(f"Character Age: {char_age}")
print(f"Character Race: {char_race}")
print(f"Character Sub-Race: {char_sub_race}")
print(f"Character Class: {char_class}")
print(f"Character Sub-Class: {char_sub_class}")
print("------Character Stats--------")
print(f"Strength Stat: {strength}")
print(f"Dexterity Stat: {dexterity}")
print(f"Constitution Stat: {constitution}")
print(f"Intelligence Stat: {intelligence}")
print(f"Wisdom Stat: {wisdom}")
print(f"Charisma Stat: {charisma}")
print("----------------------------")