######################################
#                                    #
#             LIBRERIE               #
#                                    #
######################################

#fondamental

import os
import sys
import copy
import time
import random
import pygame
import pyfiglet
from Game_Setup import *
from colorama import init, Fore, Back, Style

#debug

import traceback
import subprocess

#def install_requirements():
#    if os.path.exists("requirements.txt"):
#        print("Installazione delle dipendenze da requirements.txt...")
#        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
#    else:
#        print("File requirements.txt non trovato.")
#install_requirements()


######################################
#                                    #
#                INIT                #
#                                    #
######################################

#initialization

os.system("title Dawn of Elvaria")
init(autoreset=True)

while True:
    try:
        pygame.init()
        pygame.mixer.init()
        break

    except:
        print(f"{Fore.RED}COLLEGA UN DISPOSITIVO AUDIO DI OUTPUT")
        if input("restart? [Y/N]").upper() == "N":
            break
        else:
            continue

#color setup

GRAY = "\033[38;5;247m"
ORANGE = "\033[38;5;208m"
GRENNI = "\033[38;5;58m"
DARKRED = "\033[38;5;88m"
TEAM_COLOR = "\033[38;5;156m" 
ENEMY_COLOR = "\033[38;5;90m" 
STATS_COLOR = "\033[38;5;66m"
STATS_COLOR2 = "\033[38;5;73m"
B = Fore.BLACK + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
GOLD = "\033[38;5;220m"
BRONZE = "\033[38;5;136m" 

ColorEconomic = {
    "CC":ORANGE,
    "BC":BRONZE,
    "SC":GRAY,
    "GC":GOLD,
    "SL":W,
    "GL":Fore.YELLOW
}

ColorElement = {
    "fire":Fore.RED,
    "water":Fore.CYAN,
    "nature":Fore.GREEN,
    "light":Fore.WHITE,
    "darkness":B,
    "rock":GRENNI,
    "electro":Fore.MAGENTA
}

ColorR_E = {
    "common":GRAY,
    "uncommon":Fore.GREEN,
    "rare":Fore.CYAN,
    "epic":Fore.MAGENTA,
    "legendary":Fore.YELLOW,
    "mythical":DARKRED
}

#global variables

CI = {}
CL = []
GlobalTempTeam = {}
GlobalTempEnemyTeam = {}
Global_Temp_Graveyard = []

TempCreationDict = {
    "Name":"NB",
    "Race":"NB",
    "Gender":"NB",
    "Age":"NB",
    "Weapon":"NB"
}


######################################
#                                    #
#       FONDAMENTAL FUNCTIONS        #
#                                    #
######################################

#pause

def pause(Number_of_Space):
    if Number_of_Space != 0:
        Space = "\n"*Number_of_Space
    else:
        Space = ""
    print(f"{Space}{B}press any key to continue\n")
    os.system('pause > null')

#clear

def clear():
    os.system('cls')

#exception

def exception(text):
    print(f"{W}\n  [ {DARKRED}error{Fore.WHITE} ] = Input Not Valid! -{Fore.RED}{Style.BRIGHT} {text}\n\n")
    for sec in range(2,0,-1):
        print(f"{B}{str(sec)}.",end=" ")
        time.sleep(1)
    pause(0)

#pyfiglet title

def title(color,style,text):
    print(color + style + (ascii_art := pyfiglet.figlet_format(text)))


######################################
#                                    #
#             SOUND SYS              #
#                                    #
######################################

#main music

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

#weapon music

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


######################################
#                                    #
#             INVENTORY              #
#                                    #
######################################

#Inventory

Inventory = {
    "POTION_AND_FOOD": {
        "Potion": [
            
        ],
        "Food": [
            
        ]
    },

    "ARROWS": [
        
    ],

    "ECONOMIC": [

    ],

    "WEAPON_AND_EQUIP": {
        "Weapon": [
            
        ],
        "Equip": [
            
        ]
    },

    "ITEMS": {
        "Grimoire": [

        ],
        "Generic": [

        ]
    }
}

#manage inventory

#INSERT

def Inventory_Insert(item, category):
    try:
        existing_item = Inventory_Check(item.name, category)
    except:
        existing_item = Inventory_Check(item.grigory, category)
    
    if existing_item:
        if category.upper() in ["ARROW","POTION","WEAPON","EQUIP","GENERIC","ECONOMIC"]:
            existing_item.count += 1

    else:
        match category.upper():
            case "POTION":
                Inventory["POTION_AND_FOOD"]["Potion"].append({item.name: item})
            case "FOOD":
                Inventory["POTION_AND_FOOD"]["Food"].append({item.name: item})
            case "ARROW":
                Inventory["ARROWS"].append({item.name: item})
            case "ECONOMIC":
                Inventory["ECONOMIC"].append({item.name: item}) 
            case "WEAPON":
                Inventory["WEAPON_AND_EQUIP"]["Weapon"].append({item.name: item})
            case "EQUIP":
                Inventory["WEAPON_AND_EQUIP"]["Equip"].append({item.name: item})
            case "GRIMOIRE":
                Inventory["ITEMS"]["Grimoire"].append({item.grigory: item})
            case "GENERIC":
                Inventory["ITEMS"]["Generic"].append({item.name: item})

#REMOVE

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
        elif category.upper() == "GENERIC" and existing_item.count > 1:
            existing_item.count -= 1
        elif category.upper() == "ECONOMIC" and existing_item.count > 1:
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
            elif category.upper() == "ECONOMIC":
                Inventory["ECONOMIC"] = [
                    economics for economics in Inventory["ECONOMIC"]
                    if item.name not in economics
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
            elif category.upper() == "GRIMOIRE":
                Inventory["ITEMS"]["Grimoire"] = [
                    item_dict for item_dict in Inventory["ITEMS"]["Grimoire"]
                    if item.name not in item_dict
                ]
            elif category.upper() == "Generic":
                Inventory["ITEMS"]["Generic"] = [
                    item_dict for item_dict in Inventory["ITEMS"]["Generic"]
                    if item.name not in item_dict
                ]

#CHECK

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
    elif category.upper() == "ECONOMIC":
        for economic in Inventory["ECONOMIC"]:
            if item_name in economic:
                return economic[item_name]
    elif category.upper() == "WEAPON":
        for weapon in Inventory["WEAPON_AND_EQUIP"]["Weapon"]:
            if item_name in weapon:
                return weapon[item_name]
    elif category.upper() == "EQUIP":
        for equip in Inventory["WEAPON_AND_EQUIP"]["Equip"]:
            if item_name in equip:
                return equip[item_name]
    elif category.upper() == "GENERIC":
        for item in Inventory["ITEMS"]["Generic"]:
            if item_name in item:
                return item[item_name]
    elif category.upper() == "GRIMOIRE":
        for item in Inventory["ITEMS"]["Grimoire"]:
            if item_name in item:
                return item[item_name]
    return None

#print and visualize inventory

def Print_Inventory_Items(item):
    clear()
    title(Fore.WHITE,Style.BRIGHT,"Inventory")
    print(f"{B}|========================================================================|\n")
    try:
        print(f"\n{GRAY} [ {item.name.upper()} ]")
    except:
        print(f"\n{GRAY} [ {item.grigory.upper()} ]")

    for attribute, value in item.__dict__.items():
        attribute = attribute.replace("_"," ")
        if attribute == "Mana" or attribute == "Stamina" or attribute == "HP" or attribute == "armor":
            print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value[1]}")
        elif attribute == "R E":
            print(f"\n{W}  [ {Fore.BLUE}rarity{Fore.WHITE} ]  ==> {ColorR_E[value[0]]}{value[0]}\n\n{W}  [ {Fore.BLUE}market value{Fore.WHITE} ]  ==> {Fore.YELLOW}{value[1]}")
        elif attribute == "ammo":
            try:
                if isinstance(value.name,list) and attribute != "R E":
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}Spells")
                else:
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value.name}")
            except:
                print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value}")

        elif attribute == "TAG_Effect":
            pass
        elif isinstance(value,list) and attribute != "R E":
            print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==>",end="")
            for idx,i in enumerate(value,start=1):
                print(f" {Fore.WHITE}| {GRAY}[{Fore.RED}G{idx}{GRAY}] {B}= {Fore.YELLOW}{i}",end="")
                if len(value) == idx:
                    print("")
        else:
            print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value}")
    
    try:
        if item in All_Generic_Items and item.effect != "nb" and item.count >= 2:
            print(f"\n{GRAY} [ USE ITEMS {B}({Fore.RED}Yes{B}/{Fore.RED}No{B})]")
            while True:
                Item_Input = input(f"\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                match Item_Input.lower():
                    case "yes" | "y" | "ye" | "yep" | "sì" | "si" | "yp":
                        print("ok")
                    case "no" | "n" | "nop" | "np":
                        break
                    case _:
                        exception("Enter a valid number value")

    except:
        pass

    pause(2)
    return

def Open_Inventory_Visualizer(category, section):
    while True:
        temp_index_dict = {}
        clear()
        title(Fore.WHITE,Style.BRIGHT,"Inventory")
        print(f"{B}|========================================================================|\n")
        items_to_display = Inventory[category] if section == "nb" else Inventory[category][section]
        for idx, i in enumerate(items_to_display, start=1):
            temp_index_dict[str(idx)] = i
            idx_print = f"{B}{'0'*(3-len(str(idx)))}{ORANGE}{idx}"

            for key, value in i.items():
                key = key.ljust(12)

                count_display = value.count if hasattr(value, 'count') else 0
                count_display = f"{'0'*(3-len(str(count_display)))}{count_display}"
                print(f"  {B}[{ORANGE}{idx_print}{B}] {STATS_COLOR}[ {GRAY}{key[:12]} {STATS_COLOR}]{B}[{count_display}] {Fore.RED}|", end="")
                if idx % 3 == 0:
                    print("\n", end="")

        print(f"\n\n{GRAY} [ SELECT AN ITEM OR WRITE ANYTHING ELSE TO EXIT ]")
        Inventory_Menu2 = input(f"\n{W} [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        if Inventory_Menu2 in temp_index_dict:
            selected_item = temp_index_dict[Inventory_Menu2]
            for key, value in selected_item.items():
                Print_Inventory_Items(value)
                break

        else:
            return

def Open_Inventory():
    count = 0
    for economic_items in Inventory["ECONOMIC"]:
        for EI in economic_items.values():
            count += (EI.R_E[1]*EI.count)
    while True:
        clear()
        title(Fore.WHITE,Style.BRIGHT,"Inventory")
        print(f"{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ INVENTORY SELECT ]\n")
        print(f"  {B}[{ORANGE}1{B}] [ {Fore.RED}POTIONS {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}2{B}] [ {Fore.RED}FOODS {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}3{B}] [ {Fore.RED}ARROWS {B}- {GRAY}M. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}4{B}] [ {Fore.RED}WEAPONS {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}5{B}] [ {Fore.RED}EQUIP {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}6{B}] [ {Fore.RED}GRIMOIRE {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}7{B}] [ {Fore.RED}ITEMS {B}- {GRAY}S. CATEGORY{B} ]\n")
        print(f"  {B}[{ORANGE}8{B}] [ {Fore.RED}EXIT{B} ]\n\n\n")
        print(f"  {B}[{ORANGE}9{B}] [ {Fore.CYAN}ECONOMIC/BANK: {Fore.RED}{count} {B} ]\n")
        
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
                Open_Inventory_Visualizer("ITEMS","Grimoire")
                continue
            
            case "7":
                Open_Inventory_Visualizer("ITEMS","Generic")

            case "8":
                break

            case "9":
                Open_Inventory_Visualizer("ECONOMIC","nb")

            case _:
                exception("Enter a valid number value")
                clear()
    return

def LootInsert(list_of_item):
    economic = []
    for item in list_of_item:
        match item.R_E[0]:
            case "common":
                if "win" == random.choices(["win","np"],[0.4,0.6],k=1)[0]:
                    economic.append(CopperCoin)
            case "uncommon":
                for _ in range(random.randint(0,1)):
                    economic.append(CopperCoin)
                if "win" == random.choices(["win","np"],[0.3,0.7],k=1)[0]:
                    economic.append(BronzeCoin)
            case "rare":
                for _ in range(random.randint(0,2)):
                    economic.append(CopperCoin)
                for _ in range(random.randint(0,1)):
                    economic.append(BronzeCoin)
                if "win" == random.choices(["win","np"],[0.2,0.8],k=1)[0]:
                    economic.append(SilverCoin)
            case "epic":
                for _ in range(random.randint(0,2)):
                    economic.append(BronzeCoin)
                if "win" == random.choices(["win","np"],[0.4,0.6],k=1)[0]:
                    economic.append(SilverCoin)
            case "legendary":
                for _ in range(random.randint(0,2)):
                    economic.append(SilverCoin)
                for _ in range(random.randint(0,1)):
                    economic.append(GoldCoin)
                if "win" == random.choices(["win","np"],[0.2,0.8],k=1)[0]:
                    economic.append(SilverLingot)

            case "mythical":
                for _ in range(random.randint(2,5)):
                    economic.append(SilverCoin)
                for _ in range(random.randint(0,3)):
                    economic.append(GoldCoin)
                for _ in range(random.randint(0,1)):
                    economic.append(SilverLingot)
                if "win" == random.choices(["win","np"],[0.2,0.8],k=1)[0]:
                    economic.append(GoldLingot)

        if item in All_Generic_Items:
            Inventory_Insert(item,"generic")
        elif item in All_Spells:
            Inventory_Insert(item,"grimoire")
        elif item in All_Weapons:
            Inventory_Insert(item,"weapon")
        elif item in All_Armors:
            Inventory_Insert(item,"equip")
        elif item in Potions_List:
            Inventory_Insert(item,"potion")
        elif item in All_Arrow:
            Inventory_Insert(item,"arrow")

    CC = 0
    BC = 0
    SC = 0
    GC = 0
    SL = 0
    GL = 0
    for values in economic:
        Inventory_Insert(values,"economic")
        match values.name:
            case "Copper Coin":
                CC += 1
            case "Bronze Coin":
                BC += 1
            case "Silver Coin":
                SC += 1
            case "Gold Coin":
                GC += 1
            case "Silver Lingot":
                SL += 1
            case "Gold Lingot":
                GL += 1
    return [CC,BC,SC,GC,SL,GL]

######################################
#                                    #
#                MENU                #
#                                    #
######################################

def create_menu(title_menu,list_title,end):
    clear()
    title(Fore.CYAN,Style.NORMAL,"Dawn of Elvaria")
    print(f"{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ {title_menu.upper()} ]\n")
    number = 1
    for titles in list_title:
        print(f"{W}  [ {ORANGE}{number}{Fore.WHITE} ] -  {Fore.YELLOW}{titles}\n")
        number += 1
    print(f"{W}  [ {ORANGE}{number}{Fore.WHITE} ] -  {Fore.RED}{end.upper()}\n")
    print(f"{B}|========================================================================|\n\n")
    

######################################
#                                    #
#        CHARACTER CREATION          #
#                                    #
######################################

#main function

def Creation():
    clear()
    title(Fore.CYAN,Style.NORMAL,"Dawn of Elvaria")
    print(f"{B}|========================================================================|\n")
    print(f"{Fore.CYAN} [ CREATE YOUR CHARACTER ]\n")

    Creation_Name()
    Creation_Race()
    Creation_Gender()
    Creation_Age()
    Creation_Weapon()

    while True:
        clear()
        title(Fore.CYAN,Style.NORMAL,"Dawn of Elvaria")
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
                clear()
                title(Fore.CYAN,Style.NORMAL,"Dawn of Elvaria")
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

#creation name

def Creation_Name():
    while True:
        ChooseName = input(f"\n{W}  [ {ORANGE}1{Fore.WHITE} ] -  {Fore.YELLOW}Choose the Character's Name: {Fore.BLUE}").capitalize()

        if ChooseName in CI:
            exception("the character already exists, change it or insert an epithet")
            continue 
        else:
            TempCreationDict["Name"] = ChooseName
            return

#creation race

def Creation_Race():
    while True:
        RaceChoice = input(f"\n{W}  [ {ORANGE}2{Fore.WHITE} ] -  {Fore.YELLOW}Choose the Character's Race: {Fore.BLUE}").capitalize().strip()

        if not RaceChoice.isalpha():
            exception("the name of your race cannot contain numbers or special characters")
            continue 
        else:
            TempCreationDict["Race"] = RaceChoice
            return

#creation gender

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

#creation age

def Creation_Age():
    while True:
        AgeChoice = input(f"\n{W}  [ {ORANGE}4{Fore.WHITE} ] -  {Fore.YELLOW}Choose the Character's Age (It Must be a Number): {Fore.BLUE}").strip()

        if not AgeChoice.isdigit():
            exception("you must enter a number")
            continue 
        else:
            TempCreationDict["Age"] = AgeChoice
            return

#creation weapon

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


######################################
#                                    #
#    VIEW AND MANAGER CHARACTERS     #
#                                    #
######################################

def View():
    while True:
        clear()
        title(Fore.CYAN,Style.NORMAL,"Dawn of Elvaria")
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
            match ViewChoice:
                case "EXIT":
                    return
                case _ if ViewChoice.isdigit() and int(ViewChoice) == TempCount:
                    return
                case _ if ViewChoice.isdigit():
                    if int(ViewChoice) > len(CL) or int(ViewChoice) <= 0:
                        exception("character not in the list, enter a valid number")
                        continue 
                    else:
                        ViewChoice = int(ViewChoice) - 1
                        Manage_Characters(ViewChoice)
                        continue
                case _:
                    exception("enter a valid input!")
        except Exception as e:
            print(f"Exception Type: {type(e).__name__}")
            print(f"Error Message: {str(e)}")
            print("Stack Trace:")
            print(traceback.format_exc())
            os.system('pause')

def Change_Equip(C_haracter,Category):
    for idx,i in enumerate(Inventory["WEAPON_AND_EQUIP"][Category],start=1):
        Item = list(i.values())[0]
        print(f"{STATS_COLOR} [ {ORANGE}{idx} {STATS_COLOR}= {B}{Item.name.upper()} ({Item.count}){STATS_COLOR}]",end="")
        if idx%3 == 0:
            print("\n",end="")

    while True:
        Select = input(f"\n{W} [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        if Select.isdigit() and Inventory["WEAPON_AND_EQUIP"][Category][int(Select)-1]:
            
            if Category == "Weapon":
                Inventory_Insert(C_haracter.Weapon,Category)
                Inventory_Remove(list(Inventory["WEAPON_AND_EQUIP"][Category][int(Select)-1].values())[0],"Weapon")
                C_haracter.Weapon = list(Inventory["WEAPON_AND_EQUIP"][Category][int(Select)-1].values())[0]
            else:
                Inventory_Insert(C_haracter.Armor,Category)
                Inventory_Remove(list(Inventory["WEAPON_AND_EQUIP"][Category][int(Select)-1].values())[0],"Equip")
                C_haracter.Armor = list(Inventory["WEAPON_AND_EQUIP"][Category][int(Select)-1].values())[0]

            print(f"\n{STATS_COLOR} [INFO STATS] {B}-{STATS_COLOR} [ {Fore.GREEN}{Category.upper()} CHANGED ]\n")
            pause(0)
            break
        else:
            exception(f"You must enter a valid numeric value")
            continue
    return

def Manage_Characters(C_haracters):
    while True:
        clear()
        Characters = CL[C_haracters]
        title(Fore.CYAN,Style.NORMAL,"Dawn of Elvaria")
        print(f"{B}|========================================================================|\n")
        print(f"{Fore.CYAN} [ CHARACTER: {Fore.GREEN}{Characters}{Fore.CYAN} ]\n")

        if Characters in CI:
            ViewCharacter = CI[Characters]
            for attribute, value in ViewCharacter.__dict__.items():
                if attribute == "Mana" or attribute == "Stamina" or attribute == "HP":
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value[1]}")
                elif attribute == "Weapon" or attribute == "Armor":
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value.name}")
                elif attribute == "TAG_Effect" or attribute == "Active_Element":
                    pass
                else:
                    print(f"\n{W}  [ {Fore.BLUE}{attribute.lower()}{Fore.WHITE} ]  ==> {Fore.YELLOW}{value}")
        else:
            exception("the chosen character does not exist")
            continue 
        
        print(f"\n\n{Fore.CYAN} [ MANAGE CHARACTER OR EXIT ]")
        
        print(f"\n{STATS_COLOR} [ {STATS_COLOR2}manager ch.{STATS_COLOR} ]  {B}==> {STATS_COLOR}[ {ORANGE}1{STATS_COLOR} ] = {B}CHANGE ARMOR | {STATS_COLOR}[ {ORANGE}2{STATS_COLOR} ] = {B}CHANGE WEAPON | {STATS_COLOR}[ {ORANGE}3{STATS_COLOR} ] = {Fore.RED}EXIT ")
        Choice_Select = input(f"{W} [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
        match Choice_Select:
            case "1":
                if Choice_Select.isdigit() and Inventory["WEAPON_AND_EQUIP"]["Equip"]:
                    print(f"\n{STATS_COLOR} [ {STATS_COLOR2}choose the armor{STATS_COLOR} ]  {B}==> ",end="")
                    Change_Equip(ViewCharacter,"Equip")

                else:
                    print(f"{W}\n  [ {DARKRED}info{Fore.WHITE} ] = Enter a valid numeric value / You have no other weapons\n\n")
                    pause(0)

            case "2":
                if Choice_Select.isdigit() and Inventory["WEAPON_AND_EQUIP"]["Weapon"]:
                    print(f"\n{STATS_COLOR} [ {STATS_COLOR2}choose the weapon{STATS_COLOR} ]  {B}==> ",end="")
                    Change_Equip(ViewCharacter,"Weapon")

                else:
                    print(f"{W}\n  [ {DARKRED}info{Fore.WHITE} ] = Enter a valid numeric value / You have no other weapons\n\n")
                    pause(0)

            case "3":
                return
    

######################################
#                                    #
#            BUILD TEAM              #
#                                    #
######################################

def CreateTeam():
    clear()
    TempTeam = []

    title(Fore.CYAN,Style.NORMAL,"Dawn of Elvaria")
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
    

######################################
#                                    #
#            COMBAT SYS              #
#                                    #
######################################

#starting

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

    clear()
    title(Fore.RED,Style.BRIGHT,"preparation")
    print(f"{B}|========================================================================|\n")
    print(f"{TEAM_COLOR} [ YOUR TEAM ]\n")

    for i in range(1,4):
        member = GlobalTempTeam[f'{str(i)}_member']
        member.HP[0] = member.HP[1]
        member.Stamina[0] = (member.Stamina[1]+member.Armor.mod_stamina)
        member.Mana[0] = (member.Mana[1]+member.Armor.mod_mana)
        print(f"{B}  [{i}][ {Fore.BLUE}{member.Name}{B} ] -  {Fore.YELLOW}armor: {B}{member.Armor.name} | {Fore.YELLOW}weapon: {B}{member.Weapon.name} | {Fore.YELLOW}stats: {B}HP: {member.HP[0]}[{member.Armor.armor[1]}] / MANA: {member.Mana[1]+member.Armor.mod_mana} / STAMINA: {member.Stamina[1]+member.Armor.mod_stamina} \n")

    print(f"{ENEMY_COLOR} [ ENEMY TEAM ]\n")
    for j in GlobalTempEnemyTeam:
        member = GlobalTempEnemyTeam[j]
        member.HP[0] = member.HP[1]
        member.Stamina[0] = (member.Stamina[1]+member.Armor.mod_stamina)
        member.Mana[0] = (member.Mana[1]+member.Armor.mod_mana)
        print(f"{B}  [{i}][ {Fore.BLUE}{member.Name}{B} ] -  {Fore.YELLOW}armor: {B}{member.Armor.name} | {Fore.YELLOW}weapon: {B}{member.Weapon.name} | {Fore.YELLOW}stats: {B}HP: {member.HP[0]}[{member.Armor.armor[1]}] / MANA: {member.Mana[1]+member.Armor.mod_mana} / STAMINA: {member.Stamina[1]+member.Armor.mod_stamina} \n")

    print(f"{B}As soon as you're ready, press any key..\n")
    os.system('pause > null')
    Combat(enemyT,team)
    return

#turn print

def Print_Combat(PC_team_name, CCT):
    global GlobalTempTeam, GlobalTempEnemyTeam

    if PC_team_name == "GlobalTempTeam":
        PC_team = GlobalTempTeam
    elif PC_team_name == "GlobalTempEnemyTeam":
        PC_team = GlobalTempEnemyTeam
    else:
        print("Error NameTeam")
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
        
        prnt_element = ""
        for lmnt,active in member.Active_Element.items():
            if active > 0:
                prnt_element += ColorElement[lmnt]+"*"
        
        if member.Weapon.type == "Bow":
            print(f"{PC_teamSpace}{GRAY} |  {B}[{GRAY}{idx.split('_')[0]}{B}] {GRAY}{member.Name}{prnt_element} {B}| HP/ARMOR: {HP_Color}{int(member.HP[0])}{B}/{ARMOR_Color}[{int(member.Armor.armor[0])}] {B}MANA: {Mana_Color}{member.Mana[0]} {B}STAMINA: {Stamina_Color}{member.Stamina[0]} {B}/ {GRAY}{member.Weapon.name}({member.Weapon.ammo.name})")
        elif member.Weapon.type == "Magical":
            print(f"{PC_teamSpace}{GRAY} |  {B}[{GRAY}{idx.split('_')[0]}{B}] {GRAY}{member.Name}{prnt_element} {B}| HP/ARMOR: {HP_Color}{int(member.HP[0])}{B}/{ARMOR_Color}[{int(member.Armor.armor[0])}] {B}MANA: {Mana_Color}{member.Mana[0]} {B}STAMINA: {Stamina_Color}{member.Stamina[0]} {B}/ {GRAY}{member.Weapon.name}({ColorElement[member.Weapon.ammo.elemental]}{member.Weapon.ammo.name[member.Weapon.grade-1]}{GRAY})")
        else:
            print(f"{PC_teamSpace}{GRAY} |  {B}[{GRAY}{idx.split('_')[0]}{B}] {GRAY}{member.Name}{prnt_element} {B}| HP/ARMOR: {HP_Color}{int(member.HP[0])}{B}/{ARMOR_Color}[{int(member.Armor.armor[0])}] {B}MANA: {Mana_Color}{member.Mana[0]} {B}STAMINA: {Stamina_Color}{member.Stamina[0]} {B}/ {GRAY}{member.Weapon.name}")
    
    print(f"{GRAY}{PC_teamSpace} |_______________________________|")

    CCT += 1
    return CCT

#turn logic

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
        
        if Value.Armor.main_effect == "Endurance":
            RGV_stamina += 5

        for effect in Value.TAG_Effect:
            if effect.name == "Magical" and effect.duration != 0:
                RGV_mana += effect.buff_efx

        ManaTOTs = (Value.Mana[1] + Value.Armor.mod_mana)
        StaminaTOTs = (Value.Stamina[1] + Value.Armor.mod_stamina)

        if Value.Mana[0] < ManaTOTs:
            Value.Mana[0] = min(Value.Mana[0] + RGV_mana, ManaTOTs)

        if Value.Stamina[0] < StaminaTOTs:
            Value.Stamina[0] = min(Value.Stamina[0] + RGV_stamina, StaminaTOTs)

    for Value in GlobalTempEnemyTeam.values():
        RGV_mana = 5
        RGV_stamina = 5
        
        if Value.Ability == "Magic":
            RGV_mana = 10
        elif Value.Ability == "Brute":
            RGV_stamina = 10
        
        if Value.Armor.main_effect == "Endurance":
            RGV_stamina += 5

        for effect in Value.TAG_Effect:
            if effect.name == "Magical" and effect.duration != 0:
                RGV_mana += effect.buff_efx

        ManaTOTs = (Value.Mana[1] + Value.Armor.mod_mana)
        StaminaTOTs = (Value.Stamina[1] + Value.Armor.mod_stamina)

        if Value.Mana[0] < ManaTOTs:
            Value.Mana[0] = min(Value.Mana[0] + RGV_mana, ManaTOTs)
            
        if Value.Stamina[0] < StaminaTOTs:
            Value.Stamina[0] = min(Value.Stamina[0] + RGV_stamina, StaminaTOTs)
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
    
#combat system

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

    clear()
    title(Fore.RED,Style.BRIGHT,"battle")
    
    while EnemyTotHP > 0 and TeamTotHP > 0:
        if Who_Start[0] == 0:
            Who_Start[0] = Player_Combat(Who_Start,First_Turn)
            First_Turn += 1
            
        elif Who_Start[0] == 1:
            Who_Start[0] = Enemy_Combat_Logic(Who_Start,First_Turn)
            First_Turn += 1
           
        elif Who_Start[0] == 2:
            end_battle("lose",enemyT,First_Turn,team)
            pygame.mixer.music.pause()
            lost_sound = pygame.mixer.Sound("Audio_Assets/Soundeffect/MixSound/lose.wav")
            lost_sound.set_volume(0.5)
            lost_sound.play()
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.unpause()
            break
        
        elif Who_Start[0] == 3:
            end_battle("win",enemyT,First_Turn,team)
            pygame.mixer.music.pause()
            win_sound = pygame.mixer.Sound("Audio_Assets/Soundeffect/MixSound/win.wav")
            win_sound.set_volume(0.5)
            win_sound.play()
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.unpause()

            break
        
        elif Who_Start[0] == 4:
            end_battle("escape",enemyT,First_Turn,team)
            break
            
    play_music("Audio_Assets/Soundtrack/menu.wav", -1)
    return


#endbattle

def end_battle(win_or_lose,enemyTeam,turn,team):
    clear()
    if win_or_lose == "win":
        tempcolor = [TEAM_COLOR,Fore.GREEN,"You Won !"]
    elif win_or_lose == "lose":
        tempcolor = [ENEMY_COLOR,Fore.RED,"Game Over !"]
    elif win_or_lose == "escape":
        tempcolor = [GRAY,GRAY,"Escape"]
        
    title(tempcolor[1],Style.BRIGHT,tempcolor[2])

    print(f"{B}|========================================================================|\n")

    print(f"{tempcolor[0]} [ YOUR TEAM ]\n")
    for i in range(1,4):
        print(f"{B}  [{i}][ {Fore.BLUE}{team[i-1].Name}{B} ] -  {Fore.YELLOW}armor: {B}{team[i-1].Armor.name} | {Fore.YELLOW}weapon: {B}{team[i-1].Weapon.name} | {Fore.YELLOW}stats: {B}HP: {team[i-1].HP[0]} / MANA: {team[i-1].Mana[0]} / STAMINA: {team[i-1].Stamina[0]} \n")

    time.sleep(0.5)
    print(f"\n{tempcolor[0]} [ BATTLE STATS ]\n")
    time.sleep(0.5)
    print(f"{B}  - 1 ) {Fore.YELLOW}total turns: {B}{turn}\n")
    time.sleep(0.5)
    print(f"{B}  - 2 ) {Fore.YELLOW}enemies killed: {B}{len(Global_Temp_Graveyard)}\n")
    time.sleep(0.5)
    LootBattle = []
    for i in Global_Temp_Graveyard:
        for value in GlobalTempTeam.values():
            if value.Armor.main_effect == "Fortune": NB = "Fortune"
            else: NB = "NB"
        LootBattle.extend(CreateLootDrop(i,NB))
    print_economic = LootInsert(LootBattle)
    print(f"{B}  - 3 ) {Fore.YELLOW}loot:",end="")
    for idx,LT in enumerate(LootBattle,start=1):
        print(f"{B} > {ColorR_E[LT.R_E[0]]}{LT.name}",end="")
        if idx%4 == 0:
            print(f"\n{B}  |          ",end="")
    print(f"\n\n  {B}> {ColorEconomic["CC"]}CC: {B}{print_economic[0]} | {ColorEconomic["BC"]}BC: {B}{print_economic[1]} | {ColorEconomic["SC"]}SC: {B}{print_economic[2]} | {ColorEconomic["GC"]}GC: {B}{print_economic[3]} | {ColorEconomic["SL"]}SL: {B}{print_economic[4]} | {ColorEconomic["GL"]}GL: {B}{print_economic[5]}")
    time.sleep(1.5)

    pause(2)
    return


######################################
#                                    #
#           COMBAT LOGIC             #
#                                    #
######################################

#damage count logic

def Element_Logic(character):
    element_list = []
    mpx = 1
    
    for lmnt,value in character.Active_Element.items():

        if value > 0:
            element_list.append(lmnt)
            character.Active_Element[lmnt] -= 1

        if len(element_list) == 3:
            element_list.pop(0)
        
        match element_list:
            case ["rock","water"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {GRAY}Erosion {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.2

            case ["rock","fire"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {ORANGE}Lava Flow {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.3

            case ["rock","electro"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {Fore.RED}Magnetize {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.1

            case ["nature","water"] | ["water","nature"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {Fore.GREEN}Grow {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.2
            
            case ["nature","darkness"] | ["darkness","nature"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {B}Wither {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.4
            
            case ["nature","fire"] | ["fire","nature"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {GRENNI}Wildfire {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.3
            
            case ["water","fire"] | ["fire","water"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {Fore.CYAN}Vaporize {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.2
            
            case ["water","electro"] | ["electro","water"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {STATS_COLOR2}Electroshock {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.3
            
            case ["water","light"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {W}Purify {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.1
            
            case ["light","darkness"] | ["darkness","light"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {Fore.YELLOW}Eclipse {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.5
            
            case ["light","electro"] | ["electro","light"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {ENEMY_COLOR}Super Bolt {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.3
            
            case ["darkness","fire"] | ["fire","darkness"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {DARKRED}Hell Fire {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.4
            
            case ["water","darkness"] | ["darkness","water"]:
                print(f"\n{STATS_COLOR}[ ELEMENT REACTIONS - {Fore.BLUE}Abyss {STATS_COLOR}]")
                for i in element_list:
                    character.Active_Element[i] = 0
                element_list.clear()
                mpx = 1.4
           
    return mpx

def Damage_Logic(target,character):
    damage = character.Weapon.damage
    mpx = 1
    modif_by_velocity = 1
    modif_by_effect = 1
    modif_by_protection = 1
    return_stats = []

    if character.Weapon.type == "Magical":
        damage += character.Weapon.ammo.damage[character.Weapon.grade-1]

        if character.Weapon.ammo.secondary_effect[character.Weapon.grade-1].lower() in ["Resistance","Shield","Strong Shield","Strength","Potent Strength","Regen","Healing","Strong Healing"]:
            for efx in character.TAG_Effect:
                if efx.name.lower() == character.Weapon.ammo.secondary_effect[character.Weapon.grade-1].lower():
                    efx.duration[0] = efx.duration[1]
            
            damage = 0
            
            character.Active_Element[character.Weapon.ammo.elemental] = character.Weapon.grade
        else:
            for efx in target.TAG_Effect:
                if efx.name.lower() == character.Weapon.ammo.secondary_effect[character.Weapon.grade-1].lower():
                    efx.duration[0] = efx.duration[1]

            target.Active_Element[character.Weapon.ammo.elemental] = character.Weapon.grade
        
        if target.Armor.protection.lower() == character.Weapon.ammo.elemental.lower():
            modif_by_protection = 0.8

    if character.Ability == "Rapid" or character.Armor.main_effect == "Thief's Rapid":
        if "win" == random.choice(["win","lose"]):
            mpx *= 2
            return_stats.append("Rapid")

    if target.Ability == "Shield":
        mpx *= 0.8
        return_stats.append("Shield")
    
    for effect in target.TAG_Effect:
        if effect.name in ["Resistance"] and modif_by_effect > 0 and effect.duration[0] != 0:
            modif_by_effect -= (effect.debuf_efx/100)
            if modif_by_effect < 0:
                modif_by_effect = 0

        if effect.name in ["Anti Arrow"] and modif_by_effect > 0 and effect.duration[0] != 0:
            if character.Weapon.type == "Bow":
                modif_by_effect -= (effect.debuf_efx/100)
            if modif_by_effect < 0:
                modif_by_effect = 0

        if effect.name in ["Frost"] and effect.duration[0] != 0:
            modif_by_effect += (effect.debuf_efx/100)
    
    for effect in character.TAG_Effect:
        if effect.name in ["Weakness"] and modif_by_effect > 0 and effect.duration[0] != 0:
            modif_by_effect -= (effect.debuf_efx/100)
            if modif_by_effect < 0:
                modif_by_effect = 0
        
        if effect.name in ["Strength","Potent Strength"] and effect.duration[0] != 0:
            modif_by_effect += (effect.buff_efx/100)

    Precision = character.Weapon.precision
    Velocity = character.Weapon.velocity

    if Velocity > 3:
        modif_by_velocity += (Velocity/100)
        if Precision > 0.8:
            modif_by_velocity += 0.06
    
    elif Velocity < 2 and Precision < 0.8:
        modif_by_velocity -= ((5 - Velocity)/100)
        if Precision < 0.6:
            modif_by_velocity -= 0.06

    if character.Armor.main_effect == "Fortune":
        damage += random.choice([0,5])

    modif_by_element = Element_Logic(target)

    damage = damage * modif_by_velocity
    damage = round(damage, 2)

    damage = damage * mpx
    damage = round(damage, 2) 

    damage = damage * modif_by_protection
    damage = round(damage, 2)

    damage = damage * modif_by_effect
    damage = round(damage, 2) 

    damage = damage * modif_by_element
    damage = round(damage, 2) 

    return [damage,return_stats]

#enemy logic system

def Enemy_Combat_Logic(Who_Start, First_Turn):
    global GlobalTempEnemyTeam
    global GlobalTempTeam

    ability_print = [0,0]
    CombatCT = 1
    Debuff_Effects = 0
    Buff_Effects = 0
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
        
        if Enemy_Selected.Weapon.type == "Magical" or Enemy_Selected.Weapon.name == "Arcane Bow":
            try:
                if Enemy_Selected.Weapon.name != "Arcane Bow":
                    
                    Adjust_CreateEnemy_Ammo(Enemy_Selected)
                mans = Enemy_Selected.Weapon.mana + Enemy_Selected.Weapon.ammo.mana
            except:
                mans = Enemy_Selected.Weapon.mana

            if Enemy_Selected.Mana[0] >= mans:
                Enemy_Selected.Mana[0] -= mans
            else:
                print(f"{STATS_COLOR}[ THE ENEMY HAD NOT ENOUGH MANA TO ATTACK ]\n")
                time.sleep(2)
                del CharacterSelectedList[NS]
                pause(0)
                continue
        else:
            mans = 0
            if Enemy_Selected.Stamina[0] >= Enemy_Selected.Weapon.stamina:
                Enemy_Selected.Stamina[0] -= Enemy_Selected.Weapon.stamina
            else:
                print(f"{STATS_COLOR}[ THE ENEMY HAD NOT ENOUGH STAMINA TO ATTACK ]\n")
                time.sleep(2)
                del CharacterSelectedList[NS]
                pause(0)
                continue
        

        for efx in Enemy_Selected.TAG_Effect:
            efx.update_duration()

            if Enemy_Selected.Armor.passive_effect == efx.name:
                efx.duration[0] = efx.duration[1]

            if efx.duration[0] != 0 and efx.buff_efx != 0:
                match efx.name:
                    case "Regen" | "Healing" | "Strong Healing":
                        if Enemy_Selected.HP[0] < Enemy_Selected.HP[1]:
                            Enemy_Selected.HP[0] = min(Enemy_Selected.HP[0] + efx.buff_efx, Enemy_Selected.HP[1])
                    
                    case "Shield" | "Strong Shield":
                        Enemy_Selected.Armor.armor[0] += efx.buff_efx
                        
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

                    case "Wood":
                        for efx1 in Enemy_Selected.TAG_Effect:
                            if efx1.duration[0] != 0 and efx1.name == "Burn":
                                Debuff_Effects += efx.debuff.efx
                        if Enemy_Selected.Active_Element["nature"] > 0:
                            if Enemy_Selected.HP[0] < Enemy_Selected.HP[1]:
                                Enemy_Selected.HP[0] = min(Enemy_Selected.HP[0] + 5, Enemy_Selected.HP[1])

                    case _:
                        Debuff_Effects += efx.debuf_efx

        
        W1 = Enemy_Selected.Weapon.precision
        W2 = 1 - Enemy_Selected.Weapon.precision
        if Enemy_Selected.Ability == "Archer" and Enemy_Selected.Weapon.type == "Bow":
            W1 += 0.2
            W2 -= 0.2

        for effect in Enemy_Selected.TAG_Effect:
            if effect.name == "Lowering Speed" and effect.duration[0] != 0:
                W1 -= effect.debuf_efx
                W2 += effect.debuf_efx
        
        if Enemy_Selected.Armor.main_effect == "Good Aim":
            W1 += 0.15
            W2 -= 0.15
        elif Enemy_Selected.Armor.main_effect == "Fortune":
            fortune = random.choice([0,0.1])
            W1 += fortune
            W1 -= fortune

        if W1 < 0:
            W1 = 0
        elif W1 > 1:
            W1 = 1
        
        if W2 < 0:
            W2 = 0
        elif W2 > 1:
            W2 = 1

        
        W1 = round(W1,2)
        W2 = round(W2,2)

        if "hit" == random.choices(["hit","miss"],weights=[W1,W2],k=1)[0]:
            Damage_Logic_Return = Damage_Logic(Target,Enemy_Selected)
            damage = Damage_Logic_Return[0]
            if damage < 0:
                damage = 0
            if "Rapid" in Damage_Logic_Return[1]:
                ability_print = [f"{STATS_COLOR}[ABILITY] {B}-{STATS_COLOR} [ '{STATS_COLOR2}RAPID{STATS_COLOR}' - {Enemy_Selected.Name.upper()} ATTACKED TWICE ]\n",1]
            
            prnt = f"{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ THE ENEMY HITS YOU ][ {STATS_COLOR2}damage: {Fore.RED}-{damage}{B} - {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{mans}{B}/{Fore.YELLOW}-{Enemy_Selected.Weapon.stamina}{STATS_COLOR} ]\n"
            
            if ability_print[1] != 0:
                print(ability_print[0])
            print(prnt)

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
                pause(0)
                continue

            pause(0)

        else:
            print(f"{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ THE ENEMY MISSED YOU ][ {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{mans}{B}/{Fore.YELLOW}-{Enemy_Selected.Weapon.stamina}{STATS_COLOR} ]\n")
            time.sleep(2)
            del CharacterSelectedList[NS]
            pause(0)
            continue
            
        EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
        TeamTotHP = sum(member.HP[0] for member in GlobalTempTeam.values())

        Enemy_Selected.HP[0] -= Debuff_Effects

        del CharacterSelectedList[NS]
        if Enemy_Selected.HP[0] <= 0:
            print(f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ {STATS_COLOR2}{Enemy_Selected.Name.upper()} WAS DEFEATED by effects {STATS_COLOR}]\n")
            time.sleep(2)
            Global_Temp_Graveyard.append(GlobalTempEnemyTeam[NS])
            del GlobalTempEnemyTeam[NS]
            pause(0)
        continue

    if TeamTotHP > 0 and EnemyTotHP > 0:
        print(f"\n{B}|========================================================================|\n")
        RegenEffect()
        print(f"{Fore.CYAN} [ TURN SUMMARY ][ MANA / STAMINA HAVE BEEN REGENERATED ]\n")
        CombatCT = Print_Combat("GlobalTempEnemyTeam", CombatCT)
        print("\n")
        CombatCT = Print_Combat("GlobalTempTeam", CombatCT)
        pause(1)
        return 0

    elif TeamTotHP <= 0:
        return 2
    elif EnemyTotHP <= 0:
        return 3
    
#player combat logic

def Player_Combat(Who_Start,First_Turn):
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
                    stats_mess = Player_Combat_Turn("1_member",CombatCT)
                    EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
                    break
                elif Character_Selected == "2":
                    del CharacterSelectedList["2_member"]
                    stats_mess = Player_Combat_Turn("2_member",CombatCT)
                    EnemyTotHP = sum(enemy.HP[0] for enemy in GlobalTempEnemyTeam.values())
                    break
                elif Character_Selected == "3":
                    del CharacterSelectedList["3_member"]
                    stats_mess = Player_Combat_Turn("3_member",CombatCT)
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
        pause(0)
        return 1
    elif TeamTotHP <= 0:
        return 2
    elif EnemyTotHP <= 0:
        return 3

def Player_Combat_Inventory(Team_Member,CombatCT):
    global GlobalTempEnemyTeam
    global GlobalTempTeam
    clear()
    title(Fore.RED,Style.BRIGHT,"battle")
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
                        if Weapon_Select.isdigit() and Inventory["WEAPON_AND_EQUIP"]["Weapon"][int(Weapon_Select)-1]:
                            Inventory_Insert(GlobalTempTeam[Team_Member].Weapon,"Weapon")
                            GlobalTempTeam[Team_Member].Weapon = list(Inventory["WEAPON_AND_EQUIP"]["Weapon"][int(Weapon_Select)-1].values())[0]
                            Inventory_Remove(list(Inventory["WEAPON_AND_EQUIP"]["Weapon"][int(Weapon_Select)-1].values())[0],"Weapon")
                            
                            print(f"\n{STATS_COLOR}  [INFO STATS] {B}-{STATS_COLOR} [ {Fore.GREEN}WEAPON CHANGED{STATS_COLOR} ]\n")
                            pause(0)
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
                pause(0)

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
                        if Potion_or_Food_Select.isdigit() and Inventory["POTION_AND_FOOD"]["Potion"][int(Potion_or_Food_Select)-1]:
                            
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
                            pause(0)
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
                pause(0)

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
                            pause(0)
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
                pause(0)
                break
        
        elif GlobalTempTeam[Team_Member].Weapon.type == "Bow" and Choice_Select == "4":
            break
        elif GlobalTempTeam[Team_Member].Weapon.type != "Bow" and Choice_Select == "3":
            break
        else:
            exception(f"You must enter a valid numeric value")
            continue

    return [f"{STATS_COLOR}[ INVENTORY CLOSED ]\n"]

def Player_Combat_Turn(Team_Member,CombatCT):
    global GlobalTempEnemyTeam
    global GlobalTempTeam
    PG = GlobalTempTeam[Team_Member]
    
    stats_effect = f"{STATS_COLOR}[EFFECTS STATS]"
    Buff_Effects = 0
    Debuff_Effects = 0

    for efx in PG.TAG_Effect:
        efx.update_duration()
        if PG.Armor.passive_effect == efx.name:
            efx.duration[0] = efx.duration[1]
        if efx.duration[0] != 0 and efx.element == "nb":
            stats_effect += f" {B}- {STATS_COLOR}[ {GRAY}name: {Fore.RED}{efx.name.upper()} {GRAY}({ORANGE}{efx.duration[0]}{GRAY}) {STATS_COLOR}]"
        elif efx.duration[0] != 0 and efx.element != "nb":
            stats_effect += f" {B}- {STATS_COLOR}[ {GRAY}name: {ColorElement[efx.element]}{efx.name.upper()} {GRAY}({ORANGE}{efx.duration[0]}{GRAY}) {STATS_COLOR}]"


        if efx.duration[0] != 0 and efx.buff_efx != 0:
            match efx.name:
                case "Regen" | "Healing" | "Strong Healing":
                    if PG.HP[0] < PG.HP[1]:
                        PG.HP[0] = min(PG.HP[0] + efx.buff_efx, PG.HP[1])

                case "Shield" | "Strong Shield":
                    PG.Armor.armor[0] += efx.buff_efx

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

                case "Wood":
                    for efx1 in PG.TAG_Effect:
                        if efx1.duration[0] != 0 and efx1.name == "Burn":
                            Debuff_Effects += efx.debuf_efx
                    if PG.Active_Element["nature"] > 0:
                        if PG.HP[0] < PG.HP[1]:
                            PG.HP[0] = min(PG.HP[0] + 5, PG.HP[1])

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
            if PG.Weapon.type == "Magical" and PG.Weapon.name != "Arcane Bow":
                while True:
                    print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the spell to use{STATS_COLOR} ]  {B}==>",end="")
                    if Inventory["ITEMS"]["Grimoire"]:
                        for idx,i in enumerate(Inventory["ITEMS"]["Grimoire"],start=1):
                            Spell = list(i.values())[0]
                            if Spell.elemental == PG.Weapon.element and Spell.grade <= PG.Weapon.grade:
                                print(f" {STATS_COLOR}[ {ORANGE}{idx} {STATS_COLOR}= {ColorElement[Spell.elemental]}{Spell.name[PG.Weapon.grade-1].upper()} {STATS_COLOR}]",end="")
                                if idx%3 == 0:
                                    print("\n ",end="")
                            else:
                                pass
                    else:
                        print(f"{W}\n  [ {DARKRED}info{Fore.WHITE} ] = you have no other spells\n\n")
                        pause(0)
                        break

                    while True:
                        Spell_Select = input(f"\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                        if Spell_Select.isdigit() and Inventory["ITEMS"]["Grimoire"][int(Spell_Select)-1]:
                            PG.Weapon.ammo = list(Inventory["ITEMS"]["Grimoire"][int(Spell_Select)-1].values())[0]
                            
                            print(f"\n{STATS_COLOR}  [INFO STATS] {B}-{STATS_COLOR} [ {Fore.GREEN}SPELL SELECTED ({ColorElement[Spell.elemental]}{PG.Weapon.ammo.grigory}{Fore.GREEN}){STATS_COLOR} ]")
                            break
                        else:
                            exception(f"You must enter a valid numeric value")
                            continue
                    break

            while True:
                if PG.Weapon.type == "Magical" and PG.Weapon.name != "Arcane Bow":
                    if PG.Weapon.ammo.grigory.capitalize() not in ["Flowing Rain","Faith Shield","Healing","Restorative Growth","Granite Shield"]:
                        print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the enemy to hit {STATS_COLOR}] {B} ==>",end="")
                        for keys,values in enumerate(list(GlobalTempEnemyTeam.values()),start=1):
                            print(f" {STATS_COLOR} '{ORANGE}{keys}{STATS_COLOR}' - {values.Name} |",end="")
                        
                        temx = GlobalTempEnemyTeam
                    else:
                        print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the character to buff {STATS_COLOR}] {B} ==>",end="")
                        for keys,values in enumerate(list(GlobalTempTeam.values()),start=1):
                            print(f" {STATS_COLOR} '{ORANGE}{keys}{STATS_COLOR}' - {values.Name} |",end="")

                        temx = GlobalTempTeam
                else:
                    print(f"\n{STATS_COLOR}  [ {STATS_COLOR2}choose the enemy to hit {STATS_COLOR}] {B} ==>",end="")
                    for keys,values in enumerate(list(GlobalTempEnemyTeam.values()),start=1):
                        print(f" {STATS_COLOR} '{ORANGE}{keys}{STATS_COLOR}' - {values.Name} |",end="")
                    
                    temx = GlobalTempEnemyTeam

                Enemy_Selected = input(f"\n{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                if Enemy_Selected.isdigit() and int(Enemy_Selected) in range(1, len(temx) + 1):
                    selected_enemy = list(temx.items())[int(Enemy_Selected) - 1]

                    if PG.Weapon.type == "Bow" and not Inventory["ARROWS"]:
                        stats_mess = [f"\n{STATS_COLOR}[ YOU DON'T HAVE ENOUGH {STATS_COLOR2}ARROW {STATS_COLOR}]\n",stats_effect]
                        break

                    if PG.Weapon.type == "Magical" or PG.Weapon.name == "Arcane Bow":
                        try:
                            mans = PG.Weapon.mana + PG.Weapon.ammo.mana
                            
                        except:
                            mans = PG.Weapon.mana
                        if PG.Mana[0] >= mans:
                            PG.Mana[0] -= mans
                        else:
                            stats_mess = [f"\n{STATS_COLOR}[ YOU DON'T HAVE ENOUGH MANA ][ {STATS_COLOR2}mana:{STATS_COLOR} YOUR MANA: {PG.Mana[0]} MANA REQUIRED: {mans} ]\n",stats_effect]
                            break
                    else:
                        mans = 0
                        if PG.Stamina[0] >= PG.Weapon.stamina:
                            PG.Stamina[0] -= PG.Weapon.stamina
                        else:
                            stats_mess = [f"\n{STATS_COLOR}[ YOU DON'T HAVE ENOUGH STAMINA ][ {STATS_COLOR2}stamina:{STATS_COLOR} YOUR STAMINA: {PG.Stamina[0]} STAMINA REQUIRED: {PG.Weapon.stamina} ]\n",stats_effect]
                            break
                    
                    if PG.Weapon.type == "Bow":
                        Arrow_Equip = PG.Weapon.ammo
                        CheckArrow = Inventory_Check(Arrow_Equip.name ,"ARROW")
                        if CheckArrow.count == 0:
                            Inventory_Remove(Arrow_Equip.name ,"ARROW")
                        elif CheckArrow.count > 0:
                            CheckArrow.count -= 1
                        if Arrow_Equip.effect != "none":
                            for efx in selected_enemy[1].TAG_Effect:
                                if efx.name == Arrow_Equip.effect:
                                    efx.duration[0] = efx.duration[1]

                    W1 = selected_enemy[1].Weapon.precision
                    W2 = 1 - selected_enemy[1].Weapon.precision
                    if selected_enemy[1].Ability == "Archer" and selected_enemy[1].Weapon.type == "Bow":
                        W1 += 0.2
                        W2 -= 0.2
                    
                    if W1 < 0:
                        W1 = 0
                    elif W1 > 1:
                        W1 = 1
                    
                    for effect in PG.TAG_Effect:
                        if effect.name == "Lowering Speed" and effect.duration[0] != 0:
                            W1 -= effect.debuf_efx
                            W2 += effect.debuf_efx

                    if PG.Armor.main_effect == "Good Aim":
                        W1 += 0.15
                        W2 -= 0.15
                    elif PG.Armor.main_effect == "Fortune":
                        fortune = random.choice([0,0.1])
                        W1 += fortune
                        W1 -= fortune

                    if W2 < 0:
                        W2 = 0
                    elif W2 > 1:
                        W2 = 1

                    W1 = round(W1,2)
                    W2 = round(W2,2)

                    if "hit" == random.choices(["hit","miss"],weights=[W1,W2],k=1)[0]:
                        
                        Damage_Logic_Return = Damage_Logic(selected_enemy[1],PG)
                        damage = Damage_Logic_Return[0]
                        if damage < 0:
                            damage = 0
                        if "Rapid" in Damage_Logic_Return[1]:
                            ability_print = [f"\n{STATS_COLOR}[ABILITY] {B}-{STATS_COLOR} [ '{STATS_COLOR2}RAPID{STATS_COLOR}' - {GlobalTempTeam[Team_Member].Name.upper()} ATTACKED TWICE ]\n",1]

                        prnt = f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ ENEMY SUCCESSFULLY HIT ][ {STATS_COLOR2}damage: {Fore.RED}-{damage}{B} - {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{mans}{B}/{Fore.YELLOW}-{PG.Weapon.stamina}{STATS_COLOR} ]\n"
                        if ability_print[1] != 0:
                            prnt += ability_print[0]
                        stats_mess = [prnt,stats_effect]

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
                            Global_Temp_Graveyard.append(GlobalTempEnemyTeam[selected_enemy[0]])
                            del GlobalTempEnemyTeam[selected_enemy[0]]
                            stats_mess = [f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ ENEMY SUCCESSFULLY HIT ][ {STATS_COLOR2}damage: {Fore.RED}-{damage}{B} - {STATS_COLOR2}mana/stamina: {Fore.CYAN}-{mans}{B}/{Fore.YELLOW}-{PG.Weapon.stamina}{STATS_COLOR} ]\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ {STATS_COLOR2}YOU HAVE DEFEATED THE ENEMY {STATS_COLOR}]\n",stats_effect]

                        break

                    else:
                        stats_mess = [f"\n{STATS_COLOR}[INFO STATS] {B}-{STATS_COLOR} [ YOU MISSED THE ENEMY ({W1}/{W2}) ][{STATS_COLOR2}mana/stamina: {Fore.CYAN}-{mans}{B}/{Fore.YELLOW}-{GlobalTempTeam[Team_Member].Weapon.stamina}{STATS_COLOR} ]\n",stats_effect]
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
        pause(0)

    return stats_mess


######################################
#                                    #
#            MAIN PROGRAM            #
#                                    #
######################################

#main program

debugmode = 0
play_music("Audio_Assets/Soundtrack/menu.wav", -1)
clear()
while True:
    create_menu("main menu",["The Journey Begins (start game)","Consult the Codex (characters)","The Scholar Tome (game guide)"],"exit")
    Main_Menu = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
    match Main_Menu:
        case "1":
            if len(CL) >= 3:
                Team = CreateTeam()
                try:
                    if len(Team) >= 3:
                        EnemyList = []
                        if lista_di_nemici_furbetti:
                            for i in lista_di_nemici_furbetti:
                                EnemyList.append(Adjust_CreateEnemy_Ammo(CreateEnemy(i)))
                            start_combat(Team,EnemyList)
                        else:
                            EnemyList = [Adjust_CreateEnemy_Ammo(CreateEnemy(Elf_Mage)),
                                        Adjust_CreateEnemy_Ammo(CreateEnemy(Goblin_Shaman)),
                                        Adjust_CreateEnemy_Ammo(CreateEnemy(Elf_Mage))]
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
                create_menu("codex menu",["Create a Character","View and Manage Characters","Open Inventory"],"back")
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
            clear()
            while True:   
                create_menu("DEBUG MENU / CHEAT",["Create 6 Random Character","Add 10 Random Weapons","Add 10 Random Armor","Add All Potions","Add All Spells","Add All Arrows","Add All Items","Add All Generic Items","Test LootTable System","Setup/choose Enemies","Disable DEBUGMODE"],"back")
                Debug_Menu = input(f"{W}  [ {GRENNI}input{Fore.WHITE} ]  ==> {Fore.BLUE}").strip()
                match Debug_Menu:
                    case "1":
                        for i in range(1,7):
                            CI[str(i)+"° Hero"] = Character(Name=str(i)+"° Hero",Race=random.choice(RaceList),Gender="UK",Age="2000",Weapon=random.choice(All_Weapons),Armor=random.choice(All_Armors))
                            CL.append(str(i)+"° Hero")
                        print(f"\n\n{Fore.CYAN}Created. {B}- Go to the Codex to see the result")
                        pause(2)
                    
                    case "2":
                        Type_Wep = input(f"{W} [ {GRAY}(1) {GRENNI}Magical / {GRAY}(2) {GRENNI}Physics / {GRAY}(3) {GRENNI}Both {W}] ==> {Fore.BLUE}").strip()
                        match Type_Wep:
                            case "1":
                                for n in range(1,11):
                                    Inventory_Insert(random.choice(Magical_Weapons),"weapon")
                            case "2":
                                for n in range(1,11):
                                    Inventory_Insert(random.choice(All_Weapon_Physics),"weapon")
                            case "3":
                                for n in range(1,11):
                                    Inventory_Insert(random.choice(All_Weapons),"weapon")

                    case "3":
                        for n in range(1,11):
                            Inventory_Insert(random.choice(All_Armors),"equip")
                    
                    case "4":
                        for n in range(1,11):
                            for potion in Potions_List:
                                Inventory_Insert(potion,"potion")
                    
                    case "5":
                        for grimoire in All_Spells:
                            Inventory_Insert(grimoire,"grimoire")
                    
                    case "6":
                        for n in range(1,11):
                            for arrow in All_Arrow:
                                Inventory_Insert(arrow,"arrow")

                    case "7":
                        for grimoire in All_Spells:
                            Inventory_Insert(grimoire,"grimoire")
                        for n in range(1,11):
                            for potion in Potions_List:
                                Inventory_Insert(potion,"potion")
                            for arrow in All_Arrow:
                                Inventory_Insert(arrow,"arrow")
                            for weapon in All_Weapons:
                                Inventory_Insert(weapon,"weapon")
                            for armor in All_Armors:
                                Inventory_Insert(armor,"equip")
                            for IT in All_Generic_Items:
                                Inventory_Insert(IT,"GENERIC")
                    
                    case "8":
                        for IT in All_Generic_Items:
                            Inventory_Insert(IT,"GENERIC")

                    case "9":
                        Type_Wep = input(f"{W} [ {GRAY}(1) {GRENNI}Base Rarity / {GRAY}(2) {GRENNI}Medium Rarity / {GRAY}(3) {GRENNI}Legendary Rarity {W}] ==> {Fore.BLUE}").strip()
                        match Type_Wep:
                            case "1":
                                DEBUGCHEST = CreateLootTable(50,GENERAL_ALL_LIST_ITEMS,"random_ten_pull",rarity)
                            case "2":
                                DEBUGCHEST = CreateLootTable(50,GENERAL_ALL_LIST_ITEMS,"random_ten_pull",rarity_medium)
                            case "3":
                                DEBUGCHEST = CreateLootTable(50,GENERAL_ALL_LIST_ITEMS,"random_ten_pull",rarity_legendary)

                        print(f"{GRAY}CHEST: '{Fore.RED}{DEBUGCHEST[0]}{GRAY}' {B}= \n")
                        print_economic = LootInsert(DEBUGCHEST[1])
                        for item in DEBUGCHEST[1]:
                            try:
                                print(f"{ColorR_E[item.R_E[0]]}{item.grigory}")
                            except:
                                print(f"{ColorR_E[item.R_E[0]]}{item.name}")
                        print(f"\n{B}> {ColorEconomic["CC"]}CC: {B}{print_economic[0]} | {ColorEconomic["BC"]}BC: {B}{print_economic[1]} | {ColorEconomic["SC"]}SC: {B}{print_economic[2]} | {ColorEconomic["GC"]}GC: {B}{print_economic[3]} | {ColorEconomic["SL"]}SL: {B}{print_economic[4]} | {ColorEconomic["GL"]}GL: {B}{print_economic[5]}")
                        print("NOW TESTING LOOTDROP")
                        ListEnemi = [Vampire_Assassin,Elf_Mage,Elf_Archer,GrayWolf,Rabbit,Bandit,Troll,Demon,Tabaxi_Warrior,Goblin_Warrior,Werewolf]
                        for enemi in ListEnemi:
                            Chestsa = CreateLootDrop(Adjust_CreateEnemy_Ammo(CreateEnemy(enemi)),"nb")
                            print(f"\nLOOTDROP: {enemi}\n\n")
                            print_economic = LootInsert(Chestsa)
                            for item in Chestsa:
                                
                                try:
                                    if isinstance(item,list):
                                        print(item)
                                    else:
                                        print(f"{ColorR_E[item.R_E[0]]}{item.grigory}")
                                except:
                                    if isinstance(item,list):
                                        print(item)
                                    else:
                                        print(f"{ColorR_E[item.R_E[0]]}{item.name}")
                            print(f"\n{B}> {ColorEconomic["CC"]}CC: {B}{print_economic[0]} | {ColorEconomic["BC"]}BC: {B}{print_economic[1]} | {ColorEconomic["SC"]}SC: {B}{print_economic[2]} | {ColorEconomic["GC"]}GC: {B}{print_economic[3]} | {ColorEconomic["SL"]}SL: {B}{print_economic[4]} | {ColorEconomic["GL"]}GL: {B}{print_economic[5]}")
                            pause(1)

                    case "10":
                        lista_di_nemici_furbetti = []
                        create_menu("Choose The Enemy",all_enemies,"invia EXIT, NON IL NUMERO")
                        while True:
                            EC = input("input: ")
                            if EC in ["EXIT","exit","Exit"]:
                                break
                            else:
                                for idx,enemis in enumerate(all_enemies,start=1):
                                    if int(EC) == idx:
                                        lista_di_nemici_furbetti.append(enemis)
                                        print("hai scelto:")
                                        print(enemis)
                            
                    case "11":

                        if debugmode == 1:
                            debugmode = 0
                            print(f"\n{Fore.CYAN}DEBUGMODE {B}- disable")
                            pause(2)
                        else:
                            debugmode = 1
                            print(f"\n{Fore.CYAN}DEBUGMODE {B}- enable")
                            pause(2)
                    case "12":
                        break

                    case _:
                        continue