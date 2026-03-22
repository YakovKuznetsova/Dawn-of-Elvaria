import time
import pygame
import traceback
import os
import random
from colorama import init, Fore, Style, Back
import pyfiglet
import copy
from Game_Setup import *
import sys

# import subprocess
# def install_requirements():
#    if os.path.exists("requirements.txt"):
#        print("Installazione delle dipendenze da requirements.txt...")
#        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
#    else:
#        print("File requirements.txt non trovato.")
#
# install_requirements()

#####################################################
# CREATION INDEX / CREATION LIST / COLOR

os.system("title Dawn of Elvaria")
init(autoreset=True)
try:
    os.system('cls')
    pygame.init()
    os.system('cls')
    pygame.mixer.init()
    os.system('cls')
except:
    os.system('cls')
    for i in range(0,5):
        print(f"{Fore.RED}COLLEGA UN DISPOSITIVO AUDIO DI OUTPUT")
        
ORANGE = "\033[38;5;208m"
GRENNI = "\033[38;5;58m"
DARKRED = "\033[38;5;88m"
TEAM_COLOR = "\033[38;5;156m" 
ENEMY_COLOR = "\033[38;5;90m" 
STATS_COLOR = "\033[38;5;66m"
STATS_COLOR2 = "\033[38;5;73m"
B = Fore.BLACK + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
GRAY = "\033[38;5;247m"

CI = {}
CL = []
TempCreationDict = {
    "Name":"NB",
    "Race":"NB",
    "Gender":"NB",
    "Age":"NB",
    "Weapon":"NB"
}
GlobalTempTeam = {}
GlobalTempEnemyTeam = {}
GlobalTempGraveyard = {}

#####################################################
# MUSIC

def get_resource_path(relative_path):
    """Restituisce il percorso assoluto per i file e le risorse inclusi nell'eseguibile"""
    if hasattr(sys, "_MEIPASS"):
        # Se il programma è stato impacchettato con PyInstaller, usa il percorso temporaneo
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def play_music(next_file, loop, fade_out_ms=2000, fade_in_ms=2000):
    if pygame.mixer.music.get_busy():  
        pygame.mixer.music.fadeout(fade_out_ms)
    
    if next_file != get_resource_path("Audio_Assets/Soundtrack/menu.wav"):
        pygame.mixer.music.set_volume(0.3)
    else:
        pygame.mixer.music.set_volume(0.5)
    
    pygame.mixer.music.load(next_file)
    pygame.mixer.music.play(loops=loop, fade_ms=fade_in_ms)

def weaponSound(weapon_type):
    match weapon_type:
        case "Hand":
            sound_file = f"hand_sound_{random.randint(1, 4)}.wav"
            sound_path = get_resource_path(f"Audio_Assets/Soundeffect/WeaponSound/{sound_file}")
            hand_sound = pygame.mixer.Sound(sound_path)
            hand_sound.set_volume(0.75)
            hand_sound.play()
        case "Light":
            light_sound = pygame.mixer.Sound(get_resource_path("Audio_Assets/Soundeffect/WeaponSound/light_sound.wav"))
            light_sound.set_volume(0.75)
            light_sound.play()
        case "Heavy":
            heavy_sound = pygame.mixer.Sound(get_resource_path("Audio_Assets/Soundeffect/WeaponSound/heavy_sound.wav"))
            heavy_sound.set_volume(0.75)
            heavy_sound.play()
        case "Bow":
            bow_sound = pygame.mixer.Sound(get_resource_path("Audio_Assets/Soundeffect/WeaponSound/bow_sound.wav"))
            bow_sound.set_volume(0.75)
            bow_sound.play()

#####################################################
# INVENTORY

Inventory = {
    "POTION_AND_FOOD": {
        "Potion": [
            
        ],
        "Food": [
            
        ]
    },

    "ARROWS": [
        
    ],

    "WEAPON_AND_EQUIP": {
        "Weapon": [
            
        ],
        "Equip": [
            
        ]
    },

    "ITEMS": [
        
    ]
}

def Inventory_Insert(item, category):
    existing_item = Inventory_Check(item.name, category)
    
    if existing_item:
        if category.upper() == "ARROW":
            existing_item.count += 1
        elif category.upper() == "POTION":
            existing_item.count += 1
        elif category.upper() == "WEAPON":
            existing_item.count += 1
        elif category.upper() == "EQUIP":
            existing_item.count += 1

    else:
        if category.upper() == "POTION":
            Inventory["POTION_AND_FOOD"]["Potion"].append({item.name: item})
        elif category.upper() == "FOOD":
            Inventory["POTION_AND_FOOD"]["Food"].append({item.name: item})
        elif category.upper() == "ARROW":
            Inventory["ARROWS"].append({item.name: item})
        elif category.upper() == "WEAPON":
            Inventory["WEAPON_AND_EQUIP"]["Weapon"].append({item.name: item})
        elif category.upper() == "EQUIP":
            Inventory["WEAPON_AND_EQUIP"]["Equip"].append({item.name: item})
        elif category.upper() == "ITEM":
            Inventory["ITEMS"].append({item.name: item})


def Inventory_Remove(item, category):
    existing_item = Inventory_Check(item.name, category)
    
    if existing_item:
        if category.upper() == "ARROW" and existing_item.count > 1:
            existing_item.count -= 1
        elif category.upper() == "POTION" and existing_item.count > 1:
            existing_item.count -= 1
        elif category.upper() == "WEAPON" and existing_item.count > 1:
            existing_item.count -= 1
        elif category.upper() == "EQUIP" and existing_item.count > 1:
            existing_item.count -= 1

        else:
            if category.upper() == "POTION":
                Inventory["POTION_AND_FOOD"]["Potion"] = [
                    potion for potion in Inventory["POTION_AND_FOOD"]["Potion"]
                    if item.name not in potion
                ]
            elif category.upper() == "FOOD":
                Inventory["POTION_AND_FOOD"]["Food"] = [
                    food for food in Inventory["POTION_AND_FOOD"]["Food"]
                    if item.name not in food
                ]
            elif category.upper() == "ARROW":
                Inventory["ARROWS"] = [
                    arrow for arrow in Inventory["ARROWS"]
                    if item.name not in arrow
                ]
            elif category.upper() == "WEAPON":
                Inventory["WEAPON_AND_EQUIP"]["Weapon"] = [
                    weapon for weapon in Inventory["WEAPON_AND_EQUIP"]["Weapon"]
                    if item.name not in weapon
                ]
            elif category.upper() == "EQUIP":
                Inventory["WEAPON_AND_EQUIP"]["Equip"] = [
                    equip for equip in Inventory["WEAPON_AND_EQUIP"]["Equip"]
                    if item.name not in equip
                ]
            elif category.upper() == "ITEM":
                Inventory["ITEMS"] = [
                    item_dict for item_dict in Inventory["ITEMS"]
                    if item.name not in item_dict
                ]

def Inventory_Check(item_name, category):
    if category.upper() == "POTION":
        for potion in Inventory["POTION_AND_FOOD"]["Potion"]:
            if item_name in potion:
                return potion[item_name]
    elif category.upper() == "FOOD":
        for food in Inventory["POTION_AND_FOOD"]["Food"]:
            if item_name in food:
                return food[item_name]
    elif category.upper() == "ARROW":
        for arrow in Inventory["ARROWS"]:
            if item_name in arrow:
                return arrow[item_name]
    elif category.upper() == "WEAPON":
        for weapon in Inventory["WEAPON_AND_EQUIP"]["Weapon"]:
            if item_name in weapon:
                return weapon[item_name]
    elif category.upper() == "EQUIP":
        for equip in Inventory["WEAPON_AND_EQUIP"]["Equip"]:
            if item_name in equip:
                return equip[item_name]
    elif category.upper() == "ITEM":
        for item in Inventory["ITEMS"]:
            if item_name in item:
                return item[item_name]
    return None

def Print_Inventory_Items(item):
    os.system('cls')
    print(Fore.WHITE + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("Inventory")))
    print(f"{B}|========================================================================|\n")
    print(f"\n{GRAY} [ {item.name.upper()} ]")
    for attribute, value in item.__dict__.items():
        if attribute == "Mana" or attribute == "Stamina" or attribute == "HP" or attribute == "armor":
            print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value[1]}")
        elif attribute == "ammo":
            print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value.name}")
        elif attribute == "TAG_Effect":
            pass
        else:
            print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value}")
    
    print(f"\n\n{B}press any key to continue\n")
    os.system('pause > null')
    return

def Open_Inventory_Visualizer(category, section):
    while True:
        tempindexdict = {}

        os.system('cls')
        print(Fore.WHITE + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("Inventory")))
        print(f"{B}|========================================================================|\n")
        items_to_display = Inventory[category] if section == "nb" else Inventory[category][section]
        for idx, i in enumerate(items_to_display, start=1):
            tempindexdict[str(idx)] = i
            idx_print = f"{B}{'0'*(3-len(str(idx)))}{ORANGE}{idx}"

            for key, value in i.items():
                key = key.ljust(12)

                count_display = value.count if hasattr(value, 'count') else 0
                print(f"  {B}[{ORANGE}{idx_print}{B}] {STATS_COLOR}[ {GRAY}{key[:12]} {STATS_COLOR}]{B}[{count_display}] {Fore.RED}|", end="")
                if idx % 3 == 0:
                    print("\n", end="")

        print(f"\n\n{GRAY} [ SELECT AN ITEM OR WRITE ANYTHING ELSE TO EXIT ]")
        Inventory_Menu2 = input(f"\n{W} [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        if Inventory_Menu2 in tempindexdict:
            selected_item = tempindexdict[Inventory_Menu2]
            for key, value in selected_item.items():
                Print_Inventory_Items(value)
                break

        else:
            return

def Open_Inventory():
    while True:
        os.system('cls')
        print(Fore.WHITE + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("Inventory")))
        print(f"{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ INVENTORY SELECT ]\n")
        print(f"  {B}[{ORANGE}1{B}] [ {Fore.RED}POTIONS {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}2{B}] [ {Fore.RED}FOODS {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}3{B}] [ {Fore.RED}ARROWS {B}- {GRAY}M. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}4{B}] [ {Fore.RED}WEAPONS {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}5{B}] [ {Fore.RED}EQUIP {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}6{B}] [ {Fore.RED}ITEMS {B}- {GRAY}M. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}7{B}] [ {Fore.RED}EXIT{B} ]\n")

        
        Inventory_Menu = input(f"\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        match Inventory_Menu:
            case "1":
                Open_Inventory_Visualizer("POTION_AND_FOOD","Potion")
                continue

            case "2":
                Open_Inventory_Visualizer("POTION_AND_FOOD","Food")
                continue

            case "3":
                Open_Inventory_Visualizer("ARROWS","nb")
                continue

            case "4":
                Open_Inventory_Visualizer("WEAPON_AND_EQUIP","Weapon")
                continue

            case "5":
                Open_Inventory_Visualizer("WEAPON_AND_EQUIP","Equip")
                continue

            case "6":
                Open_Inventory_Visualizer("ITEMS","nb")
                continue

            case "7":
                break

            case _:
                exception("Enter a valid number value")
                os.system('cls')
    
    return

#####################################################
# CREATION CHARACTER

def Creation():
    os.system('cls')
    print(Fore.CYAN + Style.NORMAL + (ascii_art := pyfiglet.figlet_format("Dawn of Elvaria")))
    print(f"{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ CREATE YOUR CHARACTER ]\n")

    Creation_Name()
    Creation_Race()
    Creation_Gender()
    Creation_Age()
    Creation_Weapon()

    while True:
        os.system('cls')
        print(Fore.CYAN + Style.NORMAL + (ascii_art := pyfiglet.figlet_format("Dawn of Elvaria")))
        print(f"{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ CHARACTER SUMMARY ]\n")
        
        for i in TempCreationDict:
            if i != "Weapon":
                print(f"\n{W}  [ {ORANGE}{i.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{TempCreationDict[i]}")
            else:
                print(f"\n{W}  [ {ORANGE}{i.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{TempCreationDict[i].name}")

        print(f"\n{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ IS EVERYTHING CORRECT? ][ WRITE '{Fore.RED}ABORT{Fore.CYAN}' TO CANCEL ]\n")
        RepChoice = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        if RepChoice.lower() in ['yes','yp','si','sì','y','yep','s']:
            CI[TempCreationDict["Name"]] = Character(Name=TempCreationDict["Name"],Race=TempCreationDict["Race"],Gender=TempCreationDict["Gender"],Age=TempCreationDict["Age"],Weapon=TempCreationDict["Weapon"],Armor=Cloth_Garments)
            CL.append(TempCreationDict["Name"])
            return
        elif RepChoice.lower() == "abort":
            return
        else:
            while True:
                os.system('cls')
                print(Fore.CYAN + Style.NORMAL + (ascii_art := pyfiglet.figlet_format("Dawn of Elvaria")))
                print(f"{B}|========================================================================|\n")
                print(f"{Fore.CYAN} [ WHAT DO YOU WANT TO CHANGE? ][ WRITE '{Fore.RED}ABORT{Fore.CYAN}' TO CANCEL ]\n")

                print(f"\n{W}  [ {Fore.BLUE}info{Fore.WHITE} ]  ==> {B}'{ORANGE}1{B}' = Name | '{ORANGE}2{B}' = Race | '{ORANGE}3{B}' = Gender | '{ORANGE}4{B}' = Age | '{ORANGE}5{B}' = Weapon")
                ChangeChoice = input(f"\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                if ChangeChoice in ["1","2","3","4","5"]:
                    if ChangeChoice == "1":
                        Creation_Name()
                        break
                    elif ChangeChoice == "2":
                        Creation_Race()
                        break
                    elif ChangeChoice == "3":
                        Creation_Gender()
                        break
                    elif ChangeChoice == "4":
                        Creation_Age()
                        break
                    elif ChangeChoice == "5":
                        Creation_Weapon()
                        break
                elif ChangeChoice.lower() == "abort":
                    break
                else:
                    exception("Enter a valid number")
                    continue 

def Creation_Name():
    while True:
        ChooseName = input(f"\n{W}  [ {ORANGE}1{Fore.WHITE} ] -  {Fore.YELLOW}Choose the Character's Name: {Fore.BLUE}").capitalize()

        if ChooseName in CI:
            exception("the character already exists, change it or insert an epithet")
            continue 
        else:
            TempCreationDict["Name"] = ChooseName
            return

def Creation_Race():
    while True:
        RaceChoice = input(f"\n{W}  [ {ORANGE}2{Fore.WHITE} ] -  {Fore.YELLOW}Choose the Character's Race: {Fore.BLUE}").capitalize().strip()

        if not RaceChoice.isalpha():
            exception("the name of your race cannot contain numbers or special characters")
            continue 
        else:
            TempCreationDict["Race"] = RaceChoice
            return

def Creation_Gender():
    TempDictGender = {
        "1":"Male",
        "2":"Female",
        "3":"Unknown",
        "4":"Genderless"
    }

    while True:
        print(f"\n{W}  [ {Fore.BLUE}preset{Fore.WHITE} ]  ==> {B}'{ORANGE}1{B}' = Male [MM] | '{ORANGE}2{B}' = Female [FM] | '{ORANGE}3{B}' = Unknown [UK] | '{ORANGE}4{B}' = Genderless [NB]")
        GenderChoice = input(f"{W}  [ {ORANGE}3{Fore.WHITE} ] -  {Fore.YELLOW}Choose a Preset or Write your Own Gender Custom: {Fore.BLUE}").capitalize().strip()
        
        if GenderChoice in TempDictGender:
            TempCreationDict["Gender"] = TempDictGender[GenderChoice]
            return
        elif not GenderChoice.isalpha():
            exception("the name of your gender cannot contain numbers or special characters.")
            continue 
        else:
            TempCreationDict["Gender"] = GenderChoice
            return

def Creation_Age():
    while True:
        AgeChoice = input(f"\n{W}  [ {ORANGE}4{Fore.WHITE} ] -  {Fore.YELLOW}Choose the Character's Age (It Must be a Number): {Fore.BLUE}").strip()

        if not AgeChoice.isdigit():
            exception("you must enter a number")
            continue 
        else:
            TempCreationDict["Age"] = AgeChoice
            return

def Creation_Weapon():
    TempDictWeapon = {
        "1":Punch,
        "2":Sword,
        "3":Staff,
        "4":Bow,
        "5":Hammer
    }

    while True:
        print(f"\n{W}  [ {Fore.BLUE}preset{Fore.WHITE} ]  ==> {B}'{ORANGE}1{B}' = Punch | '{ORANGE}2{B}' = Sword | '{ORANGE}3{B}' = Staff | '{ORANGE}4{B}' = Bow | '{ORANGE}5{B}' = Hammer")
        WeaponChoice = input(f"{W}  [ {ORANGE}5{Fore.WHITE} ] -  {Fore.YELLOW}Choose the Character's Weapon: {Fore.BLUE}").strip()

        if WeaponChoice in TempDictWeapon:
            TempCreationDict["Weapon"] = TempDictWeapon[WeaponChoice]
            Check_Arrow = Inventory_Check("Iron_Arrow","ARROW")
            try:
                if WeaponChoice == "4" and Check_Arrow.count <= 30:
                    for n in range(1,11):
                        Inventory_Insert(IronArrow,"ARROW")
                break
            except: 
                for n in range(1,11):
                    Inventory_Insert(IronArrow,"ARROW")
                break
        else:
            exception("You must choose one of the four weapons provided in the choice menu.")
            continue 

#####################################################
# VIEW CHARACTER

def View():
    while True:
        os.system('cls')
        print(Fore.CYAN + Style.NORMAL + (ascii_art := pyfiglet.figlet_format("Dawn of Elvaria")))
        print(f"{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ LIST OF CREATED CHARACTERS ]\n")
        
        TempCount = 1
        for index, character in enumerate(CL,start=1):
            print(f"{W}  [ {ORANGE}{index}{Fore.WHITE} ] -  {Fore.YELLOW}{character}\n")
            TempCount += 1
        
        print(f"{W}  [ {ORANGE}{TempCount}{Fore.WHITE} ] -  {Fore.YELLOW}{Fore.RED}EXIT\n")
        
        print(f"\n{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ VIEW A SPECIFIC CHARACTER ][ WRITE '{Fore.RED}EXIT{Fore.CYAN}' TO CANCEL ]\n")
        ViewChoice = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        try:
            if int(ViewChoice) == TempCount:
                return
            elif ViewChoice.isdigit():
                if int(ViewChoice) > len(CL) or int(ViewChoice) <= 0:
                    exception("character not in the list, enter a valid number")
                    continue 
                else:
                    ViewChoice = int(ViewChoice) - 1
                    Specific_View(ViewChoice)
                    continue
            elif ViewChoice.lower() == "exit" or ViewChoice == str(TempCount):
                return
            else:
                exception("enter a number or write 'EXIT'")
                continue
        except:
            exception("enter a number or write 'EXIT'")
            continue 

def Specific_View(Characters):
    while True:
        os.system('cls')
        Characters = CL[Characters]
        print(Fore.CYAN + Style.NORMAL + (ascii_art := pyfiglet.figlet_format("Dawn of Elvaria")))
        print(f"{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ CHARACTER: {Fore.GREEN}{Characters}{Fore.CYAN} ]\n")

        if Characters in CI:
            ViewCharacter = CI[Characters]
            for attribute, value in ViewCharacter.__dict__.items():
                if attribute == "Mana" or attribute == "Stamina" or attribute == "HP":
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value[1]}")
                elif attribute == "Weapon" or attribute == "Armor":
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value.name}")
                elif attribute == "TAG_Effect":
                    pass
                else:
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value}")
        else:
            exception("the chosen character does not exist")
            continue 

        print(f"\n{B}|========================================================================|\n")
        print(f"{B}press any key to continue")
        os.system('pause > null')
        return

#####################################################
# SETUP TEAM

def CreateTeam():
    os.system('cls')
    TempTeam = []

    print(Fore.CYAN + Style.NORMAL + (ascii_art := pyfiglet.figlet_format("Dawn of Elvaria")))
    print(f"{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ LIST OF CREATED CHARACTERS ]\n")
    
    for index, characters in enumerate(CL,start=1):
        print(f"{W}  [ {ORANGE}{index}{Fore.WHITE} ] -  {Fore.YELLOW}{characters}")
        print(f"{W}  [ {Fore.BLUE}STATS{Fore.WHITE} ]  - {Fore.YELLOW}Race: {B}{CI[characters].Race} | {Fore.YELLOW}Armor: {B}{CI[characters].Armor.name} | {Fore.YELLOW}Weapon: {B}{CI[characters].Weapon.name}\n\n")
    
    print(f"\n{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ CREATE YOUR TEAM - CHOOSE THREE CHARACTERS ][ WRITE '{Fore.RED}EXIT{Fore.CYAN}' TO CANCEL ]\n")

    for number in range(1,4):
        while True:
            TeamMemberNumber = input(f"{W}  [ {Fore.BLUE}N°{number}{Fore.WHITE} ]{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
            if TeamMemberNumber.isdigit():
                if int(TeamMemberNumber) > len(CL) or int(TeamMemberNumber) <= 0:
                    exception("character not in the list, enter a valid number")
                    continue 
                else:
                    TeamMemberNumber = int(TeamMemberNumber) - 1
                    Characters = CL[TeamMemberNumber]
                    if CI[Characters] not in TempTeam:
                        TempTeam.append(CI[Characters])
                        break
                    else:
                        exception("Character Already Taken")
                        continue 
            elif TeamMemberNumber.lower() == "exit":
                return
            else:
                exception("enter a number or write 'EXIT'")
                continue 

    print(f"\n{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ SUMMARY ]\n")
    
    for index, member in enumerate(TempTeam, start=1):
       print(f"{W}  [ {ORANGE}{index}{Fore.WHITE} ] -  {Fore.YELLOW}{member.Name}")
    
    
    print(f"\n{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ IS EVERYTHING CORRECT? ][ WRITE '{Fore.RED}ABORT{Fore.CYAN}' TO CANCEL ]\n")
    RepChoice = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
    if RepChoice.lower() in ['yes','yp','si','sì','y','yep','s']:
        TempTeam.sort(key=lambda member: member.Weapon.velocity, reverse=False)
        return TempTeam
    elif RepChoice.lower() == "abort":
        return
    else:
        exception("Enter a valid option")
        CreateTeam()
        TempTeam.sort(key=lambda member: member.Weapon.velocity, reverse=False)
        return TempTeam

#####################################################
# COMBAT

def start_combat(team,enemyT):
    global GlobalTempTeam
    global GlobalTempEnemyTeam

    GlobalTempTeam = {}
    GlobalTempEnemyTeam = {}
    
    play_music(f"Audio_Assets/Soundtrack/background_{random.randint(1, 7)}.wav", -1)

    for idx, ply in enumerate(team, start=1):
        GlobalTempTeam[f"{idx}_member"] = copy.deepcopy(ply)
    
    if isinstance(enemyT, list):
        sorted_enemyT = sorted(enemyT, key=lambda enemy: enemy.Weapon.velocity, reverse=False)
        for idx, nmy in enumerate(sorted_enemyT, start=1):
            GlobalTempEnemyTeam[f"{idx}_enemy"] = copy.deepcopy(nmy)
    else:
        GlobalTempEnemyTeam["1_enemy"] = copy.deepcopy(enemyT)

    os.system('cls')
    print(Fore.RED + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("preparation")))
    print(f"{B}|========================================================================|\n")

    print(f"{TEAM_COLOR} [ YOUR TEAM ]\n")
    for i in range(1,4):
        print(f"{B}  [{i}][ {Fore.BLUE}{GlobalTempTeam[f'{str(i)}_member'].Name}{B} ] -  {Fore.YELLOW}armor: {B}{GlobalTempTeam[f'{str(i)}_member'].Armor.name} | {Fore.YELLOW}weapon: {B}{GlobalTempTeam[f'{str(i)}_member'].Weapon.name} | {Fore.YELLOW}stats: {B}HP: {GlobalTempTeam[f'{str(i)}_member'].HP[1]}[{GlobalTempTeam[f'{str(i)}_member'].Armor.armor[1]}] / MANA: {GlobalTempTeam[f'{str(i)}_member'].Mana[1]} / STAMINA: {GlobalTempTeam[f'{str(i)}_member'].Stamina[1]} \n")

    print(f"{ENEMY_COLOR} [ ENEMY TEAM ]\n")
    for j in GlobalTempEnemyTeam:
        print(f"{B}  [{j[:-6]}][ {Fore.BLUE}{GlobalTempEnemyTeam[j].Name}{B} ] -  {Fore.YELLOW}armor: {B}{GlobalTempEnemyTeam[j].Armor.name} | {Fore.YELLOW}weapon: {B}{GlobalTempEnemyTeam[j].Weapon.name} | {Fore.YELLOW}stats: {B}HP: {GlobalTempEnemyTeam[j].HP[1]}[{GlobalTempEnemyTeam[j].Armor.armor[1]}] / MANA: {GlobalTempEnemyTeam[j].Mana[1]} / STAMINA: {GlobalTempEnemyTeam[j].Stamina[1]} \n")

    print(f"{B}As soon as you're ready, press any key..\n")
    os.system('pause > null')
    Combat(enemyT,team)
    return

def Combat(enemyT,team):
    global GlobalTempEnemyTeam
    global GlobalTempTeam
    EnemyTotHP = 0
    TeamTotHP = 0
    First_Turn = 1
    
    for member in GlobalTempTeam.values():
        TeamTotHP += member.HP[0]
    for member in GlobalTempEnemyTeam.values():
        EnemyTotHP += member.HP[0]
        
    Who_Start = Who_Starts()

    os.system('cls')
    print("\n"+Fore.RED + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("battle")),end="")
    
    while EnemyTotHP > 0 and TeamTotHP > 0:
        if Who_Start[0] == 0:
            Who_Start[0] = PlayerCombat(Who_Start,First_Turn)
            First_Turn += 1
            
        elif Who_Start[0] == 1:
            Who_Start[0] = EnemyCombat_AI(Who_Start,First_Turn)
            First_Turn += 1
           
        elif Who_Start[0] == 2:
            os.system('cls')
            print(Fore.RED + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("You Lost !")))
            pygame.mixer.music.pause()
            lost_sound = pygame.mixer.Sound("Audio_Assets/Soundeffect/MixSound/lose.wav")
            lost_sound.set_volume(0.5)
            lost_sound.play()
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.unpause()
            print(f"{B}|========================================================================|\n")
            
            print(f"{ENEMY_COLOR} [ ENEMY TEAM ]\n")
            for n,j in enumerate(enemyT,start=1):
                print(f"{B}  [{n}][ {Fore.BLUE}{j.Name}{B} ] -  {Fore.YELLOW}race: {B}{j.Race} | {Fore.YELLOW}weapon: {B}{j.Weapon.name} | {Fore.YELLOW}stats: {B}HP: {j.HP[0]} / MANA: {j.Mana[0]} / STAMINA: {j.Stamina[0]} \n")
            
            time.sleep(1.5)
            
            print(f"\n{B}Press any key to continue..\n")
            os.system('pause > null')
            break
        
        elif Who_Start[0] == 3:
            os.system('cls')
            print(Fore.GREEN + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("You Won !")))
            pygame.mixer.music.pause()
            win_sound = pygame.mixer.Sound("Audio_Assets/Soundeffect/MixSound/win.wav")
            win_sound.set_volume(0.5)
            win_sound.play()
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.unpause()
            print(f"{B}|========================================================================|\n")
            
            print(f"{TEAM_COLOR} [ YOUR TEAM ]\n")
            for i in range(1,4):
                print(f"{B}  [{i}][ {Fore.BLUE}{team[i-1].Name}{B} ] -  {Fore.YELLOW}race: {B}{team[i-1].Race} | {Fore.YELLOW}weapon: {B}{team[i-1].Weapon.name} | {Fore.YELLOW}stats: {B}HP: {team[i-1].HP[0]} / MANA: {team[i-1].Mana[0]} / STAMINA: {team[i-1].Stamina[0]} \n")
            
            time.sleep(0.5)
            print(f"\n{TEAM_COLOR} [ BATTLE STATS ]\n")
            time.sleep(0.5)
            print(f"{B}  - 1 ) {Fore.YELLOW}total turns: {B}{First_Turn}\n")
            time.sleep(0.5)
            print(f"{B}  - 2 ) {Fore.YELLOW}enemies killed: {B}{len(enemyT)}")
            time.sleep(1.5)
            
            print(f"\n{B}Press any key to continue..\n")
            os.system('pause > null')
            break
        
        elif Who_Start[0] == 4:
            os.system('cls')
            print(GRAY + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("Escape !")))
            print(f"{B}|========================================================================|\n")
            
            print(f"{GRAY} [ YOUR TEAM ]\n")
            for i in range(1,4):
                print(f"{B}  [{i}][ {Fore.BLUE}{team[i-1].Name}{B} ] -  {Fore.YELLOW}race: {B}{team[i-1].Race} | {Fore.YELLOW}weapon: {B}{team[i-1].Weapon.name} | {Fore.YELLOW}stats: {B}HP: {team[i-1].HP[0]} / MANA: {team[i-1].Mana[0]} / STAMINA: {team[i-1].Stamina[0]} \n")
            
            time.sleep(0.5)
            print(f"\n{GRAY} [ BATTLE STATS ]\n")
            time.sleep(0.5)
            print(f"{B}  - 1 ) {Fore.YELLOW}total turns: {B}{First_Turn}\n")
            time.sleep(0.5)
            print(f"{B}  - 2 ) {Fore.YELLOW}enemies killed: {B}{len(enemyT)-len(GlobalTempEnemyTeam)}")
            time.sleep(1.5)
            
            print(f"\n{B}Press any key to continue..\n")
            os.system('pause > null')
            break
            
    play_music("Audio_Assets/Soundtrack/menu.wav", -1)
    return

def Who_Starts():
    global GlobalTempTeam
    global GlobalTempEnemyTeam
    
    optionsW = ['You','They']
    W_enemy = 0.5
    W_team = 0.5
    
    for member in GlobalTempTeam.values():
        if W_enemy >= 0.2 and W_team >= 0.2:
            if member.Ability in Rapid_List:
                W_team += 0.2
                W_enemy -= 0.2
            elif member.Ability in Slow_List:
                W_team -= 0.2
                W_enemy += 0.2
            if member.Weapon.type in Rapid_List:
                W_team += 0.1
                W_enemy -= 0.1
            elif member.Weapon.type in Slow_List:
                W_team -= 0.1
                W_enemy += 0.1
        else:
            continue
            
    for member in GlobalTempEnemyTeam.values():
        if W_enemy >= 0.2 and W_team >= 0.2:
            if member.Ability in Rapid_List:
                W_team -= 0.2
                W_enemy += 0.2
            elif member.Ability in Slow_List:
                W_team += 0.2
                W_enemy -= 0.2
            if member.Weapon.type in Rapid_List:
                W_team -= 0.1
                W_enemy += 0.1
            elif member.Weapon.type in Slow_List:
                W_team += 0.1
                W_enemy -= 0.1
        else:
            continue
        
    W_enemy = round(W_enemy, 2)
    W_team = round(W_team, 2)

    if random.choices(optionsW,weights=[W_team,W_enemy],k=1)[0] == 'You':
        return [0,W_enemy,W_team]
    else:
        return [1,W_enemy,W_team]

def Print_Combat(PC_team_name, CCT):
    global GlobalTempTeam, GlobalTempEnemyTeam

    if PC_team_name == "GlobalTempTeam":
        PC_team = GlobalTempTeam
    elif PC_team_name == "GlobalTempEnemyTeam":
        PC_team = GlobalTempEnemyTeam
    else:
        print("Errore: nome del team non valido!")
        return CCT

    if any(key.split("_")[1] == "member" for key in PC_team.keys()):
        PC_teamTitle = "YOUR TEAM"
        PC_teamColor = TEAM_COLOR
    else:
        PC_teamTitle = "ENEMY TEAM"
        PC_teamColor = ENEMY_COLOR

    if CCT % 2 == 1:
        PC_teamSpace = ""
    else:
        PC_teamSpace = "\t\t"

    print(f"{PC_teamSpace}{GRAY} [ {PC_teamColor}{PC_teamTitle} {GRAY}] ____________________________\n{PC_teamSpace} |")
    
    for idx, member in PC_team.items():
        HP_Color = Fore.RED if member.HP[0] <= 30 else Fore.GREEN
        ARMOR_Color = GRAY if member.Armor.armor[0] <= 0 else Fore.BLUE
        Mana_Color = Fore.RED if member.Mana[0] <= 10 else Fore.CYAN
        Stamina_Color = Fore.RED if member.Stamina[0] <= 10 else Fore.YELLOW
        
        if member.Weapon.type == "Bow":
            print(f"{PC_teamSpace}{GRAY} |  {B}[{GRAY}{idx.split('_')[0]}{B}] {GRAY}{member.Name} {B}| HP/ARMOR: {HP_Color}{int(member.HP[0])}{B}/{ARMOR_Color}[{int(member.Armor.armor[0])}] {B}MANA: {Mana_Color}{member.Mana[0]} {B}STAMINA: {Stamina_Color}{member.Stamina[0]} {B}/ {GRAY}{member.Weapon.name}({member.Weapon.ammo.name})")
        else:
            print(f"{PC_teamSpace}{GRAY} |  {B}[{GRAY}{idx.split('_')[0]}{B}] {GRAY}{member.Name} {B}| HP/ARMOR: {HP_Color}{int(member.HP[0])}{B}/{ARMOR_Color}[{int(member.Armor.armor[0])}] {B}MANA: {Mana_Color}{member.Mana[0]} {B}STAMINA: {Stamina_Color}{member.Stamina[0]} {B}/ {GRAY}{member.Weapon.name}")
    
    print(f"{GRAY}{PC_teamSpace} |_______________________________|")

    CCT += 1
    return CCT

def EnemyCombat_AI(Who_Start, First_Turn):
    global GlobalTempEnemyTeam
    global GlobalTempTeam
    ability_print = [0,0]
    CombatCT = 1
    EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
    TeamTotHP = sum(member.HP[0] for member in GlobalTempTeam.values())
    CharacterSelectedList = GlobalTempEnemyTeam.copy()

    if First_Turn == 1:
        stats_mess = f"{STATS_COLOR} [ THE ENEMY TEAM STARTS FIRST ][ {STATS_COLOR2}Velocity Weights:{STATS_COLOR} ENEMY: {Who_Start[1]} TEAM: {Who_Start[2]} ]\n"
    else:
        stats_mess = f"{STATS_COLOR} [ IT'S THE TURN OF THE ENEMY ]\n"

    while TeamTotHP > 0 and EnemyTotHP > 0 and CharacterSelectedList:
        if not CharacterSelectedList:
            break  
        
        print(f"\n{B}|========================================================================|\n")
        print(stats_mess)
        CombatCT = Print_Combat("GlobalTempEnemyTeam", CombatCT)
        print("\n")
        CombatCT = Print_Combat("GlobalTempTeam", CombatCT)

        if CharacterSelectedList:
            NS = max(CharacterSelectedList, key=lambda x: CharacterSelectedList[x].Mana[0] + CharacterSelectedList[x].Stamina[0])
            Enemy_Selected = CharacterSelectedList[NS]
        else:
            print("No characters left in the enemy team.")
            return 3

        if GlobalTempTeam:
            T = min(GlobalTempTeam, key=lambda x: GlobalTempTeam[x].HP[0])
            Target = GlobalTempTeam[T]
        else:
            print("No characters left in your team.")
            return 2

        print(f"\n{STATS_COLOR}[ ENEMY SELECTED: {STATS_COLOR2}{Enemy_Selected.Name.upper()}{STATS_COLOR} ][ TARGET SELECTED: {STATS_COLOR2}{Target.Name.upper()}{STATS_COLOR} ]\n")
        time.sleep(2)
        
        if Enemy_Selected.Weapon.type == "Magical":
            if Enemy_Selected.Mana[0] >= Enemy_Selected.Weapon.mana:
                Enemy_Selected.Mana[0] -= Enemy_Selected.Weapon.mana
            else:
                print(f"{STATS_COLOR}[ THE ENEMY HAD NOT ENOUGH MANA TO ATTACK ]\n")
                time.sleep(2)
                del CharacterSelectedList[NS]
                print(f"{B}As soon as you're ready, press any key..\n")
                os.system('pause > null')
                continue
        else:
            if Enemy_Selected.Stamina[0] >= Enemy_Selected.Weapon.stamina:
                Enemy_Selected.Stamina[0] -= Enemy_Selected.Weapon.stamina
            else:
                print(f"{STATS_COLOR}[ THE ENEMY HAD NOT ENOUGH STAMINA TO ATTACK ]\n")
                time.sleep(2)
                del CharacterSelectedList[NS]
                print(f"{B}As soon as you're ready, press any key..\n")
                os.system('pause > null')
                continue
        
        if Enemy_Selected.Weapon.velocity < 3:
            hit_modifier = 1 - (3 - Enemy_Selected.Weapon.velocity) * 0.1
        else:
            hit_modifier = 1 + (Enemy_Selected.Weapon.velocity - 3) * 0.1

        if Enemy_Selected.Ability == "Archer" and Enemy_Selected.Weapon.type == "Bow":
            P_Weight1 = Enemy_Selected.Weapon.precision + 0.2
        else:
            P_Weight1 = Enemy_Selected.Weapon.precision
        P_Weight2 = 1 - Enemy_Selected.Weapon.precision
        
        Velocity_Weight1 = round(P_Weight1 * hit_modifier,2)
        Velocity_Weight2 = round(P_Weight2,2)

        Precision_Weights = [Velocity_Weight1, Velocity_Weight2]
        
        if "hit" == random.choices(["hit","miss"],weights=Precision_Weights,k=1)[0]:
            damage = 1
            mxp = 1
            weaponSound(Enemy_Selected.Weapon.type)

            if Enemy_Selected.Ability == "Rapid":
                if "hit" == random.choices(["hit","miss"],weights=Precision_Weights,k=1)[0]:
                    ability_print = [f"{STATS_COLOR}[ABILITY] {B}-{STATS_COLOR} [ '{STATS_COLOR2}RAPID{STATS_COLOR}' - {Enemy_Selected.Name.upper()} ATTACKED TWICE ]\n",1]
                    mxp *= 2
                    damage = (Enemy_Selected.Weapon.damage * mxp)
                else:
                    ability_print = [0,0]
                    mxp *= 1
                    damage = (Enemy_Selected.Weapon.damage * mxp)
            elif Target.Ability == "Shield" and Enemy_Selected.Ability == "Rapid":
                mxp *= 1.6
                damage = (Enemy_Selected.Weapon.damage * mxp)
            elif Target.Ability == "Shield":
                mxp *= 0.8
                damage = (Enemy_Selected.Weapon.damage * mxp)
            else:
                damage = (Enemy_Selected.Weapon.damage * mxp)
            
            damage * hit_modifier
            round(damage,2)

            for fnx in Target.TAG_Effect:
                if fnx.duration[0] != 0:
                    match fnx.name:
                        case "Resistance":
                            damage *= (1 - 20 / 100)
                        
                        case "Frost":
                            damage *= 1.2
            
            round(damage,2)

            prnt = f"{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ THE ENEMY HITS YOU ][ {STATS_COLOR2}damage: {Fore.RED}-{damage}{B} - {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{Enemy_Selected.Weapon.mana}{B}/{Fore.YELLOW}-{Enemy_Selected.Weapon.stamina}{STATS_COLOR} ]\n"
            if ability_print[1] != 0:
                print(ability_print[0])
            print(prnt)

            if damage < 0:
                damage = 0

            if Enemy_Selected.Weapon.type == "Bow" and Enemy_Selected.Weapon.ammo.effect != "none":
                for i in Target.TAG_Effect:
                    if i.name == Enemy_Selected.Weapon.ammo.effect:
                        Target.TAG_Effect.duration[0] = Target.TAG_Effect.duration[1]

            if Target.Armor.armor[0] > 0:
                if Target.Armor.armor[0] >= damage:
                    Target.Armor.armor[0] -= damage
                else:
                    damage -= Target.Armor.armor[0]
                    Target.Armor.armor[0] = 0
                    Target.HP[0] -= damage
                
            else:
                Target.HP[0] -= damage

            if Target.HP[0] <= 0:
                print(f"{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ {STATS_COLOR2}{Target.Name.upper()} WAS DEFEATED {STATS_COLOR}]\n")
                time.sleep(2)
                del GlobalTempTeam[T]
                del CharacterSelectedList[NS]
                print(f"{B}As soon as you're ready, press any key..\n")
                os.system('pause > null')
                continue

            print(f"{B}As soon as you're ready, press any key..\n")
            os.system('pause > null')

        else:
            print(f"{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ THE ENEMY MISSED YOU ][ {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{Enemy_Selected.Weapon.mana}{B}/{Fore.YELLOW}-{Enemy_Selected.Weapon.stamina}{STATS_COLOR} ]\n")
            time.sleep(2)
            del CharacterSelectedList[NS]
            print(f"{B}As soon as you're ready, press any key..\n")
            os.system('pause > null')
            continue
            
        EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
        TeamTotHP = sum(member.HP[0] for member in GlobalTempTeam.values())
 
        del CharacterSelectedList[NS]
        continue

    if TeamTotHP > 0 and EnemyTotHP > 0:
        print(f"\n{B}|========================================================================|\n")
        RegenEffect()
        print(f"{Fore.CYAN} [ TURN SUMMARY ][ MANA / STAMINA HAVE BEEN REGENERATED]\n")
        CombatCT = Print_Combat("GlobalTempEnemyTeam", CombatCT)
        print("\n")
        CombatCT = Print_Combat("GlobalTempTeam", CombatCT)
        print(f"\n{B}Press any key to continue..\n")
        os.system('pause > null')
        return 0
    elif TeamTotHP <= 0:
        return 2
    elif EnemyTotHP <= 0:
        return 3

def PlayerCombat(Who_Start,First_Turn):
    global GlobalTempEnemyTeam
    global GlobalTempTeam
    CombatCT = 1
    TeamTotHP = 0
    EnemyTotHP = 0
    CharacterSelectedList = GlobalTempTeam.copy()

    if First_Turn == 1:
        stats_mess = [f"{STATS_COLOR} [ YOUR TEAM STARTS FIRST ][ {STATS_COLOR2}Velocity Weights:{STATS_COLOR} ENEMY: {Who_Start[1]} TEAM: {Who_Start[2]} ]\n"]
    else:
        stats_mess = [f"{STATS_COLOR} [ IT'S YOUR TURN ]\n"]

    for member in GlobalTempTeam.values():
        TeamTotHP += member.HP[0]
    for member in GlobalTempEnemyTeam.values():
        EnemyTotHP += member.HP[0]

    while TeamTotHP > 0 and EnemyTotHP > 0 and CharacterSelectedList:
        print(f"\n{B}|========================================================================|\n")
        try:
            print(stats_mess[1])
            print(stats_mess[0])
        except:
            print(stats_mess[0])

        CombatCT = Print_Combat("GlobalTempTeam",CombatCT)
        print("\n")
        CombatCT = Print_Combat("GlobalTempEnemyTeam",CombatCT)

        print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}character select {STATS_COLOR}] {B} ==>",end="")
        for keys,values in CharacterSelectedList.items():
            print(f" {STATS_COLOR} '{ORANGE}{keys.split('_')[0]}{STATS_COLOR}' {B}-{STATS_COLOR} {values.Name} |",end="")
        print(f" {STATS_COLOR}'{ORANGE}4{STATS_COLOR}' {B}-{Fore.RED} Escape",end="")
        
        while TeamTotHP > 0 and EnemyTotHP > 0 and CharacterSelectedList:
            if CharacterSelectedList:
                Character_Selected = input(f"\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
            else:
                return 2
            if any(Character_Selected == key.split("_")[0] for key in CharacterSelectedList.keys()) or Character_Selected == "4":
                if Character_Selected == "1":
                    del CharacterSelectedList["1_member"]
                    stats_mess = CombatMove("1_member",CombatCT)
                    EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
                    break
                elif Character_Selected == "2":
                    del CharacterSelectedList["2_member"]
                    stats_mess = CombatMove("2_member",CombatCT)
                    EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
                    break
                elif Character_Selected == "3":
                    del CharacterSelectedList["3_member"]
                    stats_mess = CombatMove("3_member",CombatCT)
                    EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
                    break
                elif Character_Selected == "4":
                    return 4
            else:
                exception("You must enter a valid numeric value.")
                continue
    
    if TeamTotHP > 0 and EnemyTotHP > 0:
        print(f"\n{B}|========================================================================|\n")
        try:
            print(stats_mess[1])
            print(stats_mess[0])
        except:
            print(stats_mess[0])

        RegenEffect()
        print(f"{Fore.CYAN} [ TURN SUMMARY ][ MANA / STAMINA HAVE BEEN REGENERATED]\n")
        CombatCT = Print_Combat("GlobalTempTeam",CombatCT)
        print("\n")
        CombatCT = Print_Combat("GlobalTempEnemyTeam",CombatCT)
        CharacterSelectedList = GlobalTempTeam.copy()
        print(f"\n{B}Press any key to continue..\n")
        os.system('pause > null')
        return 1
    elif TeamTotHP <= 0:
        return 2
    elif EnemyTotHP <= 0:
        return 3

def Player_Combat_Inventory(Team_Member,CombatCT):
    global GlobalTempEnemyTeam
    global GlobalTempTeam
    os.system('cls')
    print("\n"+Fore.RED + Style.BRIGHT + (ascii_art := pyfiglet.figlet_format("battle")),end="")
    print(f"\n{B}|========================================================================|\n")
    print(f"{STATS_COLOR}[ {STATS_COLOR2}{GlobalTempTeam[Team_Member].Name.upper()}{STATS_COLOR} OPENED THE INVENTORY {STATS_COLOR}]\n")
    CombatCT = Print_Combat("GlobalTempTeam",CombatCT)
    print("\n")
    CombatCT = Print_Combat("GlobalTempEnemyTeam",CombatCT)
    
    while True:
        print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}inv. menu{STATS_COLOR} ]  {B}==> {STATS_COLOR}[ {ORANGE}1{STATS_COLOR} ] = {B}CHANGE WEAPON | {STATS_COLOR}[ {ORANGE}2{STATS_COLOR} ] = {B}POTIONS ",end="")
        if GlobalTempTeam[Team_Member].Weapon.type == "Bow":
            print(f"{B}| {STATS_COLOR}[ {ORANGE}3{STATS_COLOR} ] = {B}CHANGE ARROW {B}| {STATS_COLOR}[ {ORANGE}4{STATS_COLOR} ] = {B}EXIT")
        else:
            print(F"{B}| {STATS_COLOR}[ {ORANGE}3{STATS_COLOR} ] = {B}EXIT")
        Choice_Select = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        
        if Choice_Select == "1":
            if Inventory["WEAPON_AND_EQUIP"]["Weapon"]:
                print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the weapon{STATS_COLOR} ]  {B}==> ",end="")
                for idx,i in enumerate(Inventory["WEAPON_AND_EQUIP"]["Weapon"],start=1):
                    Weapon = list(i.values())[0].name
                    print(f" {STATS_COLOR}[ {ORANGE}{idx} {STATS_COLOR}= {B}{Weapon.upper()} ({list(i.values())[0].count}){STATS_COLOR}]",end="")
                    if idx%3 == 0:
                        print("\n ",end="")

                while True:
                    Weapon_Select = input(f"\n\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                            
                    try:
                        if Inventory["WEAPON_AND_EQUIP"]["Weapon"][int(Weapon_Select)-1]:
                            Inventory_Insert(GlobalTempTeam[Team_Member].Weapon,"Weapon")
                            GlobalTempTeam[Team_Member].Weapon = list(Inventory["WEAPON_AND_EQUIP"]["Weapon"][int(Weapon_Select)-1].values())[0]
                            Inventory_Remove(list(Inventory["WEAPON_AND_EQUIP"]["Weapon"][int(Weapon_Select)-1].values())[0],"Weapon")
                            
                            print(f"\n{STATS_COLOR}  [INFO STATS] {B}-{STATS_COLOR} [ {Fore.GREEN}WEAPON CHANGED{STATS_COLOR} ]\n")
                            print(f"{B}press any key to continue\n")
                            os.system('pause > null')
                            break
                        else:
                            exception(f"You must enter a valid numeric value")
                            continue
                    except Exception as e:
                        print(f"Exception Type: {type(e).__name__}")
                        print(f"Error Message: {str(e)}")
                        print("Stack Trace:")
                        print(traceback.format_exc())
                        os.system('pause')

            else:
                print(f"{W}\n  [ {DARKRED}info{Fore.WHITE} ] = you have no other weapons\n\n")
                print(f"{B}press any key to continue\n")
                os.system('pause > null')

        elif Choice_Select == "2":
            if Inventory["POTION_AND_FOOD"]["Potion"]:
                print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the potion{STATS_COLOR} ]  {B}==> ",end="")
                for idx,i in enumerate(Inventory["POTION_AND_FOOD"]["Potion"],start=1):
                    Potion_or_Food = list(i.values())[0].name
                    print(f" {STATS_COLOR}[ {ORANGE}{idx} {STATS_COLOR}= {B}{Potion_or_Food.upper()} ({list(i.values())[0].count}){STATS_COLOR}]",end="")
                    if idx%3 == 0:
                        print("\n ",end="")
                
                while True:
                    Potion_or_Food_Select = input(f"\n\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                    
                    try:
                        if Inventory["POTION_AND_FOOD"]["Potion"][int(Potion_or_Food_Select)-1]:
                            
                            PG = GlobalTempTeam[Team_Member]
                            Potion = list(Inventory["POTION_AND_FOOD"]["Potion"][int(Potion_or_Food_Select)-1].values())[0]

                            if PG.HP[0] < PG.HP[1]:
                                PG.HP[0] = min(PG.HP[0] + Potion.mod_hp, PG.HP[1])
                            if PG.Mana[0] < PG.Mana[1]:
                                PG.Mana[0] = min(PG.Mana[0] + Potion.mod_mana, PG.Mana[1])
                            if PG.Stamina[0] < PG.Stamina[1]:
                                PG.Stamina[0] = min(PG.Stamina[0] + Potion.mod_stamina, PG.Stamina[1])
                            if Potion.effect != "NB":
                                for fnx in PG.TAG_Effect:
                                    if Potion.effect == fnx.name:
                                        fnx.duration[0] = fnx.duration[1]
                            
                            CheckPotion = Inventory_Check(Potion.name,"Potion")
                            Inventory_Remove(Potion,"Potion")

                            print(f"\n{STATS_COLOR}  [INFO STATS] {B}-{STATS_COLOR} [ {Fore.GREEN}POTION USED{STATS_COLOR} ]\n")
                            print(f"{B}press any key to continue\n")
                            os.system('pause > null')
                            break

                        else:
                            exception(f"You must enter a valid numeric value")
                            continue
                    except Exception as e:
                        print(f"Exception Type: {type(e).__name__}")
                        print(f"Error Message: {str(e)}")
                        print("Stack Trace:")
                        print(traceback.format_exc())
                        os.system('pause')

            else:
                print(f"{W}\n  [ {DARKRED}info{Fore.WHITE} ] = you have no other potions or foods\n")
                print(f"{B}press any key to continue\n")
                os.system('pause > null')

        elif GlobalTempTeam[Team_Member].Weapon.type == "Bow" and Choice_Select == "3":
            if Inventory["ARROWS"]:
                print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the arrow{STATS_COLOR} ]  {B}==> ",end="")
                for idx,i in enumerate(Inventory["ARROWS"],start=1):
                    Arrow = list(i.values())[0].name
                    print(f" {STATS_COLOR}[ {ORANGE}{idx} {STATS_COLOR}= {B}{Arrow.upper()} ({list(i.values())[0].count}){STATS_COLOR}]",end="")
                    if idx%3 == 0:
                        print("\n ",end="")
                    
                while True:
                    Arrow_Select = input(f"\n\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()

                    try:
                        if Inventory["ARROWS"][int(Arrow_Select)-1]:
                            GlobalTempTeam[Team_Member].Weapon.ammo = list(Inventory["ARROWS"][int(Arrow_Select)-1].values())[0]
                            
                            print(f"\n{STATS_COLOR}  [INFO STATS] {B}-{STATS_COLOR} [ {Fore.GREEN}ARROW CHANGED{STATS_COLOR} ]\n")
                            print(f"{B}press any key to continue\n")
                            os.system('pause > null')
                            break
                        else:
                            exception(f"You must enter a valid numeric value")
                            continue
                    except Exception as e:
                        print(f"Exception Type: {type(e).__name__}")
                        print(f"Error Message: {str(e)}")
                        print("Stack Trace:")
                        print(traceback.format_exc())
                        os.system('pause')

            else:
                print(f"{W}\n  [ {DARKRED}info{Fore.WHITE} ] = you have no other arrows\n\n")
                print(f"{B}press any key to continue\n")
                os.system('pause > null')
                break
        
        elif GlobalTempTeam[Team_Member].Weapon.type == "Bow" and Choice_Select == "4":
            break
        elif GlobalTempTeam[Team_Member].Weapon.type != "Bow" and Choice_Select == "3":
            break
        else:
            exception(f"You must enter a valid numeric value")
            continue

    return [f"{STATS_COLOR}[ INVENTORY CLOSED ]\n"]

def CombatMove(Team_Member,CombatCT):
    global GlobalTempEnemyTeam
    global GlobalTempTeam
    PG = GlobalTempTeam[Team_Member]
    
    stats_effect = f"{STATS_COLOR}[EFFECTS STATS]"
    Buff_Effects = 0
    Debuff_Effects = 0

    for efx in PG.TAG_Effect:
        efx.update_duration()
        if efx.duration[0] != 0:
            stats_effect += f" {B}- {STATS_COLOR}[ {GRAY}name: {Fore.RED}{efx.name.upper()} {GRAY}({ORANGE}{efx.duration[0]}{GRAY}) {STATS_COLOR}]"

        if efx.duration[0] != 0 and efx.buff_efx != 0:
            match efx.name:
                case "Regen":
                    if PG.HP[0] < PG.HP[1]:
                        PG.HP[0] = min(PG.HP[0] + efx.buff_efx, PG.HP[1])
                
                case _:
                    Buff_Effects += efx.buff_efx
                
        if efx.duration[0] != 0 and efx.debuf_efx != 0:
            match efx.name:
                case "Resistance":
                    pass
                
                case "Poison":
                    return_efx = 2*efx.duration[0]
                    Debuff_Effects += return_efx

                case "Potent Poison":
                    return_efx = 4*efx.duration[0]
                    Debuff_Effects += return_efx

                case _:
                    Debuff_Effects += efx.debuf_efx

    while True:
        print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}actions menu{STATS_COLOR} ]  {B}==> {STATS_COLOR}[ {ORANGE}1{STATS_COLOR} ] = {B}ATTACK | {STATS_COLOR}[ {ORANGE}2{STATS_COLOR} ] = {B}ITEMS ")
        Choice_Select = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        
        if Choice_Select == "2":
            stats_mess = Player_Combat_Inventory(Team_Member,CombatCT)
            break
            
        elif Choice_Select == "1":
            ability_print = [0,0]
            while True:
                print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the enemy to hit {STATS_COLOR}] {B} ==>",end="")
                for keys,values in enumerate(list(GlobalTempEnemyTeam.values()),start=1):
                    print(f" {STATS_COLOR} '{ORANGE}{keys}{STATS_COLOR}' - {values.Name} |",end="")

                Enemy_Selected = input(f"\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                if Enemy_Selected.isdigit() and int(Enemy_Selected) in range(1, len(GlobalTempEnemyTeam) + 1):
                    selected_enemy = list(GlobalTempEnemyTeam.items())[int(Enemy_Selected) - 1]

                    if PG.Weapon.type == "Bow" and not Inventory["ARROWS"]:
                        stats_mess = [f"\n{STATS_COLOR}[ YOU DON'T HAVE ENOUGH {STATS_COLOR2}ARROW {STATS_COLOR}]\n",stats_effect]
                        break
                        
                    if PG.Weapon.type == "Magical" or PG.Weapon.name == "Arcane Bow":
                        if PG.Mana[0] >= PG.Weapon.mana:
                            PG.Mana[0] -= PG.Weapon.mana
                        else:
                            stats_mess = [f"\n{STATS_COLOR}[ YOU DON'T HAVE ENOUGH MANA ][ {STATS_COLOR2}mana:{STATS_COLOR} YOUR MANA: {PG.Mana[0]} MANA REQUIRED: {PG.Weapon.mana} ]\n",stats_effect]
                            break
                    else:
                        if PG.Stamina[0] >= PG.Weapon.stamina:
                            PG.Stamina[0] -= PG.Weapon.stamina
                        else:
                            stats_mess = [f"\n{STATS_COLOR}[ YOU DON'T HAVE ENOUGH STAMINA ][ {STATS_COLOR2}stamina:{STATS_COLOR} YOUR STAMINA: {PG.Stamina[0]} STAMINA REQUIRED: {PG.Weapon.stamina} ]\n",stats_effect]
                            break
                    
                    
                    if PG.Weapon.velocity < 3:
                        hit_modifier = 1 - (3 - PG.Weapon.velocity) * 0.1
                    else:
                        hit_modifier = 1 + (PG.Weapon.velocity - 3) * 0.1

                    if PG.Ability == "Archer" and PG.Weapon.type == "Bow":
                        P_Weight1 = PG.Weapon.precision + 0.2
                    else:
                        P_Weight1 = PG.Weapon.precision
                    P_Weight2 = 1 - PG.Weapon.precision

                    Velocity_Weight1 = round(P_Weight1 * hit_modifier,2)
                    Velocity_Weight2 = round(P_Weight2,2)

                    Precision_Weights = [Velocity_Weight1, Velocity_Weight2]
                    
                    if PG.Weapon.type == "Bow":
                        Arrow_Equip = PG.Weapon.ammo.name 
                        CheckArrow = Inventory_Check(Arrow_Equip,"ARROW")
                        if CheckArrow.count == 0:
                            Inventory_Remove(Arrow_Equip,"ARROW")
                        elif CheckArrow.count > 0:
                            CheckArrow.count -= 1

                    if "hit" == random.choices(["hit","miss"],weights=Precision_Weights,k=1)[0]:
                        damage = 1
                        mxp = 1
                        weaponSound(GlobalTempTeam[Team_Member].Weapon.type)

                        if PG.Ability == "Rapid":
                            if "hit" == random.choices(["hit","miss"],weights=Precision_Weights,k=1)[0]:
                                ability_print = [f"\n{STATS_COLOR}[ABILITY] {B}-{STATS_COLOR} [ '{STATS_COLOR2}RAPID{STATS_COLOR}' - {GlobalTempTeam[Team_Member].Name.upper()} ATTACKED TWICE ]\n",1]
                                mxp *= 2
                                damage = (PG.Weapon.damage * mxp)
                            else:
                                ability_print = [0,0]
                                mxp *= 1
                                damage = (PG.Weapon.damage * mxp)
                        elif selected_enemy[1].Ability == "Shield" and PG.Ability == "Rapid":
                            mxp *= 1.6
                            damage = (PG.Weapon.damage * mxp)
                        elif selected_enemy[1].Ability == "Shield":
                            mxp *= 0.8
                            damage = (PG.Weapon.damage * mxp)
                        else:
                            damage = (PG.Weapon.damage * mxp)

                        damage * hit_modifier
                        round(damage,2)

                        for fnx in selected_enemy[1].TAG_Effect:
                            if fnx.duration[0] != 0:
                                match fnx.name:
                                    case "Resistance":
                                        damage *= (1 - 20 / 100)
                                    
                                    case "Frost":
                                        damage *= 1.2
                        
                        round(damage,2)
                        damage += Buff_Effects

                        prnt = f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ ENEMY SUCCESSFULLY HIT ][ {STATS_COLOR2}damage: {Fore.RED}-{damage}{B} - {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{PG.Weapon.mana}{B}/{Fore.YELLOW}-{PG.Weapon.stamina}{STATS_COLOR} ]\n"
                        if ability_print[1] != 0:
                            prnt += ability_print[0]
                        stats_mess = [prnt,stats_effect]
                        if damage < 0:
                            damage = 0

                        if PG.Weapon.type == "Bow" and PG.Weapon.ammo.effect != "none":
                            for i in PG.TAG_Effect:
                                if i.name == PG.Weapon.ammo.effect:
                                     selected_enemy[1].TAG_Effect.duration[0] =  selected_enemy[1].TAG_Effect.duration[1]

                        if selected_enemy[1].Armor.armor[0] > 0:
                            if selected_enemy[1].Armor.armor[0] >= damage:
                                selected_enemy[1].Armor.armor[0] -= damage
                            else:
                                damage -= selected_enemy[1].Armor.armor[0]
                                selected_enemy[1].Armor.armor[0] = 0
                                selected_enemy[1].HP[0] -= damage
                            
                        else:
                            selected_enemy[1].HP[0] -= damage
                        
                        if selected_enemy[1].HP[0] <= 0:
                            del GlobalTempEnemyTeam[selected_enemy[0]]
                            stats_mess = [f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ ENEMY SUCCESSFULLY HIT ][ {STATS_COLOR2}damage: {Fore.RED}-{damage}{B} - {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{PG.Weapon.mana}{B}/{Fore.YELLOW}-{PG.Weapon.stamina}{STATS_COLOR} ]\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ {STATS_COLOR2}YOU HAVE DEFEATED THE ENEMY {STATS_COLOR}]\n",stats_effect]

                        break

                    else:
                        stats_mess = [f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ YOU MISSED THE ENEMY ][{STATS_COLOR2}mana/stamina: {Fore.CYAN}-{GlobalTempTeam[Team_Member].Weapon.mana}{B}/{Fore.YELLOW}-{GlobalTempTeam[Team_Member].Weapon.stamina}{STATS_COLOR} ]\n",stats_effect]
                        break

                else:
                    exception(f"You must enter a numeric value between 1 and {len(GlobalTempEnemyTeam)}")
                    continue
            break
        
        else:
            exception(f"You must enter a valid numeric value")
            continue
    
    PG.HP[0] -= Debuff_Effects

    if PG.HP[0] <= 0:
        print(f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ {STATS_COLOR2}{PG.Name.upper()} WAS DEFEATED by effects {STATS_COLOR}]\n")
        time.sleep(2)
        del GlobalTempTeam[Team_Member]
        print(f"{B}As soon as you're ready, press any key..\n")
        os.system('pause > null')

    return stats_mess

def RegenEffect():
    global GlobalTempEnemyTeam
    global GlobalTempTeam

    for Value in GlobalTempTeam.values():
        RGV_mana = 5
        RGV_stamina = 5 
        
        if Value.Ability == "Magic":
            RGV_mana = 10
        elif Value.Ability == "Brute":
            RGV_stamina = 10

        if Value.Mana[0] < Value.Mana[1]:
            Value.Mana[0] = min(Value.Mana[0] + RGV_mana, Value.Mana[1])

        if Value.Stamina[0] < Value.Stamina[1]:
            Value.Stamina[0] = min(Value.Stamina[0] + RGV_stamina, Value.Stamina[1])

    for Value in GlobalTempEnemyTeam.values():
        RGV_mana = 5
        RGV_stamina = 5
        
        if Value.Ability == "Magic":
            RGV_mana = 10
        elif Value.Ability == "Brute":
            RGV_stamina = 10
            
        if Value.Mana[0] < Value.Mana[1]:
            Value.Mana[0] = min(Value.Mana[0] + RGV_mana, Value.Mana[1])
            
        if Value.Stamina[0] < Value.Stamina[1]:
            Value.Stamina[0] = min(Value.Stamina[0] + RGV_stamina, Value.Stamina[1])
    return

    

#####################################################
# MENU & STORY

def exception(text):
    print(f"{W}\n  [ {DARKRED}error{Fore.WHITE} ] = Input Not Valid! -{Fore.RED}{Style.BRIGHT} {text}\n\n")
    for sec in range(2,0,-1):
        print(f"{B}{str(sec)}.",end=" ")
        time.sleep(1)
    print(f"{B}press any key to continue\n")
    os.system('pause > null')

def create_menu(title_menu,list_title,end):
    os.system('cls')
    print(Fore.CYAN + Style.NORMAL + (ascii_art := pyfiglet.figlet_format("Dawn of Elvaria")))
    print(f"{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ {title_menu.upper()} ]\n")
    number = 1
    for title in list_title:
        print(f"{W}  [ {ORANGE}{number}{Fore.WHITE} ] -  {Fore.YELLOW}{title}\n")
        number += 1
    print(f"{W}  [ {ORANGE}{number}{Fore.WHITE} ] -  {Fore.RED}{end.upper()}\n")
    print(f"{B}|========================================================================|\n\n")

#####################################################
#PROGRAM
debugmode = 0
play_music("Audio_Assets/Soundtrack/menu.wav", -1)
os.system('cls')
while True:
    create_menu("main menu",["The Journey Begins (start game)","Consult the Codex (characters)","The Scholar Tome (game guide)"],"exit")
    Main_Menu = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
    match Main_Menu:
        case "1":
            if len(CL) >= 3:
                Team = CreateTeam()
                try:
                    if len(Team) >= 3:
                        EnemyList = [CreateEnemy(Goblin_Archer),
                                    CreateEnemy(Goblin_Shaman),
                                    CreateEnemy(Goat)]
                        start_combat(Team,EnemyList)
                        continue
            
                except Exception as e:
                    if debugmode == 1:
                        print(f"Exception Type: {type(e).__name__}")
                        print(f"Error Message: {str(e)}")
                        print("Stack Trace:")
                        print(traceback.format_exc())
                        print("Debugging Information:")
                        #ricorda che puoi cambiarlo a seconda della funzione interessata
                        print(f"GlobalTempEnemyTeam: {GlobalTempEnemyTeam}")
                        os.system('pause')
                        continue
                    else:
                        continue
            else:
                exception("You don't have enough characters - Go to Codex")
                continue

        case "2":
            while True:
                create_menu("codex menu",["Create a Character","list of characters","Inventory"],"back")
                Secondary_Menu = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                match Secondary_Menu:
                    case "1":
                        os.system('cls')
                        Creation()
                        continue 
                    case "2":
                        os.system('cls')
                        View()
                    case "3":
                        os.system('cls')
                        Open_Inventory()
                    case "4":
                        os.system('cls')
                        break
                    case _:
                        exception("You must enter a numeric value between 1 and 4.")

        case "3":
            exception("NON L'HO ANCORA FATTO")
        case "4":
            break

        #DEBUG MENU AND MODE
        case "DEBUG":
            debugmode = 1
            while True:
                debug = input(f"\n\n{B}[ {Fore.RED}1 {B}] {GRAY}- {DARKRED}CREATE SIX RANDOM CHARACTERS\n{B}[ {Fore.RED}2 {B}] {GRAY}- {DARKRED}ADD ALL POTIONS\n{B}[ {Fore.RED}3 {B}] {GRAY}- {DARKRED}ADD TEN RANDOM WEAPONS\n{B}[ {Fore.RED}4 {B}] {GRAY}- {DARKRED}ADD ALL ARROWS\n{B}[ {Fore.RED}5 {B}] {GRAY}- {DARKRED}ADD TEN RANDOM ARMORS\n{B}[ {Fore.RED}6 {B}] {GRAY}- {DARKRED}DISABLE DEBUGMODE\n{B}[ {Fore.RED}7 {B}] {GRAY}- {DARKRED}EXIT\n {Fore.RED}>>> {Fore.GREEN}")
                match debug:
                    case "1":
                        for i in range(1,7):
                            CI[str(i)+"° Hero"] = Character(Name=str(i)+"° Hero",Race=random.choice(RaceList),Gender="UK",Age="2000",Weapon=random.choice(All_Weapons),Armor=random.choice(All_Armors))
                            CL.append(str(i)+"° Hero")
                        print(f"\n\n{Fore.CYAN}Created. {B}- Go to the Codex to see the result")
                        os.system('pause')
                            
                    case "2":
                        for i in Potions_List:
                            Inventory_Insert(i,"potion")
                        
                        print(f"\n\n{Fore.CYAN}Created. {B}- result:")
                        print("\n")
                        for potion in Inventory["POTION_AND_FOOD"]["Potion"]:
                            for arrow_name, arrow in potion.items():
                                print(f"> {GRAY}Nome: {DARKRED}{arrow.name}")

                        print("\n\n")
                        os.system('pause')
                    
                    case "3":
                        for n in range(1,11):
                            Inventory_Insert(random.choice(All_Weapons),"weapon")
                        
                        print(f"\n\n{Fore.CYAN}Created. {B}- result:")
                        print("\n")
                        for arrow_dict in Inventory["WEAPON_AND_EQUIP"]["Weapon"]:
                            for arrow_name, arrow in arrow_dict.items():
                                print(f"> {GRAY}Nome: {DARKRED}{arrow.name}")

                        print("\n\n")
                        os.system('pause')
                    
                    case "4":
                        for n in range(1,20):
                            Inventory_Insert(IronArrow,"arrow")
                            Inventory_Insert(GlassArrow,"arrow")
                            Inventory_Insert(CrystalArrow,"arrow")
                            Inventory_Insert(SteelArrow,"arrow")
                            Inventory_Insert(IcyArrow,"arrow")
                            Inventory_Insert(FlamingArrow,"arrow")
                            Inventory_Insert(PoisonArrow,"arrow")
                        
                        print(f"\n\n{Fore.CYAN}Created. {B}- result:")
                        print("\n")
                        for arrow_dict in Inventory["ARROWS"]:
                            for arrow_name, arrow in arrow_dict.items():
                                print(f"- {GRAY}Nome: {DARKRED}{arrow.name}{B}, {GRAY}Danno: {DARKRED}{arrow.dmg}{B}, {GRAY}Quantità: {DARKRED}{arrow.count}")
                        
                        print("\n\n")
                        os.system('pause')

                    case "5":
                        for n in range(1,11):
                            Inventory_Insert(random.choice(All_Armors),"equip")
                        
                        print(f"\n\n{Fore.CYAN}Created. {B}- result:")
                        print("\n")
                        for arrow_dict in Inventory["WEAPON_AND_EQUIP"]["Equip"]:
                            for arrow_name, arrow in arrow_dict.items():
                                print(f"> {GRAY}Nome: {DARKRED}{arrow.name}")

                        print("\n\n")
                        os.system('pause')

                    case "6":
                        debugmode = 0
                    case "7":
                        break
                    case _:
                        continue

        case _:
            exception("You must enter a numeric value between 1 and 4.")
