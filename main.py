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
    
    if char_class == "Barbarian":
        print("")
        print("Barbarian Sub-Class's")
        print("| 1 - Path of the Berserker | 2 - Path of the Totem Warrior | 3 - Path of the Storm Herald | 4 - Path of the Zealot | 5 - Path of the Ancestral Guardian | 6 - Path of the Beast | 7 - Path of Wild Magic |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Path of the Berserker"
        elif char_sub_class == "2":
            char_sub_class = "Path of the Totem Warrior"
        elif char_sub_class == "3":
            char_sub_class = "Path of the Storm Herald"
        elif char_sub_class == "4":
            char_sub_class = "Path of the Zealot"
        elif char_sub_class == "5":
            char_sub_class = "Path of the Ancestral Guardian"
        elif char_sub_class == "6":
            char_sub_class = "Path of the Beast"
        elif char_sub_class == "7":
            char_sub_class = "Path of Wild Magic"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Bard":
        print("")
        print("Bard Sub-Class's")
        print("| 1 - College of Lore | 2 - College of Valor | 3 - College of Glamour | 4 - College of Swords | 5 - College of Whispers | 6 - College of Creation | 7 - College of Eloquence |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
         char_sub_class = "College of Lore"
        elif char_sub_class == "2":
            char_sub_class = "College of Valor"
        elif char_sub_class == "3":
            char_sub_class = "College of Glamour"
        elif char_sub_class == "4":
            char_sub_class = "College of Swords"
        elif char_sub_class == "5":
            char_sub_class = "College of Whispers"
        elif char_sub_class == "6":
            char_sub_class = "College of Creation"
        elif char_sub_class == "7":
            char_sub_class = "College of Eloquence"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Cleric":
        print("")
        print("Cleric Sub-Class's")
        print("| 1 - Life Domain | 2 - Light Domain | 3 - Trickery Domain | 4 - War Domain | 5 - Tempest Domain | 6 - Knowledge Domain | 7 - Nature Domain | 8 - Grave Domain | 9 - Forge Domain | 10 - Order Domain | 11 - Peace Domain | 12 - Twilight Domain |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Life Domain"
        elif char_sub_class == "2":
            char_sub_class = "Light Domain"
        elif char_sub_class == "3":
            char_sub_class = "Trickery Domain"
        elif char_sub_class == "4":
            char_sub_class = "War Domain"
        elif char_sub_class == "5":
            char_sub_class = "Tempest Domain"
        elif char_sub_class == "6":
            char_sub_class = "Knowledge Domain"
        elif char_sub_class == "7":
            char_sub_class = "Nature Domain"
        elif char_sub_class == "8":
            char_sub_class = "Grave Domain"
        elif char_sub_class == "9":
            char_sub_class = "Forge Domain"
        elif char_sub_class == "10":
            char_sub_class = "Order Domain"
        elif char_sub_class == "11":
            char_sub_class = "Peace Domain"
        elif char_sub_class == "12":
            char_sub_class = "Twilight Domain"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Druid":
        print("")
        print("Druid Sub-Class's")
        print("| 1 - Circle of the Land | 2 - Circle of the Moon | 3 - Circle of the Shepherd | 4 - Circle of Spores | 5 - Circle of Dreams | 6 - Circle of Stars | 7 - Circle of Wildfire |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Circle of the Land"
        elif char_sub_class == "2":
            char_sub_class = "Circle of the Moon"
        elif char_sub_class == "3":
            char_sub_class = "Circle of the Shepherd"
        elif char_sub_class == "4":
            char_sub_class = "Circle of Spores"
        elif char_sub_class == "5":
            char_sub_class = "Circle of Dreams"
        elif char_sub_class == "6":
            char_sub_class = "Circle of Stars"
        elif char_sub_class == "7":
            char_sub_class = "Circle of Wildfire"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Fighter":
        print("")
        print("Fighter Sub-Class's")
        print("| 1 - Champion | 2 - Battle Master | 3 - Eldritch Knight | 4 - Arcane Archer | 5 - Samurai | 6 - Cavalier | 7 - Echo Knight | 8 - Psi Warrior | 9 - Rune Knight |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Champion"
        elif char_sub_class == "2":
            char_sub_class = "Battle Master"
        elif char_sub_class == "3":
            char_sub_class = "Eldritch Knight"
        elif char_sub_class == "4":
            char_sub_class = "Arcane Archer"
        elif char_sub_class == "5":
            char_sub_class = "Samurai"
        elif char_sub_class == "6":
            char_sub_class = "Cavalier"
        elif char_sub_class == "7":
            char_sub_class = "Echo Knight"
        elif char_sub_class == "8":
            char_sub_class = "Psi Warrior"
        elif char_sub_class == "9":
            char_sub_class = "Rune Knight"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Monk":
        print("")
        print("Monk Sub-Class's")
        print("| 1 - Way of the Open Hand | 2 - Way of Shadow | 3 - Way of the Four Elements | 4 - Way of the Kensei | 5 - Way of the Drunken Master | 6 - Way of the Sun Soul | 7 - Way of Mercy | 8 - Way of the Astral Self |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Way of the Open Hand"
        elif char_sub_class == "2":
            char_sub_class = "Way of Shadow"
        elif char_sub_class == "3":
            char_sub_class = "Way of the Four Elements"
        elif char_sub_class == "4":
            char_sub_class = "Way of the Kensei"
        elif char_sub_class == "5":
            char_sub_class = "Way of the Drunken Master"
        elif char_sub_class == "6":
            char_sub_class = "Way of the Sun Soul"
        elif char_sub_class == "7":
            char_sub_class = "Way of Mercy"
        elif char_sub_class == "8":
            char_sub_class = "Way of the Astral Self"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Paladin":
        print("")
        print("Paladin Sub-Class's")
        print("| 1 - Oath of Devotion | 2 - Oath of Vengeance | 3 - Oath of the Ancients | 4 - Oath of Conquest | 5 - Oath of Redemption | 6 - Oath of Glory | 7 - Oath of the Crown | 8 - Oath of the Watchers |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Oath of Devotion"
        elif char_sub_class == "2":
            char_sub_class = "Oath of Vengeance"
        elif char_sub_class == "3":
            char_sub_class = "Oath of the Ancients"
        elif char_sub_class == "4":
            char_sub_class = "Oath of Conquest"
        elif char_sub_class == "5":
            char_sub_class = "Oath of Redemption"
        elif char_sub_class == "6":
            char_sub_class = "Oath of Glory"
        elif char_sub_class == "7":
            char_sub_class = "Oath of the Crown"
        elif char_sub_class == "8":
            char_sub_class = "Oath of the Watchers"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Ranger":
        print("")
        print("Ranger Sub-Class's")
        print("| 1 - Hunter | 2 - Beast Master | 3 - Gloom Stalker | 4 - Horizon Walker | 5 - Monster Slayer | 6 - Fey Wanderer | 7 - Swarmkeeper | 8 - Drakewarden |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Hunter"
        elif char_sub_class == "2":
            char_sub_class = "Beast Master"
        elif char_sub_class == "3":
            char_sub_class = "Gloom Stalker"
        elif char_sub_class == "4":
            char_sub_class = "Horizon Walker"
        elif char_sub_class == "5":
            char_sub_class = "Monster Slayer"
        elif char_sub_class == "6":
            char_sub_class = "Fey Wanderer"
        elif char_sub_class == "7":
            char_sub_class = "Swarmkeeper"
        elif char_sub_class == "8":
            char_sub_class = "Drakewarden"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Rogue":
        print("")
        print("Rogue Sub-Class's")
        print(" | 1 - Thief | 2 - Assassin | 3 - Arcane Trickster | 4 - Mastermind | 5 - Swashbuckler | 6 - Inquisitive | 7 - Scout | 8 - Phantom | 9 - Soulknife |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Thief"
        elif char_sub_class == "2":
            char_sub_class = "Assassin"
        elif char_sub_class == "3":
            char_sub_class = "Arcane Trickster"
        elif char_sub_class == "4":
            char_sub_class = "Mastermind"
        elif char_sub_class == "5":
            char_sub_class = "Swashbuckler"
        elif char_sub_class == "6":
            char_sub_class = "Inquisitive"
        elif char_sub_class == "7":
            char_sub_class = "Scout"
        elif char_sub_class == "8":
            char_sub_class = "Phantom"
        elif char_sub_class == "9":
            char_sub_class = "Soulknife"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Warlock":
        print("")
        print("Warlock Sub-Class's")
        print("| 1 - The Fiend | 2 - The Great Old One | 3 - The Archfey | 4 - The Celestial | 5 - The Hexblade | 6 - The Fathomless | 7 - The Genie | 8 - The Undead |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "The Fiend"
        elif char_sub_class == "2":
            char_sub_class = "The Great Old One"
        elif char_sub_class == "3":
            char_sub_class = "The Archfey"
        elif char_sub_class == "4":
            char_sub_class = "The Celestial"
        elif char_sub_class == "5":
            char_sub_class = "The Hexblade"
        elif char_sub_class == "6":
            char_sub_class = "The Fathomless"
        elif char_sub_class == "7":
            char_sub_class = "The Genie"
        elif char_sub_class == "8":
            char_sub_class = "The Undead"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Wizard":
        print("")
        print("Wizard Sub-Class's")
        print("| 1 - School of Evocation | 2 - School of Conjuration | 3 - School of Divination | 4 - School of Enchantment | 5 - School of Illusion | 6 - School of Necromancy | 7 - School of Transmutation | 8 - School of Abjuration | 9 - Bladesinging | 10 - War Magic | 11 - Chronurgy Magic | 12 - Graviturgy Magic | 13 - Scribes (Order of Scribes) |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "School of Evocation"
        elif char_sub_class == "2":
            char_sub_class = "School of Conjuration"
        elif char_sub_class == "3":
            char_sub_class = "School of Divination"
        elif char_sub_class == "4":
            char_sub_class = "School of Enchantment"
        elif char_sub_class == "5":
            char_sub_class = "School of Illusion"
        elif char_sub_class == "6":
            char_sub_class = "School of Necromancy"
        elif char_sub_class == "7":
            char_sub_class = "School of Transmutation"
        elif char_sub_class == "8":
            char_sub_class = "School of Abjuration"
        elif char_sub_class == "9":
            char_sub_class = "Bladesinging"
        elif char_sub_class == "10":
            char_sub_class = "War Magic"
        elif char_sub_class == "11":
            char_sub_class = "Chronurgy Magic"
        elif char_sub_class == "12":
            char_sub_class = "Graviturgy Magic"
        elif char_sub_class == "13":
            char_sub_class = "Order of Scribes"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    if char_class == "Artificer":
        print("")
        print("Artificer Sub-Class's")
        print("| 1 - Alchemist | 2 - Armorer | 3 - Artillerist | 4 - Battle Smith |")
        char_sub_class = input("Character Sub-Class: ")
        if char_sub_class == "1":
            char_sub_class = "Alchemist"
        elif char_sub_class == "2":
            char_sub_class = "Armorer"
        elif char_sub_class == "3":
            char_sub_class = "Artillerist"
        elif char_sub_class == "4":
            char_sub_class = "Battle Smith"
        else:
            print("Invalid Sub-Class")
            return char_creation()

    return char_name, char_Gender, char_age, char_race, char_sub_race, char_class, char_sub_class

char_name, char_Gender, char_age, char_race, char_sub_race, char_class, char_sub_class = char_creation()

print("----------------------------")
print(f"Character Name: {char_name}")
print(f"Character Gender: {char_Gender}")
print(f"Character Age: {char_age}")
print(f"Character Race: {char_race}")
print(f"Character Sub-Race: {char_sub_race}")
print(f"Character Class: {char_class}")
print(f"Character Sub-Class: {char_sub_class}")
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