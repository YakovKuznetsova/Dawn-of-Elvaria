import random
import copy

##############################################
# WEAPON CLASSES                             #

class Weapons:
    def __init__(self,name,damage,velocity,mana,stamina,precision,ammo,type,element,grade,R_E):
        self.name = name
        self.damage = damage
        self.velocity = velocity
        self.mana = mana
        self.stamina = stamina
        self.precision = precision
        self.ammo = ammo
        self.type = type
        self.effect = element
        self.grade = grade
        self.element = element
        self.R_E = R_E
        self.count = 1

        if ammo != "nb" and type != "Magical":
            self.damage += ammo.dmg
    
    def Weapon_Effect(self, damage, velocity, mana, stamina, precision, effect):
        self.damage += damage
        self.velocity += velocity
        self.mana += mana
        self.stamina += stamina
        self.precision += precision
        self.effect = effect
        
    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} | Damage: {self.damage} | Velocity: {self.velocity} | Mana: {self.mana} | Stamina: {self.stamina} | Precision: {self.precision}"

##############################################
# TAG EFFECT

class Effect:
    def __init__(self, name, buff_efx, debuf_efx, duration, element):
        self.name = name
        self.buff_efx = buff_efx
        self.debuf_efx = debuf_efx
        self.duration = duration
        self.element = element

    def update_duration(self):
        if self.duration[0] > 0:
            self.duration[0] -= 1
        
    def copy(self):
        return copy.deepcopy(self)
    
##############################################
# ARMOR CLASSES                              #

class Armor:
    def __init__(self,name,mod_stamina,mod_mana,armor,passive_effect,main_effect,protection,R_E):
        self.name = name
        self.mod_stamina = mod_stamina
        self.mod_mana = mod_mana
        self.armor = armor
        self.passive_effect = passive_effect
        self.main_effect = main_effect
        self.protection = protection
        self.R_E = R_E
        self.count = 1

    def copy(self):
        return copy.deepcopy(self)


##############################################
# AMMO CLASSES                              #

class Arrow:
    def __init__(self, dmg, name, count, effect, R_E):
        self.dmg = dmg
        self.name = name
        self.count = count
        self.effect = effect
        self.R_E = R_E

class Magic:
    def __init__(self,damage,grigory,mana,name,elemental,main_effect,secondary_effect,grade,R_E):
        self.damage = damage
        self.grigory = grigory
        self.mana = mana
        self.name = name
        self.elemental = elemental
        self.main_effect = main_effect
        self.secondary_effect = secondary_effect
        self.grade = grade
        self.R_E = R_E

##############################################
# POTION / FOODS CLASSES                     #

class Potions_Foods:
    def __init__(self,name,mod_mana,mod_stamina,mod_hp,effect,count,R_E):
        self.name = name
        self.mod_mana = mod_mana
        self.mod_stamina = mod_stamina
        self.mod_hp = mod_hp
        self.effect = effect
        self.count = count
        self.R_E = R_E

##############################################
# OBJECT - ECONOMY - ALTRO                   #

class obj:
    def __init__(self,name,mods,effect,R_E):
        self.name = name
        self.mods = mods
        self.effect = effect
        self.count = 1
        self.R_E = R_E

CopperCoin = obj(
    name = "Copper Coin",
    mods = "nb",
    effect = "nb",
    R_E = ["common",1]
)

BronzeCoin = obj(
    name = "Bronze Coin",
    mods = "nb",
    effect = "nb",
    R_E = ["common",2]
)

SilverCoin = obj(
    name = "Silver Coin",
    mods = "nb",
    effect = "nb",
    R_E = ["uncommon",5]
)

GoldCoin = obj(
    name = "Gold Coin",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",10]
)

SilverLingot = obj(
    name = "Silver Lingot",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",25]
)

GoldLingot = obj(
    name = "Gold Lingot",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",50]
)

ObsidianShard = obj(
    name = "Obsidian Shard",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",8]
)

CrystalShard = obj(
    name = "Crystal Shard",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",14]
)

RoughRuby = obj(
    name = "Rough Ruby",
    mods = "nb",
    effect = "nb",
    R_E = ["uncommon",4]
)

Ruby = obj(
    name = "Ruby",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",8]
)

PureRuby = obj(
    name = "Ruby",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",12]
)

Emerald = obj(
    name = "Emerald",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",11]
)

RoughAmethyst = obj(
    name = "Rough Amethyst",
    mods = "nb",
    effect = "nb",
    R_E = ["uncommon",3]
)

Amethyst = obj(
    name = "Amethyst",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",6]
)

PureAmethyst = obj(
    name = "Pure Amethyst",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",9]
)

Topaz = obj(
    name = "Topaz",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",8]
)

OpalPearl = obj(
    name = "Opal Pearl",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",9]
)

AnimalClaws = obj(
    name = "Animal Claws",
    mods = "nb",
    effect = "nb",
    R_E = ["uncommon",2]
)

Diamond = obj(
    name = "Diamond",
    mods = "nb",
    effect = "nb",
    R_E = ["legendary",40]
)

PureCrystal = obj(
    name = "Pure Crystal",
    mods = "nb",
    effect = "nb",
    R_E = ["legendary",30]
)

SilverNecklace = obj(
    name = "Silver Necklace",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",12]
)

GoldNecklace = obj(
    name = "Gold Necklace",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",16]
)

GemstoneNecklace = obj(
    name = "Gemstone Necklace",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",14]
)

WoodScraps = obj(
    name = "Wood Scraps",
    mods = "nb",
    effect = "nb",
    R_E = ["common",1]
)

BrokenVial = obj(
    name = "Broken Vial",
    mods = "nb",
    effect = "nb",
    R_E = ["uncommon",1]
)

Skull = obj(
    name = "Skull",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",6]
)

VampirismBook = obj(
    name = "Vampirism Book",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",16]
)

MasterVampirismBook = obj(
    name = "Master Vampirism Book",
    mods = "nb",
    effect = "Vampirism",
    R_E = ["epic",34]
)

VampireTooth = obj(
    name="Vampire Tooth",
    mods = "nb",
    effect = "Vampirism",
    R_E = ["uncommon",3]      
)

Bone = obj(
    name = "Bone",
    mods = "nb",
    effect = "nb",
    R_E = ["common",2]
)

AnimalFur = obj(
    name = "Animal Fur",
    mods = "nb",
    effect = "nb",
    R_E = ["uncommon",4]
)

AnimalHide = obj(
    name = "Animal Hide",
    mods = "nb",
    effect = "nb",
    R_E = ["common",2]
)

PrestigeFur = obj(
    name = "Prestige Fur",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",8]
)

GoddessAmulet = obj(
    name = "Goddess Amulet",
    mods = "nb",
    effect = "nb",
    R_E = ["uncommon",7]
)

FaithNecklace = obj(
    name = "Faith Necklace",
    mods = "nb",
    effect = "nb",
    R_E = ["common",4]
)

ForestFaithAmulet = obj(
    name = "Forest Faith Amulet",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",7]
)

PaganAmulet = obj(
    name = "Pagan Amulet",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",13]
)

IronRing = obj(
    name = "Iron Ring",
    mods = "nb",
    effect = "nb",
    R_E = ["common",2]
)

SilverRing = obj(
    name = "Silver Ring",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",6]
)

GoldRing = obj(
    name = "Gold Ring",
    mods = "nb",
    effect = "nb",
    R_E = ["epic",11]
)

RubyRing = obj(
    name = "Ruby Ring",
    mods = "nb",
    effect = "nb",
    R_E = ["rare",9]
)

DiamondRing = obj(
    name = "Diamond Ring",
    mods = "nb",
    effect = "nb",
    R_E = ["legendary",45]
)

Crown = obj(
    name = "Crown",
    mods = "nb",
    effect = "nb",
    R_E = ["legendary",145]
)

ScrapAnimal = obj(
    name = "Scrap Animal",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

CookingPot = obj(
    name = "Cooking Pot",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 3]
)

Rope = obj(
    name = "Rope",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 2]
)

Lantern = obj(
    name = "Lantern",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 4]
)

LeatherPouch = obj(
    name = "Leather Pouch",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 2]
)

FlintAndSteel = obj(
    name = "Flint and Steel",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 5]
)

HerbalKit = obj(
    name = "Herbal Kit",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 10]
)

Candles = obj(
    name = "Candles",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

Inkwell = obj(
    name = "Inkwell",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 3]
)

SilkHandkerchief = obj(
    name = "Silk Handkerchief",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

SmallBell = obj(
    name = "Small Bell",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

ThreadAndNeedle = obj(
    name = "Thread and Needle",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 2]
)

SmallMirror = obj(
    name = "Small Mirror",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 4]
)

FlaskOfWine = obj(
    name = "Flask of Wine",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 5]
)

Bucket = obj(
    name = "Bucket",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 2]
)

PouchOfSalt = obj(
    name = "Pouch of Salt",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 8]
)

VialOfPerfume = obj(
    name = "Vial of Perfume",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 7]
)

PocketWatch = obj(
    name = "Pocket Watch",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 6]
)

Whistle = obj(
    name = "Whistle",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

PatchOfCloth = obj(
    name = "Patch of Cloth",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

GlassBottle = obj(
    name = "Glass Bottle",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

Scarf = obj(
    name = "Scarf",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 2]
)

Locket = obj(
    name = "Locket",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 2]
)

BurntBook = obj(
    name = "Burnt Book",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 0]
)

IronScraps = obj(
    name = "Iron Scraps",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

BrokenWeapon = obj(
    name = "Broken Weapon",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

BrokenArmor = obj(
    name = "Broken Armor",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

FracturedAmulet = obj(
    name = "Fractured Amulet",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

RustyRing = obj(
    name = "Rusty Ring",
    mods = "nb",
    effect = "nb",
    R_E = ["common", 1]
)

##############################################
# ARMOR                                      #

No_Armor = Armor(
    name = "None",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb", #effetto passivo, cioè magari una riduzione/aumento dell'attacco o bho
    main_effect = "nb", #abilità effettiva tipo rapid
    protection = "nb", #special element protection
    R_E = ["common",0] #rarity and economic value
)

Slave_Rags = Armor(
    name = "Slave Rags",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "Weakness",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",0]
)

Cloth_Garments = Armor(
    name = "Cloth Garments",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",2]
)

Elf_Robe = Armor(
    name = "Elf Robe",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",5]
)

Elegant_Clothes = Armor(
    name = "Elegant Clothes",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["uncommon",6]
)

Poor_Clothes = Armor(
    name = "Poor Clothes",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",1]
)

Leather_Garments = Armor(
    name = "Leather Garments",
    armor = [5,5],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",5]
)

Merchant_Attire = Armor(
    name = "Merchant Attire",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",4]
)

Peasant_Tunic = Armor(
    name = "Peasant Tunic",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",2]
)

Scholars_Robe = Armor(
    name = "Scholar's Robe",
    armor = [0,0],
    mod_mana = 5,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",2]
)

Bards_Costume = Armor(
    name = "Bard's Costume",
    armor = [0,0],
    mod_mana = 0,
    mod_stamina = 5,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",4]
)

Work_Tunic = Armor(
    name = "Work Tunic",
    armor = [5,5],
    mod_mana = 0,
    mod_stamina = 15,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",5]
)

Leather_Armor = Armor(
    name = "Leather Armor",
    armor = [8,8],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "Electro",
    R_E = ["common",10]
)

Wooden_Armor = Armor(
    name = "Wooden Armor",
    armor = [14,14],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "Wood",
    main_effect = "nb",
    protection = "Nature",
    R_E = ["common",10]
)

Paper_Armor = Armor(
    name = "Paper Armor",
    armor = [12,12],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "Anti Arrow",
    main_effect = "nb",
    protection = "Electro",
    R_E = ["rare",18]
)

Studded_Armor = Armor(
    name = "Studded Armor",
    armor = [16,16],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",12]
)

Thiefs_Robes = Armor(
    name = "Thief's Robes",
    armor = [12,12],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "Thief's Rapid",
    protection = "nb",
    R_E = ["uncommon",15]
)

Archers_Robes = Armor(
    name = "Archer's Robes",
    armor = [8,8],
    mod_mana = 0,
    mod_stamina = 15,
    passive_effect = "nb",
    main_effect = "Good Aim",
    protection = "nb",
    R_E = ["uncommon",15]
)

Goblin_Mail = Armor(
    name = "Goblin Mail",
    armor = [10,10],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",6]
)

Iron_Chainmail = Armor(
    name = "Iron Chainmail",
    armor = [18,18],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "Rock",
    R_E = ["common",16]
)

Bandit_Armor = Armor(
    name = "Bandit Armor",
    armor = [20,20],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",16]
)

Trollhide_Armor = Armor(
    name = "Trollhide Armor",
    armor = [15,15],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "Good Aim",
    protection = "Fire",
    R_E = ["rare",24]
)

Orcish_Armor = Armor(
    name = "Orcish Armor",
    armor = [20,20],
    mod_mana = 0,
    mod_stamina = 10,
    passive_effect = "Lowering Speed",
    main_effect = "nb",
    protection = "nb",
    R_E = ["uncommon",20]
)

Warriors_Armor = Armor( 
    name = "Warrior's Armor",
    armor = [20,20],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["uncommon",20]
)

Bone_Armor = Armor(
    name = "Bone Armor",
    armor = [25,25],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "Lowering Speed",
    main_effect = "nb",
    protection = "Fire",
    R_E = ["rare",24]
)

Nobles_Armor = Armor(
    name = "Noble's Armor",
    armor = [25,25],
    mod_mana = 5,
    mod_stamina = 5,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["rare",30]
)

Dwarven_Armor = Armor(
    name = "Dwarven Armor",
    armor = [25,25],
    mod_mana = 0,
    mod_stamina = 10,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["uncommon",20]
)

Elven_Armor = Armor(
    name = "Elven Armor",
    armor = [25,25],
    mod_mana = 10,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["uncommon",20]
)

Vampiric_Armor = Armor(
    name = "Vampiric Armor",
    armor = [30,30],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "Light",
    R_E = ["uncommon",20]
)

Knights_Armor = Armor(
    name = "Knight's Armor",
    armor = [30,30],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["rare",32]
)

Heavy_War_Armor = Armor(
    name = "Heavy War Armor",
    armor = [35,35],
    mod_mana = 0,
    mod_stamina = 0,
    passive_effect = "Lowering Speed",
    main_effect = "nb",
    protection = "nb",
    R_E = ["rare",32]
)

Demonic_Armor = Armor(
    name = "Demonic Armor",
    armor = [35,35],
    mod_mana = 10,
    mod_stamina = 10,
    passive_effect = "Lowering Speed",
    main_effect = "Endurance",
    protection = "Fire",
    R_E = ["uncommon",24]
)

Heavy_Elven_Armor = Armor(
    name = "Heavy Elven Armor",
    armor = [35,35],
    mod_mana = 15,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "Darkness",
    R_E = ["rare",32]
)

Ebony_Armor = Armor(
    name = "Ebony Armor",
    armor = [45,45],
    mod_mana = 0,
    mod_stamina = 15,
    passive_effect = "Lowering Speed",
    main_effect = "nb",
    protection = "Rock",
    R_E = ["epic",130]
)

Heros_Armor = Armor(
    name = "Hero's Armor",
    armor = [45,45],
    mod_mana = 0,
    mod_stamina = 15,
    passive_effect = "Lowering Speed",
    main_effect = "Fortune",
    protection = "Darkness",
    R_E = ["epic",132]
)

Mithril_Armor = Armor(
    name = "Mithril Armor",
    armor = [55,55],
    mod_mana = 15,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "nb",
    R_E = ["rare",85]
)

Dragon_Scale_Armor = Armor(
    name = "Dragon Scale Armor",
    armor = [70,70],
    mod_mana = 15,
    mod_stamina = 20,
    passive_effect = "Lowering Speed",
    main_effect = "Endurance",
    protection = "Fire",
    R_E = ["legendary",220]
)

Legendary_Armor = Armor(
    name = "Legendary Armor",
    armor = [85,85],
    mod_mana = 25,
    mod_stamina = 25,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "Darkness",
    R_E = ["mythical",380]
)

Novice_Mages_Garments = Armor(
    name = "Novice Mage's Garments",
    armor = [0,0],
    mod_mana = 15,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",10]
)

Acolytes = Armor(
    name = "Acolytes",
    armor = [0,0],
    mod_mana = 15,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "nb",
    R_E = ["uncommon",14]
)

Monks_Tunic = Armor(
    name = "Monk's Tunic",
    armor = [0,0],
    mod_mana = 20,
    mod_stamina = 0,
    passive_effect = "nb",
    main_effect = "nb",
    protection = "Darkness",
    R_E = ["common",10]
)

Mages_Robes = Armor(
    name = "Mage's Robes",
    armor = [5,5],
    mod_mana = 20,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "nb",
    R_E = ["common",16]
)

Necromancers_Robes = Armor(
    name = "Necromancer's Robes",
    armor = [10,10],
    mod_mana = 15,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "Light",
    R_E = ["rare",24]
)

Priests_Garments = Armor(
    name = "Priest's Garments",
    armor = [5,5],
    mod_mana = 20,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "Darkness",
    R_E = ["uncommon",20]
)

Masters_Robes = Armor(
    name = "Master's Robes",
    armor = [25,25],
    mod_mana = 30,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "nb",
    R_E = ["rare",38]
)

Sacerdos_Robes = Armor(
    name = "Sacerdos's Robes",
    armor = [25,25],
    mod_mana = 30,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "Darkness",
    R_E = ["rare",38]
)

Golden_Armor = Armor(
    name = "Golden Armor",
    armor = [35,35],
    mod_mana = 40,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "nb",
    R_E = ["epic",100]
)

Elemental_Armor = Armor(
    name = "Elemental Armor",
    armor = [45,45],
    mod_mana = 55,
    mod_stamina = 0,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "Water",
    R_E = ["legendary",275]
)

Crystal_Armor = Armor(
    name = "Crystal Armor",
    armor = [65,65],
    mod_mana = 70,
    mod_stamina = 10,
    passive_effect = "Magical",
    main_effect = "nb",
    protection = "Electro",
    R_E = ["mythical",390]
)

##############################################
# EFFECTS

Vampirism = Effect(
    name = "Vampirism",
    buff_efx = 0,
    debuf_efx = 0,
    duration = [0,5],
    element = "nb"
)

Burn = Effect(
    name = "Burn",
    buff_efx = 0,
    debuf_efx= 5,
    duration= [0,3],
    element= "fire"
)

Strength = Effect(
    name = "Strength",
    buff_efx = 15,
    debuf_efx= 0,
    duration= [0,4],
    element= "nb"
)

Potent_Strength = Effect(
    name = "Potent Strength",
    buff_efx = 25,
    debuf_efx= 0,
    duration= [0,3],
    element= "nb"
)

Resistance = Effect(
    name = "Resistance",
    buff_efx = 0,
    debuf_efx= 20,
    duration= [0,3],
    element= "nb"
)

Poison = Effect(
    name = "Poison",
    buff_efx = 0,
    debuf_efx= 2,
    duration= [0,4],
    element= "nb"
)

Potent_Poison = Effect(
    name = "Potent Poison",
    buff_efx = 0,
    debuf_efx= 4,
    duration= [0,4],
    element= "nb"
)

Frost = Effect(
    name = "Frost",
    buff_efx = 0,
    debuf_efx= 5,
    duration= [0,3],
    element= "water"
)

Regen = Effect(
    name = "Regen",
    buff_efx = 8,
    debuf_efx= 0,
    duration= [0,4],
    element= "nb"
)

Healing1 = Effect(
    name = "Healing",
    buff_efx = 50,
    debuf_efx= 0,
    duration= [0,2],
    element= "nb"
)

Strong_Healing = Effect(
    name = "Strong Healing",
    buff_efx = 75,
    debuf_efx= 0,
    duration= [0,2],
    element= "nb"
)

Shield = Effect(
    name = "Shield [+30]",
    buff_efx = 30,
    debuf_efx= 0,
    duration= [0,2],
    element= "nb"
)

Strong_Shield = Effect(
    name = "Strong Shield [+60]",
    buff_efx = 60,
    debuf_efx= 0,
    duration= [0,2],
    element= "nb"
)

Weakness = Effect(
    name = "Weakness",
    buff_efx = 0,
    debuf_efx= 35, #  %
    duration= [0,3],
    element= "nb"
)

Magical = Effect(
    name = "Magical",
    buff_efx = 4,
    debuf_efx= 0,
    duration= [0,4],
    element= "nb"
)

Lowering_Speed = Effect(
    name = "Lowering Speed",
    buff_efx = 0,
    debuf_efx= 0.1,
    duration= [0,2],
    element= "nb"
)

Anti_Arrow = Effect(
    name = "Anti Arrow",
    buff_efx = 0,
    debuf_efx= 10,
    duration= [0,3],
    element= "nb"
)

Wood = Effect(
    name = "Wood",
    buff_efx = 0,
    debuf_efx= 5,
    duration= [0,2],
    element= "nb"
)


##############################################
# AMMO

IronArrow = Arrow(dmg=5,name="Iron Arrow",count=1,effect="none",R_E=["common",1])
BoneArrow = Arrow(dmg=7,name="Bone Arrow",count=1,effect="none",R_E=["common",2])
ElfArrow = Arrow(dmg=8,name="Bone Arrow",count=1,effect="none",R_E=["uncommon",3])
SteelArrow = Arrow(dmg=8,name="Steel Arrow",count=1,effect="none",R_E=["common",2])
GlassArrow = Arrow(dmg=10,name="Glass Arrow",count=1,effect="none",R_E=["rare",4])
CrystalArrow = Arrow(dmg=12,name="Crystal Arrow",count=1,effect="none",R_E=["epic",8])
FlamingArrow = Arrow(dmg=6,name="Flaming Arrow",count=1,effect="Burn",R_E=["uncommon",3])
IcyArrow = Arrow(dmg=6,name="Icy Arrow",count=1,effect="Frost",R_E=["uncommon",3])
PoisonArrow = Arrow(dmg=5,name="Poison Arrow",count=1,effect="Poison",R_E=["rare",4])
WeaknessArrow = Arrow(dmg=8,name="Weakness Arrow",count=1,effect="Weakness",R_E=["rare",4])
AbyssalArrow = Arrow(dmg=13,name="Abyssal Arrow",count=1,effect="none",R_E=["epic",10])


##############################################
# MAGIC

MagicBurst = Magic(
    damage = [8,12,16,20],
    mana = 12,
    grigory = "Magic Burst",
    elemental = "light",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","nb"],
    grade = 1,
    name = ["Base Magic Burst","Magic Burst","Charged Magic Burst","Potent Magic Burst"],
    R_E = ["common",1]
)

Fireball = Magic(
    damage = [16,18,20,24],
    mana = 12,
    grigory = "Fireball",
    elemental = "fire",
    main_effect = "nb",
    secondary_effect = ["Burn","Burn","Burn","Burn"],
    grade = 1,
    name = ["Fireball","Charged Fireball","Explosive Fireball","Meteor Fireball"],
    R_E = ["common",5]
)

FlameBurst = Magic(
    damage = [0,20,22,24],
    mana = 16,
    grigory = "Flame Burst",
    elemental = "fire",
    main_effect = "nb",
    secondary_effect = ["nb","Burn","Burn","Burn"],
    grade = 2,
    name = ["nb","Flame Burst","Explosive Burst","Fire Nova"],
    R_E = ["uncommon",20]    
)

BurningVortex = Magic(
    damage = [0,0,30,34],
    mana = 20,
    grigory = "Burning Vortex",
    elemental = "fire",
    main_effect = "nb",
    secondary_effect = ["nb","nb","Burn","Burn"],
    grade = 3,
    name = ["nb","nb","Burning Vortex","Infernal Vortex"],
    R_E = ["rare",64]    
)

FlameTempest = Magic(
    damage = [0,0,0,38],
    mana = 28,
    grigory = "Flame Tempest",
    elemental = "fire",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Burn"],
    grade = 4,
    name = ["nb","nb","nb","Flame Tempest"],
    R_E = ["legendary",340]      
)

WaterJet = Magic(
    damage = [14,16,18,22],
    mana = 11,
    grigory = "WaterJet",
    elemental = "water",
    main_effect = "nb",
    secondary_effect = ["nb","nb","Frost","Frost"],
    grade = 1,
    name = ["Waterball","WaterJet","Freezing Spray","Freezing Spike"],
    R_E = ["common",5] 
)

FlowingRain = Magic(
    damage = [0,0,0,0],
    mana = 14,
    grigory = "Flowing Rain",
    elemental = "water",
    main_effect = "nb",
    secondary_effect = ["nb","Resistance","Strength","Potent Strength"],
    grade = 2,
    name = ["nb","Raining Rain","Flowing Rain","Flowing Grace"],
    R_E = ["uncommon",20]    
)

TidalBlessing = Magic(
    damage = [0,0,12,16],
    mana = 22,
    grigory = "Tidal Blessing",
    elemental = "water",
    main_effect = "nb",
    secondary_effect = ["nb","nb","Resistance","Strength"],
    grade = 3,
    name = ["nb","nb","Tidal Blessing","Sea Blessing"],
    R_E = ["rare",64]      
)

OceanEmbrance = Magic(
    damage = [0,0,0,24],
    mana = 40,
    grigory = "Ocean Embrance",
    elemental = "water",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Potent Strength"],
    grade = 4,
    name = ["nb","nb","nb","Ocean Embrance"],
    R_E = ["legendary",340]          
)

StoneFist = Magic(
    damage = [15,17,19,23],
    mana = 12,
    grigory = "Stone Fist",
    elemental = "rock",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Weakness"],
    grade = 1,
    name = ["Cobble Fist","Stone Fist","Jagged Stone Fist","Spike Fist"],
    R_E = ["common",5]    
)

GraniteShield = Magic(
    damage = [0,0,0,0],
    mana = 16,
    grigory = "Granite Shield",
    elemental = "rock",
    main_effect = "nb",
    secondary_effect = ["nb","Resistance","Shield","Strong Shield"],
    grade = 2,
    name = ["nb","Rocky Barrier","Granite Shield","Eternal Bulwark"],
    R_E = ["uncommon",20]    
)

Rockfall = Magic(
    damage = [0,0,25,30],
    mana = 20,
    grigory = "Rockfall",
    elemental = "rock",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Resistance"],
    grade = 3,
    name = ["nb","nb","Rockfall","Stonebreaker"],
    R_E = ["rare",64]      
)

TitanImpact = Magic(
    damage = [0,0,0,34],
    mana = 20,
    grigory = "Titan Impact",
    elemental = "rock",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Shield"],
    grade = 4,
    name = ["nb","nb","nb","Titan Impact"],
    R_E = ["legendary",340]          
)

VineWhip = Magic(
    damage = [15,16,18,22],
    mana = 11,
    grigory = "Vine Whip",
    elemental = "nature",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Poison"],
    grade = 1,
    name = ["Vine Whip","Entangling Vine","Growing Vine Whip","Poisoned Vine Whip"],
    R_E = ["common",5]    
)

RestorativeGrowth = Magic(
    damage = [0,0,0,2],
    mana = 16,
    grigory = "Restorative Growth",
    elemental = "nature",
    main_effect = "nb",
    secondary_effect = ["nb","Magical","Regen","Strength"],
    grade = 2,
    name = ["nb","Verdant Foliage","Restorative Growth","Vigorous Growth"],
    R_E = ["uncommon",20]    
)

VitalBloom = Magic(
    damage = [0,0,6,12],
    mana = 25,
    grigory = "Vital Bloom",
    elemental = "nature",
    main_effect = "nb",
    secondary_effect = ["nb","nb","Healing","Strong Healing"],
    grade = 3,
    name = ["nb","nb","Vital Bloom","Verdant Vital Bloom"],
    R_E = ["rare",64]      
)

CallOfTheForest = Magic(
    damage = [0,0,0,22],
    mana = 36,
    grigory = "Call Of The Forest",
    elemental = "nature",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Strong Healing"],
    grade = 4,
    name = ["nb","nb","nb","Call Of The Forest"],
    R_E = ["legendary",340]          
)

LightingBolt = Magic(
    damage = [16,20,22,24],
    mana = 12,
    grigory = "Lighting Bolt",
    elemental = "electro",
    main_effect = "nb",
    secondary_effect = ["Burn","nb","nb","Burn"],
    grade = 1,
    name = ["Sparks Spray","Lighting Bolt","Lightning","Explosive Lightning"],
    R_E = ["common",5]    
)

VoltStrike = Magic(
    damage = [0,26,28,30],
    mana = 16,
    grigory = "Volt Strike",
    elemental = "electro",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Burn"],
    grade = 2,
    name = ["nb","Volt Strike","Overload Pulse","Volt Cataclysm"],
    R_E = ["uncommon",20]    
)

TempestSurge = Magic(
    damage = [0,0,35,38],
    mana = 20,
    grigory = "Tempest Surge",
    elemental = "electro",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Burn"],
    grade = 3,
    name = ["nb","nb","Volt Cascade","Tempest Surge"],
    R_E = ["rare",64]      
)

ElectroNova = Magic(
    damage = [0,0,0,45],
    mana = 28,
    grigory = "Electro Nova",
    elemental = "electro",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","nb"],
    grade = 4,
    name = ["nb","nb","nb","Electro Nova"],
    R_E = ["legendary",340]          
)

RadiantStrike = Magic(
    damage = [16,18,20,22],
    mana = 11,
    grigory = "Radiant Strike",
    elemental = "light",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Burn"],
    grade = 1,
    name = ["Light Flash","Radiant Strike","Piercing Radiant","Explosive Flash"],
    R_E = ["common",4]
)

Healing = Magic(
    damage = [0,0,0,0],
    mana = 14,
    grigory = "Healing",
    elemental = "light",
    main_effect = "nb",
    secondary_effect = ["Weak Healing","Healing","Potent Healing","Divine Healing"],
    grade = 2,
    name = ["nb","Regen","Healing","Strong Healing"],
    R_E = ["uncommon",16]
)

FaithShield = Magic(
    damage = [0,0,0,0],
    mana = 20,
    grigory = "Faith Shield",
    elemental = "light",
    main_effect = "nb",
    secondary_effect = ["nb","nb","Shield","Strong Shield"],
    grade = 3,
    name = ["nb","nb","For Faith Shield","For The Goddes Shield"],
    R_E = ["rare",46]  
)

GoddesBlessing = Magic(
    damage = [0,0,0,34],
    mana = 32,
    grigory = "Goddes Blessing",
    elemental = "light",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Resistance"],
    grade = 4,
    name = ["nb","nb","nb","Goddes Blessing"],
    R_E = ["legendary",280]      
)

DarkBolt = Magic(
    damage = [18,20,22,26],
    mana = 16,
    grigory = "Dark Bolt",
    elemental = "darkness",
    main_effect = "nb",
    secondary_effect = ["nb","nb","Frost","Weakness"],
    grade = 1,
    name = ["Shadow Fist","Dark Bolt","Darkness Touch","Sapping Dark Bolt"],
    R_E = ["common",14]    
)

ShadowAbyss = Magic(
    damage = [0,28,36,40],
    mana = 26,
    grigory = "Shadow Abyss",
    elemental = "darkness",
    main_effect = "nb",
    secondary_effect = ["nb","Frost","Frost","Weakness"],
    grade = 2,
    name = ["nb","Abyssal Shard","Shadow Abyss","Eternal Abyss"],
    R_E = ["uncommon",62]    
)

CorruptionBloom = Magic(
    damage = [0,0,26,36],
    mana = 48,
    grigory = "Corruption Bloom",
    elemental = "darkness",
    main_effect = "nb",
    secondary_effect = ["nb","nb","Poison","Potent Poison"],
    grade = 3,
    name = ["nb","nb","Corruption Bloom","Pestilent Dominion"],
    R_E = ["rare",162]      
)

BlackHole = Magic(
    damage = [0,0,0,100],
    mana = 78,
    grigory = "Black Hole",
    elemental = "darkness",
    main_effect = "nb",
    secondary_effect = ["nb","nb","nb","Frost"],
    grade = 4,
    name = ["nb","nb","nb","Black Hole"],
    R_E = ["legendary",485]          
)

##############################################
# POTIONS & FOODS

RawMeat = Potions_Foods(
    name="Raw Meat",
    mod_hp=5,
    mod_mana=0,
    mod_stamina=10,
    effect="NB",
    count=1,
    R_E = ["common",2]      
)

Blood = Potions_Foods(
    name="Blood",
    mod_hp=0,
    mod_mana=5,
    mod_stamina=5,
    effect="Poison",
    count=1,
    R_E = ["common",1]      
)

VampireBloodJar = Potions_Foods(
    name="Vampire Blood Jar",
    mod_hp=25,
    mod_mana=25,
    mod_stamina=25,
    effect="Vampirism",
    count=1,
    R_E = ["uncommon",3]      
)

Weak_Healing_Potion = Potions_Foods(
    name="Weak Healing Potion",
    mod_hp=25,
    mod_mana=0,
    mod_stamina=0,
    effect="NB",
    count=1,
    R_E = ["common",3]      
)

Healing_Potion = Potions_Foods(
    name="Healing Potion",
    mod_hp=50,
    mod_mana=0,
    mod_stamina=0,
    effect="NB",
    count=1,
    R_E = ["common",5] 
)

Strong_Healing_Potion = Potions_Foods(
    name="Strong Healing Potion",
    mod_hp=75,
    mod_mana=0,
    mod_stamina=0,
    effect="NB",
    count=1,
    R_E = ["uncommon",15] 
)

Weak_Restore_Potion = Potions_Foods(
    name="Weak Restore Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=20,
    effect="NB",
    count=1,
    R_E = ["common",3] 
)

Restore_Potion = Potions_Foods(
    name="Restore Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=40,
    effect="NB",
    count=1,
    R_E = ["common",5] 
)

Strong_Restore_Potion = Potions_Foods(
    name="Strong Restore Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=60,
    effect="NB",
    count=1,
    R_E = ["uncommon",15] 
)

Weak_Mana_Potion = Potions_Foods(
    name="Weak Mana Potion",
    mod_hp=0,
    mod_mana=20,
    mod_stamina=0,
    effect="NB",
    count=1,
    R_E = ["common",3] 
)

Mana_Potion = Potions_Foods(
    name="Mana Potion",
    mod_hp=0,
    mod_mana=40,
    mod_stamina=75,
    effect="NB",
    count=1,
    R_E = ["common",5] 
)

Strong_Mana_Potion = Potions_Foods(
    name="Strong Mana Potion",
    mod_hp=0,
    mod_mana=60,
    mod_stamina=75,
    effect="NB",
    count=1,
    R_E = ["uncommon",15] 
)

Strength_Potion = Potions_Foods(
    name="Strength Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Strength",
    count=1,
    R_E = ["common",10] 
)

Potent_Strength_Potion = Potions_Foods(
    name="Potent Strength Potion",
    mod_hp=10,
    mod_mana=0,
    mod_stamina=0,
    effect="Potent Strength",
    count=1,
    R_E = ["rare",25] 
)

Resistance_Potion = Potions_Foods(
    name="Resistance Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Resistance",
    count=1,
    R_E = ["uncommon",15] 
)

Regen_Potion = Potions_Foods(
    name="Regen Potion",
    mod_hp=5,
    mod_mana=0,
    mod_stamina=0,
    effect="Regen",
    count=1,
    R_E = ["common",6] 
)

Frost_Potion = Potions_Foods(
    name="Frost Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Frost",
    count=1,
    R_E = ["common",5] 
)

Poison_Potion = Potions_Foods(
    name="Poison Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Poison",
    count=1,
    R_E = ["common",15] 
)

Potent_Poison_Potion = Potions_Foods(
    name="Potent Poison Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Potent Poison",
    count=1,
    R_E = ["rare",35] 
)

Burn_Potion = Potions_Foods(
    name="Burn Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Burn",
    count=1,
    R_E = ["common",5] 
)

Weakness_Potion = Potions_Foods(
    name="Weakness Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Weakness",
    count=1,
    R_E = ["uncommon",15] 
)

Recovery_Mana = Potions_Foods(
    name="Recovery Mana Potion",
    mod_hp=0,
    mod_mana=15,
    mod_stamina=0,
    effect="Magical",
    count=1,
    R_E = ["common",8] 
)

Anti_Arrow_Potion = Potions_Foods(
    name="Anti Arrow Potion",
    mod_hp=0,
    mod_mana=0,
    mod_stamina=0,
    effect="Anti Arrow",
    count=1,
    R_E = ["uncommon",15] 
)

##############################################
# WEAPON SET BASE

Punch = Weapons(name="Punch",
               damage=6,
               velocity=1,
               mana=0,
               stamina=10,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Hand",
               R_E = ["common",0])

Sword = Weapons(name="Sword",
               damage=25,
               velocity=2,
               mana=0,
               stamina=20,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["common",2])

Hammer = Weapons(name="Hammer",
               damage=30,
               velocity=4,
               mana=0,
               stamina=25,
               precision=0.6,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["common",2])

Staff = Weapons(name="Staff",
               damage=20,
               velocity=2.5,
               mana=15,
               stamina=0,
               precision=0.7,
               ammo=MagicBurst,
               element="light",
               grade=1,
               type="Magical",
               R_E = ["common",2])

Bow = Weapons(name="Wooden Bow",
               damage=15,
               velocity=3,
               mana=0,
               stamina=20,
               precision=0.6,
               ammo=IronArrow,
               element="none",
               grade="nb",
               type="Bow",
               R_E = ["common",2])

# SPECIAL WEAPON

Scratch = Weapons(name="Scratch",
               damage=10,
               velocity=1,
               mana=0,
               stamina=10,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Special",
               R_E = ["common",0])

Claws = Weapons(name="Claws",
               damage=16,
               velocity=1.2,
               mana=0,
               stamina=15,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Special",
               R_E = ["common",0])

Bite = Weapons(name="Bite",
               damage=15,
               velocity=1,
               mana=0,
               stamina=10,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Special",
               R_E = ["common",0])

headbutt = Weapons(name="Headbutt",
               damage=12,
               velocity=2,
               mana=0,
               stamina=15,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Special",
               R_E = ["common",0])

# WEAPON LOOTABLE

BaghNakh = Weapons(name="Bagh Nakh",
               damage=16,
               velocity=1.1,
               mana=0,
               stamina=15,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Hand",
               R_E = ["common",7])

BrassKnuckles = Weapons(name="Brass Knuckles",
               damage=13,
               velocity=1,
               mana=0,
               stamina=10,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Hand",
               R_E = ["common",5])

IronFist = Weapons(name="Iron Fist",
               damage=18,
               velocity=1.5,
               mana=0,
               stamina=20,
               precision=0.7,
               ammo="nb",
               element="none",
               grade="nb",
               type="Hand",
               R_E = ["common",7])

HandWraps = Weapons(name="Hand Wraps",
               damage=10,
               velocity=1,
               mana=0,
               stamina=15,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Hand",
               R_E = ["common",2])

MetalClaw = Weapons(name="Metal Claw",
               damage=10,
               velocity=1,
               mana=0,
               stamina=15,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Hand",
               R_E = ["common",5])

LeatherGlove = Weapons(name="Leather",
               damage=10,
               velocity=0.8,
               mana=0,
               stamina=5,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Hand",
               R_E = ["common",4])

BattleAxe = Weapons(name="Battle Axe",
               damage=30,
               velocity=3,
               mana=0,
               stamina=22,
               precision=0.7,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["uncommon",15])

Spear = Weapons(name="Spear",
               damage=22,
               velocity=2.2,
               mana=0,
               stamina=20,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["common",10])

Mace = Weapons(name="Mace",
               damage=30,
               velocity=2,
               mana=0,
               stamina=25,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["uncommon",15])

Sabre  = Weapons(name="Sabre",
               damage=25,
               velocity=1.4,
               mana=0,
               stamina=18,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["uncommon",15])

Dagger = Weapons(name="Dagger",
               damage=12,
               velocity=1,
               mana=0,
               stamina=14,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["common",5])

Katana = Weapons(name="Katana",
               damage=30,
               velocity=1.4,
               mana=0,
               stamina=18,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["uncommon",15])

Rapier = Weapons(name="Rapier",
               damage=25,
               velocity=1.8,
               mana=0,
               stamina=18,
               precision=0.9,
               ammo="nb",
               element="none",
               grade="nb",
               type="Light",
               R_E = ["uncommon",10])

DoubleBladedAxe  = Weapons(name="Double-Bladed Axe",
               damage=40,
               velocity=4,
               mana=0,
               stamina=35,
               precision=0.7,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["uncommon",18])

Flail = Weapons(name="Flail",
               damage=30,
               velocity=4,
               mana=0,
               stamina=25,
               precision=0.6,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["common",12])

Halberd = Weapons(name="Halberd",
               damage=34,
               velocity=3.4,
               mana=0,
               stamina=30,
               precision=0.6,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["common",12])

Club = Weapons(name="Club",
               damage=28,
               velocity=3.2,
               mana=0,
               stamina=20,
               precision=0.6,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["common",12])

Greatsword = Weapons(name="Greatsword",
               damage=30,
               velocity=3,
               mana=0,
               stamina=25,
               precision=0.7,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["common",15])

Scythe = Weapons(name="Scythe",
               damage=30,
               velocity=2.5,
               mana=0,
               stamina=20,
               precision=0.8,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["uncommon",18])

Warhammer = Weapons(name="War hammer",
               damage=40,
               velocity=4,
               mana=0,
               stamina=35,
               precision=0.6,
               ammo="nb",
               element="none",
               grade="nb",
               type="Heavy",
               R_E = ["uncommon",22])

HunterBow = Weapons(name="Hunter's Bow",
               damage=20,
               velocity=3,
               mana=0,
               stamina=20,
               precision=0.7,
               ammo=IronArrow,
               element="none",
               grade="nb",
               type="Bow",
               R_E = ["common",8])

GuardianBow = Weapons(name="Guardian's Bow",
               damage=25,
               velocity=4,
               mana=0,
               stamina=25,
               precision=0.6,
               ammo=IronArrow,
               element="none",
               grade="nb",
               type="Bow",
               R_E = ["rare",22])

ShadowBow = Weapons(name="Shadow Bow",
               damage=23,
               velocity=2,
               mana=0,
               stamina=20,
               precision=0.8,
               ammo=IronArrow,
               element="none",
               grade="nb",
               type="Bow",
               R_E = ["rare",25])

ArcaneBow = Weapons(name="Arcane Bow",
               damage=20,
               velocity=3,
               mana=20,
               stamina=0,
               precision=0.7,
               ammo=IronArrow,
               element="none",
               grade="nb",
               type="Bow",
               R_E = ["rare",25])

CrystalBow = Weapons(name="Crystal Bow",
               damage=28,
               velocity=3,
               mana=0,
               stamina=25,
               precision=0.7,
               ammo=IronArrow,
               element="none",
               grade="nb",
               type="Bow",
               R_E = ["epic",68])

#magia

BranchOfSparks = Weapons(name="Branch of Sparks",
               damage=2,
               velocity=1.8,
               mana=4,
               stamina=0,
               precision=0.7,
               ammo=MagicBurst,
               element="fire",
               grade=1,
               type="Magical",
               R_E = ["common",10])

StaffOfEmbers = Weapons(name="Staff Of Embers",
               damage=4,
               velocity=2,
               mana=6,
               stamina=0,
               precision=0.7,
               ammo=MagicBurst,
               element="fire",
               grade=2,
               type="Magical",
               R_E = ["uncommon",35])

ScepterOfFlames = Weapons(name="Scepter Of Flames",
               damage=6,
               velocity=2.5,
               mana=8,
               stamina=0,
               precision=0.7,
               ammo=MagicBurst,
               element="fire",
               grade=3,
               type="Magical",
               R_E = ["epic",115])

CatalystOfTheBlazingSun = Weapons(name="Catalyst Of The Blazing Sun",
               damage=8,
               velocity=3,
               mana=10,
               stamina=0,
               precision=0.8,
               ammo=MagicBurst,
               element="fire",
               grade=4,
               type="Magical",
               R_E = ["mythical",365])

BranchOfTheDrop = Weapons(
    name="Branch of the Drop",
    damage=2,
    velocity=1.5,
    mana=4,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="water",
    grade=1,
    type="Magical",
    R_E = ["common",10]
)

StaffOfTheRiver = Weapons(
    name="Staff of the River",
    damage=3,
    velocity=1.7,
    mana=6,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="water",
    grade=2,
    type="Magical",
    R_E = ["uncommon",35]
)

ScepterOfTheSea = Weapons(
    name="Scepter of the Sea",
    damage=4,
    velocity=2,
    mana=8,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="water",
    grade=3,
    type="Magical",
    R_E = ["epic",115]
)

CatalystOfTheOceans = Weapons(
    name="Catalyst of the Oceans",
    damage=6,
    velocity=2.5,
    mana=10,
    stamina=0,
    precision=0.8,
    ammo=MagicBurst,
    element="water",
    grade=4,
    type="Magical",
    R_E = ["mythical",365]
)

SproutedBranch = Weapons(
    name="Sprouted Branch",
    damage=2,
    velocity=1.8,
    mana=4,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="nature",
    grade=1,
    type="Magical",
    R_E = ["common",10]
)

GrowingStaff = Weapons(
    name="Growing Staff",
    damage=4,
    velocity=2,
    mana=6,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="nature",
    grade=2,
    type="Magical",
    R_E = ["uncommon",35]
)

ScepterOfTheForest = Weapons(
    name="Scepter of the Forest",
    damage=5,
    velocity=2.5,
    mana=8,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="nature",
    grade=3,
    type="Magical",
    R_E = ["epic",115]
)

CatalystOfEternalLife = Weapons(
    name="Catalyst of Eternal Life",
    damage=6,
    velocity=3,
    mana=10,
    stamina=0,
    precision=0.8,
    ammo=MagicBurst,
    element="nature",
    grade=4,
    type="Magical",
    R_E = ["mythical",365]
)

BranchOfElectro = Weapons(
    name="Branch of Electro",
    damage=2,
    velocity=1.2,
    mana=4,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="electro",
    grade=1,
    type="Magical",
    R_E = ["common",10]
)

StaffOfElectricity = Weapons(
    name="Staff of Electricity",
    damage=4,
    velocity=1.4,
    mana=6,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="electro",
    grade=2,
    type="Magical",
    R_E = ["uncommon",35]
)

ScepterOfLightning = Weapons(
    name="Scepter of Lightning",
    damage=6,
    velocity=1.8,
    mana=8,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="electro",
    grade=3,
    type="Magical",
    R_E = ["epic",115]
)

CatalystOfTheStorm = Weapons(
    name="Catalyst of the Storm",
    damage=8,
    velocity=2.2,
    mana=10,
    stamina=0,
    precision=0.8,
    ammo=MagicBurst,
    element="electro",
    grade=4,
    type="Magical",
    R_E = ["mythical",365]
)

BranchOfThePebble = Weapons(
    name="Branch of the Pebble",
    damage=2,
    velocity=1.8,
    mana=4,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="rock",
    grade=1,
    type="Magical",
    R_E = ["common",10]
)

StaffOfTheRock = Weapons(
    name="Staff of the Rock",
    damage=4,
    velocity=2.2,
    mana=6,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="rock",
    grade=2,
    type="Magical",
    R_E = ["uncommon",35]
)

ScepterOfTheMountain = Weapons(
    name="Scepter of the Mountain",
    damage=6,
    velocity=2.8,
    mana=8,
    stamina=0,
    precision=0.8,
    ammo=MagicBurst,
    element="rock",
    grade=3,
    type="Magical",
    R_E = ["epic",115]
)

CatalystOfPrimordialEarth = Weapons(
    name="Catalyst of Primordial Earth",
    damage=8,
    velocity=3.4,
    mana=10,
    stamina=0,
    precision=0.8,
    ammo=MagicBurst,
    element="rock",
    grade=4,
    type="Magical",
    R_E = ["mythical",365]
)

BranchOfTheCandle = Weapons(
    name="Branch of the Candle",
    damage=2,
    velocity=1.2,
    mana=3,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="light",
    grade=1,
    type="Magical",
    R_E = ["common",7]
)

StaffOfFaith = Weapons(
    name="Staff of Faith",
    damage=4,
    velocity=1.4,
    mana=5,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="light",
    grade=2,
    type="Magical",
    R_E = ["uncommon",28]
)

RadiantScepter = Weapons(
    name="Radiant Scepter",
    damage=6,
    velocity=1.8,
    mana=7,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="light",
    grade=3,
    type="Magical",
    R_E = ["epic",85]
)

DivineCatalyst = Weapons(
    name="Divine Catalyst",
    damage=8,
    velocity=2.2,
    mana=9,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="light",
    grade=4,
    type="Magical",
    R_E = ["mythical",285]
)

BranchOfShadows = Weapons(
    name="Branch of Shadows",
    damage=3,
    velocity=2,
    mana=6,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="darkness",
    grade=1,
    type="Magical",
    R_E = ["common",26]
)

StaffOfDarkness = Weapons(
    name="Staff of Darkness",
    damage=6,
    velocity=2.4,
    mana=9,
    stamina=0,
    precision=0.7,
    ammo=MagicBurst,
    element="darkness",
    grade=2,
    type="Magical",
    R_E = ["uncommon",68]
)

ScepterOfTheAbyss = Weapons(
    name="Scepter of the Abyss",
    damage=9,
    velocity=2.8,
    mana=12,
    stamina=0,
    precision=0.8,
    ammo=MagicBurst,
    element="darkness",
    grade=3,
    type="Magical",
    R_E = ["epic",202]
)

CatalystOfTheAbyss = Weapons(
    name="Catalyst of the Abyss",
    damage=12,
    velocity=3.5,
    mana=14,
    stamina=0,
    precision=0.8,
    ammo=MagicBurst,
    element="darkness",
    grade=4,
    type="Magical",
    R_E = ["mythical",525]
)

##############################################
# ADJUST FUNCTION

def Adjust_Weapon_Stats(Race, Weapon):
    match Race:
        # Razze piccole
        case "Goblin" | "Gobliniano" | "Gobliniana" | "Gnomo" | "Gnoma" | "Gnome" | "Kobold" | "Svirfneblin" | "Hobbit" | "Mezzuomo":
            match Weapon.type:
                case "Hand":
                    Weapon.damage -= 4
                    Weapon.velocity -= 0.5
                case "Light":
                    Weapon.damage -= 6
                    Weapon.velocity -= 0.5
                    Weapon.precision -= 0.1
                case "Heavy":
                    Weapon.damage -= 12
                    Weapon.velocity += 1
                    Weapon.precision -= 0.2
                case "Bow":
                    Weapon.precision -= 0.1
                case "Special":
                    Weapon.damage += 5

        # Tabaxi e Khajit
        case "Tabaxi" | "Khajit":
            match Weapon.type:
                case "Hand" | "Light" | "Bow":
                    Weapon.velocity -= 0.5
                    Weapon.damage += 3
                    Weapon.precision += 0.1
                case "Heavy":
                    Weapon.damage -= 5
                case "Special":
                    Weapon.damage += 5
                    Weapon.precision += 0.1

        # Bosmer e simili
        case "Bosmer" | "Wood-Elf" | "Wood-Elves" | "Wood Elf" | "Wood Elves":
            match Weapon.type:
                case "Magical":
                    Weapon.damage += 5
                    Weapon.velocity -= 0.5
                case "Bow":
                    Weapon.damage += 10
                    Weapon.velocity -= 0.5
                case "Heavy":
                    Weapon.damage -= 6
                    Weapon.precision -= 0.1
                    Weapon.velocity -= 0.2

        # Kenku e Aarakocra
        case "Kenku" | "Aarakocra":
            match Weapon.type:
                case "Hand":
                    Weapon.damage -= 5
                    Weapon.velocity -= 0.5
                case "Light":
                    Weapon.damage -= 10
                    Weapon.velocity -= 0.5
                case "Bow":
                    Weapon.damage += 6
                    Weapon.velocity -= 1
                case "Heavy":
                    Weapon.damage -= 18
                    Weapon.velocity += 0.5

        # Mezzelfi
        case "Half-Elf" | "Half Elf" | "Half Elves" | "Half-Elves" | "Mezzelfo" | "Mezzelfi" | "Mezzelfa":
            match Weapon.type:
                case "Bow":
                    Weapon.velocity -= 0.5
                case "Magical":
                    Weapon.damage += 5
                    Weapon.velocity -= 0.5
                case "Hand":
                    Weapon.damage -= 5
                case "Heavy":
                    Weapon.damage -= 5

        # Non Morti
        case "Undead" | "Non Morto":
            match Weapon.type:
                case "Magical":
                    Weapon.damage += 5
                    Weapon.velocity += 0.5
                case "Hand":
                    Weapon.damage += 2
                    Weapon.velocity -= 0.5
                case "Special":
                    Weapon.damage += 8
                    Weapon.velocity -= 0.5
                    Weapon.precision += 0.1

        # Wraith e Streghe
        case "Wraith" | "Strega":
            match Weapon.type:
                case "Magical":
                    Weapon.damage += 10
                    Weapon.velocity -= 0.5
                case "Hand":
                    Weapon.velocity += 1
                case "Light":
                    Weapon.damage -= 5
                    Weapon.velocity += 1
                case "Heavy":
                    Weapon.damage -= 10
                    Weapon.velocity += 2
                case "Bow":
                    Weapon.damage -= 10
                    Weapon.velocity += 1
                case "Special":
                    Weapon.damage += 5
                    Weapon.velocity += 1

        # Elfi e Druidi
        case "Elves" | "Avari" | "Altmer" | "Dunmer" | "Elf" | "Elfo" | "Elfa" | "Elfian" | "Druid":
            match Weapon.type:
                case "Bow":
                    Weapon.damage += 5
                    Weapon.velocity -= 0.5
                case "Magical":
                    Weapon.damage += 10
                    Weapon.velocity -= 0.5
                case "Light":
                    Weapon.damage -= 4
                case "Hand":
                    Weapon.damage -= 10
                case "Heavy":
                    Weapon.damage -= 10
                    Weapon.precision -= 0.1
                    Weapon.velocity += 0.5

        # Vampiri
        case "Vampire" | "Vampiro" | "Vampira" | "Vampiric":
            match Weapon.type:
                case "Magical":
                    Weapon.damage += 10
                    Weapon.velocity -= 0.5
                case "Hand" | "Light":
                    Weapon.velocity -= 0.5
                case "Special":
                    Weapon.velocity -= 0.5
                    Weapon.damage += 18

        # Lupi Mannari
        case "Werewolf" | "Lupo Mannaro" | "Lupus" | "Wulf":
            match Weapon.type:
                case "Hand":
                    Weapon.damage += 10
                    Weapon.velocity -= 0.5
                case "Magical":
                    Weapon.damage -= 10
                    Weapon.velocity += 0.5
                case "Special":
                    Weapon.damage += 15
                case "Heavy":
                    Weapon.damage += 3
                    Weapon.velocity -= 0.5
                    Weapon.precision += 0.1

        # Mezzorchi
        case "Halfling" | "Mezzorco" | "Mezzorca":
            match Weapon.type:
                case "Hand":
                    Weapon.damage += 5
                case "Magical":
                    Weapon.velocity += 0.5
                case "Heavy":
                    Weapon.damage += 2

        # Orchi
        case "Orc" | "Orco" | "Orca" | "Ork" | "Orsimer":
            match Weapon.type:
                case "Light":
                    Weapon.damage += 5
                    Weapon.velocity += 0.5
                case "Hand":
                    Weapon.damage += 10
                    Weapon.velocity += 0.5
                case "Magical":
                    Weapon.damage -= 5
                    Weapon.velocity += 1
                case "Heavy":
                    Weapon.damage += 5
                    Weapon.velocity -= 0.5
                    Weapon.precision += 0.1

        # Dragonborn
        case "Dragonborn" | "Dragonide" | "Dragonidi":
            match Weapon.type:
                case "Light":
                    Weapon.damage += 5
                    Weapon.velocity += 0.5
                case "Hand":
                    Weapon.damage += 6
                    Weapon.velocity += 0.5
                case "Heavy":
                    Weapon.damage += 4
                    Weapon.velocity -= 0.5
                    Weapon.precision += 0.1

        # Nani
        case "Dwarf" | "Nano" | "Nani" | "Dwarven":
            match Weapon.type:
                case "Light":
                    Weapon.damage += 5
                case "Magical":
                    Weapon.damage -= 10
                    Weapon.velocity += 0.5
                case "Heavy":
                    Weapon.damage += 5
                    Weapon.velocity -= 1
                    Weapon.precision += 0.2

        # Troll e Giganti
        case "Troll" | "Trolliano" | "Giant" | "Giganti" | "Gigante":
            match Weapon.type:
                case "Hand":
                    Weapon.damage += 30
                    Weapon.velocity += 2
                case "Magical":
                    Weapon.damage -= 40
                case "Bow":
                    Weapon.damage -= 40
                case "Light":
                    Weapon.damage -= 20
                    Weapon.velocity += 1
                case "Heavy":
                    Weapon.damage -= 10
                    Weapon.velocity += 0.5
                    Weapon.precision -= 0.1

        # Demoni
        case "Demon" | "Demoniac" | "Demone" | "Demoniaca" | "Aasimar" | "Succubs":
            match Weapon.type:
                case "Magical":
                    Weapon.damage += 10
                    Weapon.velocity -= 0.5
                case "Light":
                    Weapon.damage += 5
                case "Heavy":
                    Weapon.velocity -= 0.5

        # Tiefling
        case "Tiefling" | "Tieflings" | "Mezzo Demone":
            match Weapon.type:
                case "Magical":
                    Weapon.damage += 5
                case "Light":
                    Weapon.velocity -= 0.5
        
        case "Fairy" | "Fairies" | "Fate" | "Fata":
            match Weapon.type:
                case "Magical":
                    Weapon.damage += 5
                    Weapon.velocity -= 0.5
                case "Heavy":
                    Weapon.damage -= 25
                case "Light":
                    Weapon.damage -= 10
                case "Bow":
                    Weapon.damage -= 5
        
        case "Animal":
            match Weapon.type:
                case "Special":
                    Weapon.damage += random.randint(5,12)
                    Weapon.velocity -= 0.5
        
        case "Alpha Animal":
            match Weapon.type:
                case "Special":
                    Weapon.damage += random.randint(8,18)
                    Weapon.velocity -= 0.5
        
        case "Passive Animal":
            match Weapon.type:
                case "Special":
                    Weapon.damage -= 11

    if Weapon.damage < 0:
        Weapon.damage = 0


##############################################
# CHARACTER

class Character:
    def __init__(self,Name,Race,Gender,Age,Weapon,Armor):
        self.Name = Name
        self.Race = Race
        self.Gender = Gender
        self.Age = Age
        self.Weapon = Weapon.copy()
        self.Armor = Armor.copy()
        self.Ability = "None"
        self.TAG_Effect = copy.deepcopy([Vampirism,Healing1,Strong_Healing,Shield,Strong_Shield,Burn,Strength,Potent_Strength,Resistance,Poison,Potent_Poison,Frost,Wood,Regen,Anti_Arrow,Weakness,Magical,Lowering_Speed])
        self.Stamina = [50,50]
        self.Mana = [50,50]
        self.HP = [100,100]
        self.Active_Element = {"fire":0,
                               "rock":0,
                               "water":0,
                               "nature":0,
                               "light":0,
                               "darkness":0,
                               "electro":0}
        self.Statistics()
        Adjust_Weapon_Stats(self.Race,self.Weapon)

    def Statistics(self):
        match self.Race:
            case "Goblin" | "Gobliniano" | "Gobliniana" | "Gnomo" | "Gnoma" | "Gnome" | "Kobold" | "Svirfneblin" | "Hobbit" | "Mezzuomo":
                self.Stamina = [50, 50]
                self.Mana = [50, 50]
                self.HP = [60, 60]
                self.Ability = "Rapid"

            case "Fairy" | "Fairies" | "Fate" | "Fata":
                self.Stamina = [25, 25]
                self.Mana = [100, 100]
                self.HP = [50, 50]
                self.Ability = "Magic"

            case "Elves" | "Avari" | "Altmer" | "Dunmer" | "Elf" | "Elfo" | "Elfa" | "Elfian" | "Druid":
                self.Stamina = [25, 25]
                self.Mana = [100, 100]
                self.HP = [80, 80]
                self.Ability = "Magic"

            case "Bosmer" | "Wood-Elf" | "Wood-Elves" | "Wood Elf" | "Wood Elves":
                self.Stamina = [75, 75]
                self.Mana = [50, 50]
                self.HP = [80, 80]
                self.Ability = "Archer"

            case "Human" | "Umano" | "Umani" | "Umana":
                self.Stamina = [50, 50]
                self.Mana = [50, 50]
                self.HP = [100, 100]
                self.Ability = "None"

            case "Vampire" | "Vampiro" | "Vampira" | "Vampiric":
                self.Stamina = [25, 25]
                self.Mana = [75, 75]
                self.HP = [110, 110]
                self.Ability = "Magic"

            case "Werewolf" | "Lupo Mannaro" | "Lupus" | "Wulf" | "Halfling" | "Mezzorco" | "Mezzorca":
                self.Stamina = [75, 75]
                self.Mana = [25, 25]
                self.HP = [110, 110]
                self.Ability = "Brute"

            case "Orc" | "Orco" | "Orca" | "Ork" | "Dragonborn" | "Dragonide" | "Dragonidi" | "Orsimer":
                self.Stamina = [75, 75]
                self.Mana = [25, 25]
                self.HP = [130, 130]
                self.Ability = "Shield"

            case "Centaur" | "Centaurs" | "Centauri" | "Centauro":
                self.Stamina = [75, 75]
                self.Mana = [25, 25]
                self.HP = [130, 130]
                self.Ability = "Archer"

            case "Dwarf" | "Nano" | "Nani" | "Dwarven":
                self.Stamina = [75, 75]
                self.Mana = [25, 25]
                self.HP = [130, 130]
                self.Ability = "Shield"

            case "Troll" | "Trolliano" | "Giant" | "Giganti" | "Gigante":
                self.Stamina = [100, 100]
                self.Mana = [25, 25]
                self.HP = [160, 160]
                self.Ability = "Brute"

            case "Demon" | "Demoniac" | "Demone" | "Demoniaca" | "Aasimar" | "Succubs":
                self.Stamina = [75, 75]
                self.Mana = [100, 100]
                self.HP = [120, 120]
                self.Ability = "Magic"

            case "Tiefling" | "Tieflings" | "Mezzo Demone":
                self.Stamina = [75, 75]
                self.Mana = [75, 75]
                self.HP = [110, 110]
                self.Ability = "None"

            case "Kenku" | "Aarakocra":
                self.Stamina = [50, 50]
                self.Mana = [25, 25]
                self.HP = [60, 60]
                self.Ability = "Archer"

            case "Tabaxi" | "Khajit":
                self.Stamina = [50, 50]
                self.Mana = [50, 50]
                self.HP = [110, 110]
                self.Ability = "None"

            case "Half-Elf" | "Half Elf" | "Half Elves" | "Half-Elves" | "Mezzelfo" | "Mezzelfi" | "Mezzelfa":
                self.Stamina = [50, 50]
                self.Mana = [75, 75]
                self.HP = [90, 90]
                self.Ability = "None"

          
##############################################
# ENEMY
  
class Enemy:
    def __init__(self,Name,Race,Gender,Age,Weapon,Armor,Stamina,Mana,HP,Ability):
        self.Name = Name
        self.Race = Race
        self.Gender = Gender
        self.Age = Age
        self.Weapon = Weapon.copy()
        self.Armor = Armor.copy()
        self.Stamina = Stamina
        self.Mana = Mana
        self.HP = HP
        self.Ability = Ability
        self.Active_Element = {"fire":0,
                        "rock":0,
                        "water":0,
                        "nature":0,
                        "light":0,
                        "darkness":0,
                        "electro":0}
        self.TAG_Effect = copy.deepcopy([Vampirism,Healing1,Wood,Strong_Healing,Shield,Strong_Shield,Burn,Strength,Potent_Strength,Resistance,Poison,Potent_Poison,Frost,Regen,Anti_Arrow,Weakness,Magical,Lowering_Speed])
        Adjust_Weapon_Stats(self.Race,self.Weapon)

    def Attribute_Return(self):
        return [self.Name,self.Weapon,self.Armor,self.Race]
    
    def __str__(self):
        return f"{self.Name} | Race: {self.Race} | Gender: {self.Gender} | Mana: {self.Mana} | Stamina: {self.Stamina} | Age: {self.Age} | HP: {self.HP} | Weapon: {self.Weapon}"

def Adjust_CreateEnemy_Ammo(Enemies):
    if Enemies.Weapon.type == "Magical" and Enemies.Weapon.name != "Arcane Bow":
        Spell_TempList = []
        for spell in All_Spells:
            if Enemies.Weapon.element != spell.elemental or Enemies.Weapon.grade < spell.grade:
                pass
            else:
                Spell_TempList.append(spell)
                continue
        Enemies.Weapon.ammo = random.choice(Spell_TempList)

    elif Enemies.Weapon.type == "Bow" or Enemies.Weapon.name == "Arcane Bow":
        match Enemies.Race:
            case "Elves" | "Avari" | "Altmer" | "Dunmer" | "Elf" | "Elfo" | "Elfa" | "Elfian" | "Elves" | "Avari" | "Altmer" | "Dunmer" | "Elf" | "Elfo" | "Elfa" | "Elfian":
                Enemies.Weapon.ammo = ElfArrow
            case "Orc" | "Orco" | "Orca" | "Ork":
                Enemies.Weapon.ammo = BoneArrow
            case "Human" | "Umano" | "Umani" | "Umana":
                Enemies.Weapon.ammo = random.choice([IronArrow,SteelArrow,BoneArrow])
            case "Centaur" | "Centaurs" | "Centauri" | "Centauro":
                Enemies.Weapon.ammo = random.choice([GlassArrow,SteelArrow])
            case _:
                Enemies.Weapon.ammo = random.choice([IronArrow,SteelArrow])

    return Enemies

def CreateEnemy(Name):
    if Name == "GoblinWarrior":
        GoblinWarriorRandomWeapon =random.choices([[Punch, HandWraps, LeatherGlove, MetalClaw], [IronFist, BaghNakh, BrassKnuckles, Spear, Sword]], weights=[0.8, 0.2], k=1)[0]
        return Enemy(
                    Name="Goblin Warrior",
                    Race="Goblin",
                    Gender=random.choice(["FM", "MM"]),
                    Age=str(random.randint(8, 25)),
                    Weapon = random.choice(GoblinWarriorRandomWeapon),
                    Armor = random.choices([Goblin_Mail,Wooden_Armor], weights=[0.7, 0.3], k=1)[0],
                    Ability="Rapid",
                    Stamina=[50,50],
                    Mana=[50,50],
                    HP=[60,60]
                )
    
    elif Name == "GoblinArcher":
        return Enemy(
            Name="Goblin Archer",
            Race="Goblin",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(8, 25)),
            Weapon=random.choices([Bow, HunterBow], weights=[0.8, 0.2], k=1)[0],
            Armor=random.choices([Archers_Robes,Goblin_Mail], weights=[0.7, 0.3], k=1)[0],
            Ability="Archer",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[60,60]
        )

    elif Name == "GoblinShaman":
        return Enemy(
            Name="Goblin Shaman",
            Race="Goblin",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(8, 25)),
            Weapon=random.choices([SproutedBranch,GrowingStaff], weights=[0.7,0.3],k=1)[0],
            Armor=random.choices([Novice_Mages_Garments,Goblin_Mail], weights=[0.6, 0.4], k=1)[0],
            Ability="Magic",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[60,60]
        )

    elif Name == "GoblinKing":
        return Enemy(
            Name="Goblin King",
            Race="Goblin",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(15, 40)),
            Weapon=random.choice([Warhammer, Hammer, StaffOfEmbers, Halberd, Flail, DoubleBladedAxe]),
            Armor=random.choices([Bone_Armor,Heavy_War_Armor], weights=[0.7, 0.3], k=1)[0],
            Ability="Brute",
            Stamina=[75, 75],
            Mana=[50, 50],
            HP=[100,100]
        )

    elif Name == "KoboldWarrior":
        KoboldWarriorRandomWeapon = random.choices([[Punch, HandWraps, LeatherGlove, MetalClaw], [IronFist, BaghNakh, BrassKnuckles, Spear, Sword]], weights=[0.8, 0.2], k=1)[0]
        return Enemy(
            Name="Kobold Warrior",
            Race="Kobold",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(8, 25)),
            Weapon=random.choice(KoboldWarriorRandomWeapon),
            Armor = random.choices([Goblin_Mail,Wooden_Armor], weights=[0.7, 0.3], k=1)[0],
            Ability="Rapid",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[60,60]
        )

    elif Name == "SvirfneblinWarrior":
        SvirfneblinWarriorRandomWeapon = random.choices([[Punch, HandWraps, LeatherGlove, MetalClaw], [IronFist, BaghNakh, BrassKnuckles, Spear, Sword]], weights=[0.8, 0.2], k=1)[0]
        return Enemy(
            Name="Svirfneblin Warrior",
            Race="Svirfneblin",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(8, 25)),
            Weapon=random.choice(SvirfneblinWarriorRandomWeapon),
            Armor = random.choices([Goblin_Mail,Wooden_Armor], weights=[0.7, 0.3], k=1)[0],
            Ability="Rapid",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[60,60]
        )

    elif Name == "GnomeThief":
        return Enemy(
            Name="Gnome Thief",
            Race="Gnome",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(20, 80)),
            Weapon=random.choice([Dagger, BrassKnuckles, BaghNakh]),
            Armor = Cloth_Garments,
            Ability="Rapid",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[60,60]
        )

    elif Name == "OrcBerserker":
        return Enemy(
            Name="Orc Berserker",
            Race="Orc",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(15, 50)),
            Weapon=random.choice([BattleAxe, Sword, IronFist, Mace]),
            Armor=Orcish_Armor,
            Ability="None",
            Stamina=[75, 75],
            Mana=[25, 25],
            HP=[130,130]
        )

    elif Name == "OrcHunter":
        return Enemy(
            Name="Orc Hunter",
            Race="Orc",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(15, 65)),
            Weapon=random.choices([Bow, HunterBow], weights=[0.8, 0.2], k=1)[0],
            Armor=Orcish_Armor,
            Ability="Archer",
            Stamina=[75, 75],
            Mana=[25, 25],
            HP=[130,130]
        )

    elif Name == "OrcWarlord":
        return Enemy(
            Name="Orc Warlord",
            Race="Orc",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(50, 75)),
            Weapon=random.choice([Warhammer, Hammer, Halberd, Flail, DoubleBladedAxe]),
            Armor = random.choices([Heavy_War_Armor,Orcish_Armor], weights=[0.7, 0.3], k=1)[0],
            Ability="Brute",
            Stamina=[90, 90],
            Mana=[50, 50],
            HP=[140,140]
        )

    elif Name == "ElfMage":
        ElfMageRandomWeapon = random.choices([[StaffOfTheRiver,GrowingStaff,StaffOfElectricity,StaffOfTheRock], [ScepterOfTheSea,ScepterOfTheForest,ScepterOfLightning]], weights=[0.7, 0.3], k=1)[0]
        return Enemy(
            Name="Elf Mage",
            Race="Elf",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(700, 3500)),
            Weapon=random.choice(ElfMageRandomWeapon),
            Armor = random.choices([Elven_Armor,Mages_Robes], weights=[0.6, 0.4], k=1)[0],
            Ability="Magic",
            Stamina=[25, 25],
            Mana=[100, 100],
            HP=[80,80]
        )

    elif Name == "ElfArcher":
        return Enemy(
            Name="Elf Archer",
            Race="Bosmer",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(500, 3500)),
            Weapon=random.choices([Bow, HunterBow], weights=[0.8, 0.2], k=1)[0],
            Armor = Elven_Armor,
            Ability="Archer",
            Stamina=[50, 50],
            Mana=[75, 75],
            HP=[80,80]
        )

    elif Name == "ElfGuardian":
        ElfGuardianRandomWeapon = random.choices([[GuardianBow], [ScepterOfTheSea,ScepterOfTheForest,ScepterOfLightning]], weights=[0.5, 0.5], k=1)[0]
        return Enemy(
            Name="Elf Guardian",
            Race="Elf",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(3500, 6500)),
            Weapon=random.choice(ElfGuardianRandomWeapon),
            Armor = random.choices([Heavy_Elven_Armor,Masters_Robes], weights=[0.6, 0.4], k=1)[0],
            Ability="Shield",
            Stamina=[50, 50],
            Mana=[100, 100],
            HP=[100,100]
        )

    elif Name == "Troll":
        return Enemy(
            Name="Troll",
            Race="Troll",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(40, 400)),
            Weapon=random.choice([Punch, Club]),
            Armor=Bone_Armor,
            Ability="Brute",
            Stamina=[100, 100],
            Mana=[25, 25],
            HP=[160,160]
        )

    elif Name == "TrollBrute":
        return Enemy(
            Name="Troll Brute",
            Race="Troll",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(180, 440)),
            Weapon=random.choice([Punch, Club]),
            Armor=Bone_Armor,
            Ability="Brute",
            Stamina=[100, 100],
            Mana=[25, 25],
            HP=[200,200]
        )

    elif Name == "VampireAssassin":
        VampireAssassinRandomWeapon = random.choices([[Sword, Rapier, Spear, MetalClaw, Dagger], [StaffOfElectricity,StaffOfDarkness,StaffOfTheRock,ScepterOfLightning,StaffOfEmbers]], weights=[0.7, 0.3], k=1)[0]
        return Enemy(
            Name="Vampire Assassin",
            Race="Vampire",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(18, 160)),
            Weapon=random.choice(VampireAssassinRandomWeapon),
            Armor=Vampiric_Armor,
            Ability="Magic",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[110,110]
        )

    elif Name == "VampireSorcerer":
        return Enemy(
            Name="Vampire Sorcerer",
            Race="Vampire",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(25, 170)),
            Weapon=random.choice([StaffOfElectricity,StaffOfDarkness,StaffOfTheRock,ScepterOfLightning,StaffOfEmbers]),
            Armor=Vampiric_Armor,
            Ability="Magic",
            Stamina=[25, 25],
            Mana=[75, 75],
            HP=[110,110]
        )

    elif Name == "VampireLord":
        VampireLordRandomWeapon = random.choices([[Halberd, Greatsword, Scythe], [StaffOfDarkness,ScepterOfLightning,ScepterOfTheAbyss,ScepterOfFlames]], weights=[0.7, 0.3], k=1)[0]
        return Enemy(
            Name="Vampire Lord",
            Race="Vampire",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(150, 220)),
            Weapon=random.choice(VampireLordRandomWeapon),
            Armor = random.choices([Vampiric_Armor,Necromancers_Robes], weights=[0.7, 0.3], k=1)[0],
            Ability=random.choice(["Brute", "Magic"]),
            Stamina=[75, 75],
            Mana=[100, 100],
            HP=[130,130]
        )

    elif Name == "Werewolf":
        return Enemy(
            Name="Werewolf",
            Race="Werewolf",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(16, 75)),
            Weapon=random.choice([HandWraps, MetalClaw, Punch]),
            Armor=Leather_Armor,
            Ability=random.choice(["Brute", "None"]),
            Stamina=[75, 75],
            Mana=[25, 25],
            HP=[110,110]
        )

    elif Name == "DwarvenWarrior":
        DwarvenWarriorRandomWeapon = random.choices([[Hammer, Sword, BattleAxe], [IronFist, DoubleBladedAxe]], weights=[0.7, 0.3], k=1)[0]
        return Enemy(
            Name="Dwarven Warrior",
            Race="Dwarf",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(45, 320)),
            Weapon=random.choice(DwarvenWarriorRandomWeapon),
            Armor=Dwarven_Armor,
            Ability="Shield",
            Stamina=[75, 75],
            Mana=[25, 25],
            HP=[130,130]
        )

    elif Name == "DwarvenHunter":
        return Enemy(
            Name="Dwarven Hunter",
            Race="Dwarf",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(45, 320)),
            Weapon=random.choice([Bow, HunterBow]),
            Armor=Dwarven_Armor,
            Ability="Archer",
            Stamina=[75, 75],
            Mana=[25, 25],
            HP=[130,130]
        )

    elif Name == "Bandit":
        return Enemy(
            Name="Bandit",
            Race="Human",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(18, 65)),
            Weapon=random.choice([Dagger, Sword, BrassKnuckles, Sabre]),
            Armor = random.choice([Bandit_Armor, Leather_Armor, Iron_Chainmail, Wooden_Armor]),
            Ability="None",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[100,100]
        )

    elif Name == "Hunter":
        return Enemy(
            Name="Hunter",
            Race="Human",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(18, 65)),
            Weapon=random.choices([Bow, HunterBow], weights=[0.8, 0.2], k=1)[0],
            Armor = random.choice([Bandit_Armor, Leather_Armor, Archers_Robes]),
            Ability="Archer",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[100,100]
        )

    elif Name == "BanditMage":
        return Enemy(
            Name="Bandit Mage",
            Race="Human",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(24, 75)),
            Weapon=random.choice([BranchOfSparks,BranchOfTheDrop,SproutedBranch,BranchOfElectro,BranchOfThePebble,BranchOfShadows]),
            Armor = random.choice([Novice_Mages_Garments, Bandit_Armor, Mages_Robes, Leather_Armor]),
            Ability="Magic",
            Stamina=[50, 50],
            Mana=[60, 60],
            HP=[100,100]
        )

    elif Name == "Wraith":
        return Enemy(
            Name="Wraith",
            Race="Wraith",
            Gender="FM",
            Age=str(random.randint(100, 500)),
            Weapon=random.choice([BranchOfSparks,BranchOfShadows,BranchOfElectro,StaffOfEmbers]),
            Armor=Cloth_Garments,
            Ability="Magic",
            Stamina=[50, 50],
            Mana=[100, 100],
            HP=[80,80]
        )

    elif Name == "TabaxiWarrior":
        return Enemy(
            Name="Tabaxi Warrior",
            Race="Tabaxi",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(20, 100)),
            Weapon=random.choice([Rapier, Sabre, MetalClaw, Katana]),
            Armor = random.choice([Thiefs_Robes, Warriors_Armor, Iron_Chainmail, Leather_Armor]),
            Ability="None",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[110,110]
        )

    elif Name == "Demon":
        DemonRandomWeapon = random.choices([[Sword, Spear, Halberd], [BranchOfShadows,StaffOfEmbers,StaffOfElectricity,StaffOfDarkness]], weights=[0.5, 0.5], k=1)[0]
        return Enemy(
            Name="Demon",
            Race="Demon",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(100, 500)),
            Weapon=random.choice(DemonRandomWeapon),
            Armor=Demonic_Armor,
            Ability="Magic",
            Stamina=[75, 75],
            Mana=[100, 100],
            HP=[120,120]
        )

    elif Name == "DemonLord":
        DemonLordRandomWeapon = random.choices([[Warhammer, Hammer, Halberd, Flail, DoubleBladedAxe, Sword], [StaffOfDarkness,ScepterOfTheAbyss,ScepterOfLightning,ScepterOfFlames]], weights=[0.5, 0.5], k=1)[0]
        return Enemy(
            Name="Demon Lord",
            Race="Demon",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(340, 620)),
            Weapon=random.choice(DemonLordRandomWeapon),
            Armor = random.choices([Ebony_Armor,Golden_Armor], weights=[0.7, 0.3], k=1)[0],
            Ability=random.choice(["Magic", "Brute"]),
            Stamina=[100, 100],
            Mana=[100, 100],
            HP=[130,130]
        )

    elif Name == "DemonSpawn":
        return Enemy(
            Name="Demon Spawn",
            Race="Demon",
            Gender="UK",
            Age=str(random.randint(1, 100)),
            Weapon=MetalClaw,
            Armor=No_Armor,
            Ability="None",
            Stamina=[50, 50],
            Mana=[50, 50],
            HP=[60,60]
        )

    elif Name == "Tiefling":
        TieflingRandomWeapon = random.choices([[Sword, Spear, Rapier], [BranchOfShadows,StaffOfEmbers,StaffOfElectricity,BranchOfElectro,BranchOfSparks]], weights=[0.5, 0.5], k=1)[0]
        return Enemy(
            Name="Tiefling",
            Race="Tiefling",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(20, 150)),
            Weapon=random.choice(TieflingRandomWeapon),
            Armor = random.choice([Mages_Robes, Iron_Chainmail, Necromancers_Robes, Studded_Armor]),
            Ability="None",
            Stamina=[75, 75],
            Mana=[75, 75],
            HP=[110,110]
        )

    elif Name == "InfernalTiefling":
        InfernalTieflingRandomWeapon = random.choices([[Greatsword, BattleAxe], [BranchOfShadows,StaffOfEmbers,StaffOfElectricity,StaffOfDarkness]], weights=[0.5, 0.5], k=1)[0]
        return Enemy(
            Name="Infernal Tiefling",
            Race="Tiefling",
            Gender="UK",
            Age=str(random.randint(110, 180)),
            Weapon=random.choice(InfernalTieflingRandomWeapon),
            Armor=random.choice([Demonic_Armor,Necromancers_Robes,Knights_Armor,Heavy_War_Armor]),
            Ability="Magic",
            Stamina=[75, 75],
            Mana=[75, 75],
            HP=[130,130]
        )

    elif Name == "UndeadKnight":
        UndeadKnightRandomWeapon = random.choices([[Punch, HandWraps, LeatherGlove], [IronFist, BaghNakh, BrassKnuckles, Spear, Rapier]], weights=[0.8, 0.2], k=1)[0]
        return Enemy(
            Name="Undead Knight",
            Race="Undead",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(300, 1000)),
            Weapon=random.choice(UndeadKnightRandomWeapon),
            Armor=Knights_Armor,
            Ability="None",
            Stamina=[75, 75],
            Mana=[0, 0],
            HP=[100,100]
        )

    elif Name == "Skeleton":
        return Enemy(
            Name="Skeleton",
            Race="Undead",
            Gender="NB",
            Age=str(random.randint(500, 5000)),
            Weapon=random.choice([Bow, Sword]),
            Armor=random.choice([Leather_Armor,No_Armor,Iron_Chainmail]),
            Ability="None",
            Stamina=[50, 50],
            Mana=[0, 0],
            HP=[30,30]
        )

    elif Name == "Spectre":
        return Enemy(
            Name="Spectre",
            Race="Undead",
            Gender="NB",
            Age=str(random.randint(8, 5000)),
            Weapon=random.choice([BranchOfShadows, BranchOfElectro, Sword]),
            Armor=No_Armor,
            Ability="Magic",
            Stamina=[50, 50],
            Mana=[75, 75],
            HP=[75,75]
        )

    elif Name == "Zombie":
        return Enemy(
            Name="Zombie",
            Race="Undead",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(8, 5000)),
            Weapon=random.choice([Punch, MetalClaw, HandWraps]),
            Armor=random.choice([Cloth_Garments,Leather_Armor,Leather_Garments]),
            Ability="Magic",
            Stamina=[50, 50],
            Mana=[75, 75],
            HP=[75,75]
        )
    
    elif Name == "GrayWolf":
        return Enemy(
            Name="Gray Wolf",
            Race="Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(3, 18)),
            Weapon=random.choice(Special_Weapons),
            Armor=No_Armor,
            Ability="None",
            Stamina=[50, 50],
            Mana=[0, 0],
            HP=[50,50]
        )
    
    elif Name == "SnowWolf":
        return Enemy(
            Name="Snow Wolf",
            Race="Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(3, 18)),
            Weapon=random.choice(Special_Weapons),
            Armor=No_Armor,
            Ability="None",
            Stamina=[75, 75],
            Mana=[0, 0],
            HP=[65,65]
        )
    
    elif Name == "AlphaWolf":
        return Enemy(
            Name="Alpha Wolf",
            Race="Alpha Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(6, 24)),
            Weapon=random.choice(Special_Weapons),
            Armor=No_Armor,
            Ability="Brute",
            Stamina=[75, 75],
            Mana=[0, 0],
            HP=[100,100]
        )
    
    elif Name == "MountainLion":
        return Enemy(
            Name="Mountain Lion",
            Race="Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(4, 18)),
            Weapon=random.choice(Special_Weapons),
            Armor=No_Armor,
            Ability="None",
            Stamina=[60, 60],
            Mana=[0, 0],
            HP=[70, 70]
        )
    
    elif Name == "VenomousSnake":
        return Enemy(
            Name="Venomous Snake",
            Race="Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(3, 12)),
            Weapon=Bite,
            Armor=No_Armor,
            Ability="None",
            Stamina=[30, 30],
            Mana=[0, 0],
            HP=[20, 20]
        )
    
    elif Name == "SavageBoar":
        return Enemy(
            Name="Savage Boar",
            Race="Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(5, 15)),
            Weapon=random.choice([headbutt,Bite]),
            Armor=No_Armor,
            Ability="None",
            Stamina=[70, 70],
            Mana=[0, 0],
            HP=[80, 80]
        )
    
    elif Name == "BrownBear":
        return Enemy(
            Name="Brown Bear",
            Race="Alpha Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(5, 20)),
            Weapon=random.choice(Special_Weapons),
            Armor=No_Armor,
            Ability="None",
            Stamina=[70, 70],
            Mana=[0, 0],
            HP=[80, 80]
        )

    elif Name == "Deer":
        return Enemy(
            Name="Deer",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(3, 12)),
            Weapon=headbutt,
            Armor=No_Armor,
            Ability="None",
            Stamina=[30, 30],
            Mana=[0, 0],
            HP=[20, 20]
        )
    
    elif Name == "Rabbit":
        return Enemy(
            Name="Rabbit",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(1, 5)),
            Weapon=Bite,
            Armor=No_Armor,
            Ability="None",
            Stamina=[20, 20],
            Mana=[0, 0],
            HP=[10, 10]
        )
    
    elif Name == "Squirrel":
        return Enemy(
            Name="Squirrel",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(1, 7)),
            Weapon=Bite,
            Ability="None",
            Stamina=[15, 15],
            Mana=[0, 0],
            HP=[8, 8]
        )

    elif Name == "Beaver":
        return Enemy(
            Name="Beaver",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(3, 15)),
            Weapon=Bite,
            Armor=No_Armor,
            Ability="None",
            Stamina=[35, 35],
            Mana=[0, 0],
            HP=[25, 25]
        )
    elif Name == "Fox":
        return Enemy(
            Name="Fox",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(2, 10)),
            Weapon=Bite,
            Armor=No_Armor,
            Ability="None",
            Stamina=[30, 30],
            Mana=[0, 0],
            HP=[20, 20]
        )
    elif Name == "Bird":
        return Enemy(
            Name="Bird",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(1, 8)),
            Weapon=Bite,
            Armor=No_Armor,
            Ability="None",
            Stamina=[15, 15],
            Mana=[0, 0],
            HP=[10, 10]
        )
    elif Name == "Goat":
        return Enemy(
            Name="Goat",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(2, 12)),
            Weapon=headbutt,
            Armor=No_Armor,
            Ability="None",
            Stamina=[40, 40],
            Mana=[0, 0],
            HP=[35, 35]
        )
    elif Name == "Faun":
        return Enemy(
            Name="Faun",
            Race="Passive Animal",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(15, 50)),
            Weapon=headbutt,
            Armor=No_Armor,
            Ability="None",
            Stamina=[60, 60],
            Mana=[30, 30],
            HP=[50, 50]
        )



    elif Name == "Debug":
        return Enemy(
            Name="Debug",
            Race="Undead",
            Gender=random.choice(["FM", "MM"]),
            Age=str(random.randint(8, 5000)),
            Weapon=Punch,
            Armor=Cloth_Garments,
            Ability="None",
            Stamina=[1000, 1000],
            Mana=[1000, 1000],
            HP=[1000,1000]
        )
    
    

##############################################
# BOSSES




##############################################
# GENERAL LISTS


Debug = "Debug"
Beaver = "Beaver"
Fox = "Fox"
Bird = "Bird"
Goat = "Goat"
Faun = "Faun"
Squirrel = "Squirrel"
Deer = "Deer"
Rabbit = "Rabbit"
BrownBear = "BrownBear"
SavageBoar = "SavageBoar"
VenomousSnake = "VenomousSnake"
GrayWolf = "GrayWolf"
SnowWolf = "SnowWolf"
AlphaWolf = "AlphaWolf"
MountainLion = "MountainLion"
Goblin_Warrior = "GoblinWarrior"
Goblin_Archer = "GoblinArcher"
Goblin_Shaman = "GoblinShaman"
Goblin_King = "GoblinKing"
Kobold_Warrior = "KoboldWarrior"
Svirfneblin_Warrior = "SvirfneblinWarrior"
Gnome_Thief = "GnomeThief"
Orc_Berserker = "OrcBerserker"
Orc_Hunter = "OrcHunter"
Orc_Warlord = "OrcWarlord"
Elf_Mage = "ElfMage"
Elf_Archer = "ElfArcher"
Elf_Guardian = "ElfGuardian"
Troll = "Troll"
Troll_Brute = "TrollBrute"
Vampire_Assassin = "VampireAssassin"
Vampire_Sorcerer = "VampireSorcerer"
Vampire_Lord = "VampireLord"
Werewolf = "Werewolf"
Dwarven_Warrior = "DwarvenWarrior"
Dwarven_Hunter = "DwarvenHunter"
Bandit = "Bandit"
Hunter = "Hunter"
Bandit_Mage = "BanditMage"
Wraith = "Wraith"
Tabaxi_Warrior = "TabaxiWarrior"
Demon = "Demon"
Demon_Lord = "DemonLord"
Demon_Spawn = "DemonSpawn"
Tiefling = "Tiefling"
Infernal_Tiefling = "InfernalTiefling"
Undead_Knight = "UndeadKnight"
Skeleton = "Skeleton"
Spectre = "Spectre"
Zombie = "Zombie"
all_enemies = [
    Debug, Beaver, Fox, Bird, Goat, Faun, Squirrel, Deer, Rabbit, BrownBear,
    SavageBoar, VenomousSnake, GrayWolf, SnowWolf, AlphaWolf, MountainLion,
    Goblin_Warrior, Goblin_Archer, Goblin_Shaman, Goblin_King, Kobold_Warrior,
    Svirfneblin_Warrior, Gnome_Thief, Orc_Berserker, Orc_Hunter, Orc_Warlord,
    Elf_Mage, Elf_Archer, Elf_Guardian, Troll, Troll_Brute, Vampire_Assassin,
    Vampire_Sorcerer, Vampire_Lord, Werewolf, Dwarven_Warrior, Dwarven_Hunter,
    Bandit, Hunter, Bandit_Mage, Wraith, Tabaxi_Warrior, Demon, Demon_Lord,
    Demon_Spawn, Tiefling, Infernal_Tiefling, Undead_Knight, Skeleton, Spectre, Zombie
]
RaceList = [
    "Goblin", "Gnome", 
    "Kobold", "Svirfneblin", "Hobbit", 
    "Elf", "Druid", "Bosmer",
    "Human", 
    "Vampire", 
    "Werewolf", "Lupus", "Wulf", "Halfling", 
    "Orc", "Dragonborn", "Dragonide", 
    "Dwarf", 
    "Troll", 
    "Demon", "Aasimar", 
    "Tiefling", 
    "Kenku", 
    "Tabaxi", "Khajit", 
    "Half-Elf",
    "Fairy",
    "Centaur","Faun"
]

# Heavy
Heavy_Weapons = [
    Hammer,
    DoubleBladedAxe,
    Flail,
    Halberd,
    Club,
    Greatsword,
    Scythe,
    Warhammer
]

# Light
Light_Weapons = [
    Sword,
    BattleAxe,
    Spear,
    Mace,
    Sabre,
    Dagger,
    Katana,
    Rapier
]

# Hand
Hand_Weapons = [
    Punch,
    BaghNakh,
    BrassKnuckles,
    IronFist,
    HandWraps,
    MetalClaw,
    LeatherGlove
]

# Bow
Bow_Weapons = [
    Bow,
    CrystalBow,
    HunterBow,
    ArcaneBow,
    ShadowBow,
    GuardianBow
]

# Spell
All_Spells = [
    MagicBurst,
    Fireball,
    FlameBurst,
    BurningVortex,
    FlameTempest,
    WaterJet,
    FlowingRain,
    TidalBlessing,
    OceanEmbrance,
    StoneFist,
    GraniteShield,
    Rockfall,
    TitanImpact,
    VineWhip,
    RestorativeGrowth,
    VitalBloom,
    CallOfTheForest,
    LightingBolt,
    VoltStrike,
    ElectroNova,
    TempestSurge,
    RadiantStrike,
    Healing,
    FaithShield,
    GoddesBlessing,
    DarkBolt,
    ShadowAbyss,
    CorruptionBloom,
    BlackHole
]

# Arrow

All_Arrow = [
    IronArrow,
    BoneArrow,
    SteelArrow,
    GlassArrow,
    CrystalArrow,
    FlamingArrow,
    IcyArrow,
    PoisonArrow,
    AbyssalArrow,
    WeaknessArrow
]

# Magical
Magical_Weapons = [
    BranchOfSparks,
    StaffOfEmbers,
    ScepterOfFlames,
    CatalystOfTheBlazingSun,
    BranchOfTheDrop,
    StaffOfTheRiver,
    ScepterOfTheSea,
    CatalystOfTheOceans,
    SproutedBranch,
    GrowingStaff,
    ScepterOfTheForest,
    CatalystOfEternalLife,
    BranchOfElectro,
    StaffOfElectricity,
    ScepterOfLightning,
    CatalystOfTheStorm,
    BranchOfThePebble,
    StaffOfTheRock,
    ScepterOfTheMountain,
    CatalystOfPrimordialEarth,
    BranchOfTheCandle,
    StaffOfFaith,
    RadiantScepter,
    DivineCatalyst,
    BranchOfShadows,
    StaffOfDarkness,
    ScepterOfTheAbyss,
    CatalystOfTheAbyss
]


# Special
Special_Weapons = [
    Scratch,
    Claws,
    Bite,
    headbutt
]

# All Weapon Physics

All_Weapon_Physics = [
    Punch,
    Sword,
    Hammer,
    Staff,
    Bow,
    BaghNakh,
    BrassKnuckles,
    IronFist,
    HandWraps,
    MetalClaw,
    LeatherGlove,
    BattleAxe,
    Spear,
    Mace,
    Sabre,
    Dagger,
    Katana,
    Rapier,
    DoubleBladedAxe,
    Flail,
    Halberd,
    Club,
    Greatsword,
    Scythe,
    Warhammer,
    CrystalBow,
    HunterBow,
    ArcaneBow,
    ShadowBow,
    GuardianBow,
]

# All
All_Weapons = [
    Punch,
    Sword,
    Hammer,
    Staff,
    Bow,
    BaghNakh,
    BrassKnuckles,
    IronFist,
    HandWraps,
    MetalClaw,
    LeatherGlove,
    BattleAxe,
    Spear,
    Mace,
    Sabre,
    Dagger,
    Katana,
    Rapier,
    DoubleBladedAxe,
    Flail,
    Halberd,
    Club,
    Greatsword,
    Scythe,
    Warhammer,
    CrystalBow,
    HunterBow,
    ArcaneBow,
    ShadowBow,
    GuardianBow,
    BranchOfSparks,
    StaffOfEmbers,
    ScepterOfFlames,
    CatalystOfTheBlazingSun,
    BranchOfTheDrop,
    StaffOfTheRiver,
    ScepterOfTheSea,
    CatalystOfTheOceans,
    SproutedBranch,
    GrowingStaff,
    ScepterOfTheForest,
    CatalystOfEternalLife,
    BranchOfElectro,
    StaffOfElectricity,
    ScepterOfLightning,
    CatalystOfTheStorm,
    BranchOfThePebble,
    StaffOfTheRock,
    ScepterOfTheMountain,
    CatalystOfPrimordialEarth,
    BranchOfTheCandle,
    StaffOfFaith,
    RadiantScepter,
    DivineCatalyst,
    BranchOfShadows,
    StaffOfDarkness,
    ScepterOfTheAbyss,
    CatalystOfTheAbyss
]

# All Armors

All_Armors = [
    Slave_Rags,
    Cloth_Garments,
    Elf_Robe,
    Elegant_Clothes,
    Poor_Clothes,
    Leather_Garments,
    Merchant_Attire,
    Peasant_Tunic,
    Scholars_Robe,
    Bards_Costume,
    Work_Tunic,
    Leather_Armor,
    Wooden_Armor,
    Paper_Armor,
    Studded_Armor,
    Thiefs_Robes,
    Archers_Robes,
    Goblin_Mail,
    Iron_Chainmail,
    Bandit_Armor,
    Trollhide_Armor,
    Orcish_Armor,
    Warriors_Armor,
    Bone_Armor,
    Nobles_Armor,
    Dwarven_Armor,
    Elven_Armor,
    Vampiric_Armor,
    Knights_Armor,
    Heavy_War_Armor,
    Demonic_Armor,
    Heavy_Elven_Armor,
    Ebony_Armor,
    Heros_Armor,
    Mithril_Armor,
    Dragon_Scale_Armor,
    Legendary_Armor,
    Novice_Mages_Garments,
    Monks_Tunic,
    Mages_Robes,
    Necromancers_Robes,
    Priests_Garments,
    Masters_Robes,
    Golden_Armor,
    Crystal_Armor
]

# All Potions

Potions_List = [
    RawMeat,
    Blood,
    Weak_Healing_Potion,
    Healing_Potion,
    Strong_Healing_Potion,
    Weak_Restore_Potion,
    Restore_Potion,
    Strong_Restore_Potion,
    Weak_Mana_Potion,
    Mana_Potion,
    Strong_Mana_Potion,
    Strength_Potion,
    Potent_Strength_Potion,
    Resistance_Potion,
    Regen_Potion,
    Frost_Potion,
    Poison_Potion,
    Potent_Poison_Potion,
    Anti_Arrow_Potion,
    Recovery_Mana,
    Weakness_Potion
]

Rapid_List = ["Hand",
              "Rapid","Lowering Speed"]
Slow_List = ["Bow","Heavy","Magical",
             "Brute","Lowering Speed"]

Economic_List = [
    BronzeCoin,
    BronzeCoin,
    SilverCoin,
    GoldCoin,
    SilverLingot,
    GoldLingot
]

GENERAL_ALL_LIST_ITEMS = [
    #Spells
    MagicBurst,
    Fireball,
    FlameBurst,
    BurningVortex,
    FlameTempest,
    WaterJet,
    FlowingRain,
    TidalBlessing,
    OceanEmbrance,
    StoneFist,
    GraniteShield,
    Rockfall,
    TitanImpact,
    VineWhip,
    RestorativeGrowth,
    VitalBloom,
    CallOfTheForest,
    LightingBolt,
    VoltStrike,
    ElectroNova,
    TempestSurge,
    RadiantStrike,
    Healing,
    FaithShield,
    GoddesBlessing,
    DarkBolt,
    ShadowAbyss,
    CorruptionBloom,
    BlackHole,

    # Arrows
    IronArrow,
    BoneArrow,
    SteelArrow,
    GlassArrow,
    CrystalArrow,
    FlamingArrow,
    IcyArrow,
    PoisonArrow,
    AbyssalArrow,
    WeaknessArrow,
    
    # Weapons - Physical
    Punch,
    Sword,
    Hammer,
    Staff,
    Bow,
    BaghNakh,
    BrassKnuckles,
    IronFist,
    HandWraps,
    MetalClaw,
    LeatherGlove,
    BattleAxe,
    Spear,
    Mace,
    Sabre,
    Dagger,
    Katana,
    Rapier,
    DoubleBladedAxe,
    Flail,
    Halberd,
    Club,
    Greatsword,
    Scythe,
    Warhammer,
    CrystalBow,
    HunterBow,
    ArcaneBow,
    ShadowBow,
    GuardianBow,
    
    # Weapons - Magical
    BranchOfSparks,
    StaffOfEmbers,
    ScepterOfFlames,
    CatalystOfTheBlazingSun,
    BranchOfTheDrop,
    StaffOfTheRiver,
    ScepterOfTheSea,
    CatalystOfTheOceans,
    SproutedBranch,
    GrowingStaff,
    ScepterOfTheForest,
    CatalystOfEternalLife,
    BranchOfElectro,
    StaffOfElectricity,
    ScepterOfLightning,
    CatalystOfTheStorm,
    BranchOfThePebble,
    StaffOfTheRock,
    ScepterOfTheMountain,
    CatalystOfPrimordialEarth,
    BranchOfTheCandle,
    StaffOfFaith,
    RadiantScepter,
    DivineCatalyst,
    BranchOfShadows,
    StaffOfDarkness,
    ScepterOfTheAbyss,
    CatalystOfTheAbyss,
    
    # Armors
    Slave_Rags,
    Cloth_Garments,
    Elf_Robe,
    Elegant_Clothes,
    Poor_Clothes,
    Leather_Garments,
    Merchant_Attire,
    Peasant_Tunic,
    Scholars_Robe,
    Bards_Costume,
    Work_Tunic,
    Leather_Armor,
    Wooden_Armor,
    Paper_Armor,
    Studded_Armor,
    Thiefs_Robes,
    Archers_Robes,
    Goblin_Mail,
    Iron_Chainmail,
    Bandit_Armor,
    Trollhide_Armor,
    Orcish_Armor,
    Warriors_Armor,
    Bone_Armor,
    Nobles_Armor,
    Dwarven_Armor,
    Elven_Armor,
    Vampiric_Armor,
    Knights_Armor,
    Heavy_War_Armor,
    Demonic_Armor,
    Heavy_Elven_Armor,
    Ebony_Armor,
    Heros_Armor,
    Mithril_Armor,
    Dragon_Scale_Armor,
    Legendary_Armor,
    Novice_Mages_Garments,
    Monks_Tunic,
    Mages_Robes,
    Necromancers_Robes,
    Priests_Garments,
    Masters_Robes,
    Golden_Armor,
    Crystal_Armor,
    
    # Potions
    RawMeat,
    Blood,
    Weak_Healing_Potion,
    Healing_Potion,
    Strong_Healing_Potion,
    Weak_Restore_Potion,
    Restore_Potion,
    Strong_Restore_Potion,
    Weak_Mana_Potion,
    Mana_Potion,
    Strong_Mana_Potion,
    Strength_Potion,
    Potent_Strength_Potion,
    Resistance_Potion,
    Regen_Potion,
    Frost_Potion,
    Poison_Potion,
    Potent_Poison_Potion,
    Anti_Arrow_Potion,
    Recovery_Mana,
    Weakness_Potion,

    #generic items
    ObsidianShard,
    CrystalShard,
    RoughRuby,
    Ruby,
    PureRuby,
    Emerald,
    RoughAmethyst,
    Amethyst,
    PureAmethyst,
    Skull,
    MasterVampirismBook,
    VampirismBook,
    VampireTooth,
    Topaz,
    OpalPearl,
    Diamond,
    PureCrystal,
    SilverNecklace,
    GoldNecklace,
    GemstoneNecklace,
    Bone,
    AnimalFur,
    AnimalHide,
    PrestigeFur,
    GoddessAmulet,
    FaithNecklace,
    ForestFaithAmulet,
    PaganAmulet,
    IronRing,
    SilverRing,
    GoldRing,
    RubyRing,
    DiamondRing,
    Crown,
    CookingPot,
    Rope,
    ScrapAnimal,
    Lantern,
    LeatherPouch,
    FlintAndSteel,
    HerbalKit,  
    Candles,
    Inkwell,
    SilkHandkerchief,
    SmallBell,
    ThreadAndNeedle,
    SmallMirror,
    FlaskOfWine,
    Bucket,
    PouchOfSalt,
    VialOfPerfume,
    PocketWatch,
    Whistle,
    PatchOfCloth,
    GlassBottle,
    Scarf,
    Locket,
    BurntBook,
    IronScraps,
    BrokenWeapon,
    BrokenArmor,
    FracturedAmulet,
    RustyRing
]

Generic_Items_GEMS = [
    ObsidianShard,
    CrystalShard,
    RoughRuby,
    Ruby,
    PureRuby,
    Emerald,
    RoughAmethyst,
    Amethyst,
    PureAmethyst,
    Topaz,
    OpalPearl,
    Diamond,
    PureCrystal,
    SilverNecklace,
    GoldNecklace,
    GemstoneNecklace,
    SilverRing,
    GoldRing,
    RubyRing,
    DiamondRing
]

All_Generic_Items = [
    ObsidianShard,
    CrystalShard,
    RoughRuby,
    Ruby,
    PureRuby,
    Emerald,
    RoughAmethyst,
    Amethyst,
    PureAmethyst,
    Skull,
    MasterVampirismBook,
    VampirismBook,
    VampireTooth,
    Topaz,
    OpalPearl,
    Diamond,
    PureCrystal,
    SilverNecklace,
    GoldNecklace,
    GemstoneNecklace,
    Bone,
    AnimalFur,
    AnimalHide,
    PrestigeFur,
    GoddessAmulet,
    FaithNecklace,
    ForestFaithAmulet,
    PaganAmulet,
    IronRing,
    SilverRing,
    GoldRing,
    RubyRing,
    DiamondRing,
    Crown,
    CookingPot,
    Rope,
    ScrapAnimal,
    Lantern,
    LeatherPouch,
    FlintAndSteel,
    HerbalKit,  
    Candles,
    Inkwell,
    SilkHandkerchief,
    SmallBell,
    ThreadAndNeedle,
    SmallMirror,
    FlaskOfWine,
    Bucket,
    PouchOfSalt,
    VialOfPerfume,
    PocketWatch,
    Whistle,
    PatchOfCloth,
    GlassBottle,
    Scarf,
    Locket,
    BurntBook,
    IronScraps,
    BrokenWeapon,
    BrokenArmor,
    FracturedAmulet,
    RustyRing
]

Generic_Drops_Items = [
    ObsidianShard,
    CrystalShard,
    RoughRuby,
    Ruby,
    PureRuby,
    Emerald,
    RoughAmethyst,
    Amethyst,
    PureAmethyst,
    Topaz,
    OpalPearl,
    Diamond,
    PureCrystal,
    SilverNecklace,
    GoldNecklace,
    GemstoneNecklace,
    IronRing,
    SilverRing,
    GoldRing,
    RubyRing,
    DiamondRing,
    CookingPot,
    Rope,
    Lantern,
    LeatherPouch,
    FlintAndSteel,
    HerbalKit,
    Candles,
    Inkwell,
    SilkHandkerchief,
    SmallBell,
    ThreadAndNeedle,
    SmallMirror,
    FlaskOfWine,
    Bucket,
    PouchOfSalt,
    VialOfPerfume,
    PocketWatch,
    Whistle,
    PatchOfCloth,
    GlassBottle,
    Scarf,
    Locket,
    BurntBook,
    IronScraps,
    BrokenWeapon,
    BrokenArmor,
    FracturedAmulet,
    RustyRing
]

All_Animal_Drops = [
    Bone,
    AnimalFur,
    AnimalHide,
    PrestigeFur,
    AnimalClaws,
    RawMeat,
    Blood,
    ScrapAnimal
]



##############################################
# LOOT TABLE
rarity = {
    "common": 40,
    "uncommon": 20,
    "rare": 10,
    "epic": 2,
    "legendary": 0.5,
    "mythical": 0.1
}

rarity_medium = {
    "common": 10,
    "uncommon": 20,
    "rare": 30,
    "epic": 10,
    "legendary": 5,
    "mythical": 1
}

rarity_legendary = {
    "common": 2,
    "uncommon": 10,
    "rare": 20,
    "epic": 40,
    "legendary": 30,
    "mythical": 10
}

def RarityMatch_LootDrop(A_item,mpx):
    match A_item.R_E[0].lower():
        case "common":
            tempWeight = [0.9,0.1]
        case "uncommon":
            tempWeight = [0.7,0.3]
        case "rare":
            if mpx == "Fortune":
                tempWeight = [0.7,0.3]
            else:
                tempWeight = [0.5,0.5]
        case "epic":
            if mpx == "Fortune":
                tempWeight = [0.7,0.3]
            else:
                tempWeight = [0.4,0.6]
        case "legendary":
            if mpx == "Fortune":
                tempWeight = [0.6,0.4]
            else:
                tempWeight = [0.3,0.7]
        case "mythical":
            tempWeight = [0.8,0.2]

    return tempWeight

def CreateLootDrop(npc,mpx):
    Drop = []

    Attr = npc.Attribute_Return()

    if Attr[1].type != "Special" and Attr[2].name != "None" and Attr[2].name != "Punch":
        tempFor = [Attr[1],Attr[2]]
        for A_item in tempFor:
            tempWeight = RarityMatch_LootDrop(A_item,mpx)
            randomdropscrapt = random.choice([IronScraps,BrokenArmor,BrokenWeapon])
            Drop.append(random.choices([A_item,randomdropscrapt],tempWeight,k=1)[0])
        
        if Attr[1].type == "Bow":
            tempWeight = RarityMatch_LootDrop(Attr[1].ammo,mpx)
            for _ in range(random.randint(1,6)):
                Drop.append(random.choices([Attr[1].ammo,IronScraps],tempWeight,k=1)[0])
        CreateLootTable
        if Attr[1].type == "Magical":
            tempWeight = RarityMatch_LootDrop(Attr[1].ammo,mpx)
            Drop.append(random.choices([Attr[1].ammo,BurntBook],tempWeight,k=1)[0])
            
            tempFor = CreateLootTable(random.randint(1,3),All_Spells,"NB",rarity)[1]
            for A_item in tempFor:
                tempWeight = RarityMatch_LootDrop(A_item,mpx)
                Drop.append(random.choices([A_item,BurntBook],tempWeight,k=1)[0])
    
    match Attr[3]:
        case "Animal" | "Passive Animal" | "Alpha Animal":
            TempListOfDrop = CreateLootTable(4,All_Animal_Drops,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)
            Drop.append(RawMeat)

        case "Goblin" | "Gobliniano" | "Gobliniana" | "Kobold" | "Svirfneblin" | "Kenku" | "Aarakocra":
            GoblinDrop_List = [AnimalHide,Rope,HerbalKit,Candles,Bucket,PatchOfCloth,IronScraps,RustyRing,RoughAmethyst,RoughRuby]
            TempListOfDrop = CreateLootTable(5,GoblinDrop_List,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)
            if "win" == random.choices(["win","nop"],[0.6,0.4],k=1)[0]:
                Drop.append(PaganAmulet)
            else:
                Drop.append(FracturedAmulet)

        case "Vampire" | "Vampiro" | "Vampira" | "Vampiric":
            VampireDrop_List = [VampireBloodJar,Blood,BrokenVial,VampireTooth,VampirismBook,MasterVampirismBook,Skull,Bone,PatchOfCloth,RawMeat,Poison_Potion,Weakness_Potion,Dagger,BurntBook]
            VampireDrop_List.extend(Generic_Items_GEMS)
            TempListOfDrop = CreateLootTable(7,VampireDrop_List,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)

        case "Werewolf" | "Lupo Mannaro" | "Lupus" | "Wulf":
            TempListOfDrop = CreateLootTable(4,All_Animal_Drops,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)

        case "Demon" | "Demoniac" | "Demone" | "Demoniaca" | "Aasimar" | "Succubs":
            DemonDrop_List = [VialOfPerfume,Blood,Skull,Bone,Rope,BurntBook,Frost_Potion,Burn_Potion,Resistance_Potion,Poison_Potion,Lantern,PatchOfCloth,FracturedAmulet,AnimalFur]
            DemonDrop_List.extend(Generic_Items_GEMS)
            TempListOfDrop = CreateLootTable(8,DemonDrop_List,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)

        case "Tabaxi" | "Khajit" | "Wraith" | "Strega":
            PotionistDrop_List = [CookingPot,FlintAndSteel,VialOfPerfume,BrokenVial,FracturedAmulet,Dagger,Skull,Bone,Rope,BurntBook,ScrapAnimal,WoodScraps,Lantern,PouchOfSalt,RawMeat]
            PotionistDrop_List.extend(Potions_List)
            PotionistDrop_List.extend(Generic_Items_GEMS)
            TempListOfDrop = CreateLootTable(8,PotionistDrop_List,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)

            if Attr[3] in ["Tabaxi","Khajit"]:
                Drop.append(PaganAmulet)

        case "Troll" | "Trolliano" | "Giant" | "Giganti" | "Gigante":
            GigantDrop_List = [IronScraps,Bone,Skull,RustyRing,WoodScraps,BrokenVial,BrokenWeapon,BrokenArmor]
            GigantDrop_List.extend(All_Animal_Drops)
            TempListOfDrop = CreateLootTable(6,GigantDrop_List,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)

        case "Bosmer" | "Wood-Elf" | "Wood-Elves" | "Wood Elf" | "Wood Elves":
            BosmerDrop_List = [AnimalFur,FlaskOfWine,VialOfPerfume,PatchOfCloth,Lantern,Rope,WoodScraps,Frost_Potion,Burn_Potion,Poison_Potion,HerbalKit,AnimalFur,LeatherPouch]
            BosmerDrop_List.extend(Generic_Items_GEMS)
            BosmerDrop_List2 = All_Arrow
            TempListOfDrop1 = CreateLootTable(2,BosmerDrop_List2,"NB",rarity)[1]
            TempListOfDrop = CreateLootTable(6,BosmerDrop_List,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)
            Drop.extend(TempListOfDrop1)
            Drop.append(ForestFaithAmulet)

        case _:
            RandomRaceDrop_List = [Regen_Potion,Weak_Restore_Potion,Weak_Healing_Potion,Weak_Mana_Potion,Healing_Potion,Restore_Potion,Poison_Potion,Anti_Arrow_Potion,Strength_Potion]
            RandomRaceDrop_List.extend(Generic_Drops_Items)
            RandomRaceDrop_List.append(Bone)
            TempListOfDrop = CreateLootTable(8,RandomRaceDrop_List,"NB",rarity)[1]
            Drop.extend(TempListOfDrop)
            if "win" == random.choices(["win","nop"],[0.7,0.3],k=1)[0]:
                Drop.append(FaithNecklace)
            else:
                Drop.append(GoddessAmulet)
            
    return Drop

def CreateLootTable(pull, list_of_items, name, rarity):
    Rtotal = sum(rarity.values())
    normalized_rarity = {k: v / Rtotal for k, v in rarity.items()}

    Chest = []
    List_of_All_Items = list_of_items
    List_of_Rarity = list(normalized_rarity.keys())
    List_of_Probabilities = list(normalized_rarity.values())
    
    while True:
        Pity_Fortune = random.choices(List_of_Rarity, List_of_Probabilities, k=pull)
        for item_rarity in Pity_Fortune:
            List_of_All_Possible_Items = [i for i in List_of_All_Items if i.R_E[0].upper() == item_rarity.upper()]
            
            if not List_of_All_Possible_Items:
                return CreateLootTable(pull, list_of_items, name, rarity)
            
            Chest.append(random.choice(List_of_All_Possible_Items))
        
        if Chest: 
            break
    
    return [name, Chest]

        
    
