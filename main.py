from random import randint, randrange

################################
#
# TO DO:
#
# Add the rest of the potions available to buy
# Create the other creatures and add them into the enemy list
#
# Add blocking to fight commands? how much damage blocked equals damage * 2???
#
#
# Add current hp for enemy similar to current hp for the player?
#
################################

class Character():
    def __init__(self, name, hp, damage, gold, movement):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.gold = gold
        self.movement = movement

class Player(Character):
    def __init__(self):
        super(Player, self).__init__(name="",
                                     hp=50,
                                     damage=3,
                                     gold=10,
                                     movement=3)
# Enemies
class Enemy(Character):
    def __init__(self, name, hp, damage, gold, movement):
        super(Enemy, self).__init__(name,
                                    hp,
                                    damage,
                                    gold,
                                    movement)


class Drake(Enemy):
    def __init__(self):
        super(Drake, self).__init__(name="Drake",
                                    hp=14,
                                    damage=5,
                                    gold=10,
                                    movement=7)

class GiantSpider(Enemy):
    def __init__(self):
        super(GiantSpider, self).__init__(name="Giant Spider",
                                          hp=3,
                                          damage=1,
                                          gold=1,
                                          movement=5)

class GoldenGnome(Enemy):
    # Rare enemy that can potentially drop a lot of gold
    def __init__(self):
        super(GoldenGnome, self).__init__(name="Golden Gnome",
                                          hp=1,
                                          damage=0,
                                          gold=randint(1, 100),
                                          movement=0)

class Slime(Enemy):
    def __init__(self):
        super(Slime, self).__init__(name="Slime",
                                    hp=10,
                                    damage=4,
                                    gold=15,
                                    movement=3)

class Zombie(Enemy):
    def __init__(self):
        super(Zombie, self).__init__(name="Zombie",
                                     hp=5,
                                     damage=5,
                                     gold=5,
                                     movement=1)

# Boss Fight Enemies
class ElderDragon(Enemy):
    def __init__(self):
        super(ElderDragon, self).__init__(name="Elder Dragon",
                                          hp=20,
                                          damage=7,
                                          gold=50,
                                          movement=10)

class Item():
    def __init__(self, name, description, value, price, sell):
        # name of item
        self.name = name
        # short description of item
        self.description = description
        # value is the amount of hp/damage a potion will do
        self.value = value
        # purchase price from the shop
        self.price = price
        # how much the shop will pay for the item
        self.sell = sell

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Potions
class HPincrease(Item):
    def __init__(self):
        super(HPincrease, self).__init__(name="HP up Potion",
                                         description="A potion that will increase your max hp by 5 points"
                                                     "and restore all of your hp",
                                         value=5,
                                         price=10,
                                         sell=3)

class HealthPotion(Item):
    def __init__(self):
        super(HealthPotion, self).__init__(name="Health Potion",
                                           description="A Potion that will restore 4 health",
                                           value=4,
                                           price=3,
                                           sell=2)

class StrengthPotion(Item):
    def __init__(self):
        super(StrengthPotion, self).__init__(name="Strength Potion",
                                             description="A Potion that increases your damage by 2",
                                             value=3,
                                             price=10,
                                             sell=3)

class PoisonPotion(Item):
    def __init__(self):
        super(PoisonPotion, self).__init__(name="Poison Potion",
                                           description="A Potion that deals diminishing damage over time",
                                           value=3,
                                           price=8,
                                           sell=2)

# Weapons
# Not yet incorporated
class Weapon(Item):
    def __init__(self, name, description, damage, price, sell):
        self.damage = damage
        super(Weapon, self).__init__(name="",
                                     description="",
                                     # value is unnecessary for weapons but needed to avoid error
                                     value=0,
                                     price=0,
                                     sell=0)

class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__(name="Dagger",
                                     description="A small rusty dagger",
                                     damage=2,
                                     price=2,
                                     sell=1)

# Main Character
player = Player()
playerhp = Player().hp
potionplayerlist = []
currenthp = playerhp
maxhp = playerhp
currentgold = Player().gold
currentattack = Player().damage

# Current Round
wave = 1

# Items
# Potions
HealthPotion = HealthPotion()
HPincrease = HPincrease()
StrengthPotion = StrengthPotion()
PoisonPotion = PoisonPotion()


# Weapons
Dagger = Dagger()


# Shop
potionlist = [HealthPotion.name, HPincrease.name, PoisonPotion.name, StrengthPotion.name]
potionlist = sorted(potionlist, key=str.lower)


# Enemies
Drake = Drake()
GiantSpider = GiantSpider()
GoldenGnome = GoldenGnome()
Slime = Slime()
Zombie = Zombie()

# Boss Enemies
ElderDragon = ElderDragon()


enemyhp = 1
poison = 0
#enemyhp = enemyhp * wave

def death():
    print()
    print("==================")
    print("| You have died! |")
    print("==================")
    return



def fight(enemyname, enemyhealth, enemydamage, enemygold):
    # Enemy health goes before the while loop nested in the if loop
    # allows for the enemy to regain health when chosen again after
    # being in a previous round

    # Could make health, damage, and gold a variable so that it can scale with the round
    # making the enemies stronger and harder for the player



    global wave
    global currenthp
    global maxhp
    global currentgold
    global currentattack
    global enemyhp
    global poison



    print("What do you want to do?")
    enemydamage = enemydamage * (wave * 0.5)
    enemydamage = round(enemydamage)
    enemyhp = enemyhealth
    currentenemyhp = enemyhp * (wave * 0.5)
    currentenemyhp = round(currentenemyhp)
    enemygold = enemygold
    enemygold = round(enemygold, 0)


    while enemyhp and currenthp > 0:
        choice = input("\nATTACK or use a POTION?\n--> ")
        choice = choice.lower()

        if choice == "attack":


            print("\nYou attack for " + str(currentattack) + " damage!")
            currentenemyhp = currentenemyhp - currentattack
            print("The " + str(enemyname) + " has " + str(currentenemyhp) + " health remaining!")

            if poison > 0:
                print("\nThe poison hurts the " + str(enemyname) + " for " + str(poison) + " damage")
                poison = poison - 1
                currentenemyhp = currentenemyhp - poison
                print("The " + str(enemyname) + " has " + str(currentenemyhp) + " health remaining!")
                print("The poison is going to wear off in " + str(poison) + " turns")
                if currentenemyhp <= 0:
                    poison = 0
                    print("\n* * * * * * Round Won * * * * * *")
                    print("You defeated the " + str(enemyname))
                    print("You looted " + str(enemygold) + " gold from " + str(enemyname))
                    currentgold = currentgold + enemygold
                    print("You have " + str(currentgold) + " gold!\n")
                    break
                else:
                    pass
            else:
                pass

            if currentenemyhp <= 0:
                print("\n* * * * * * Round Won * * * * * *")
                print("You defeated the " + str(enemyname))
                print("You looted " + str(enemygold) + " gold from " + str(enemyname))
                currentgold = currentgold + enemygold
                print("You have " + str(currentgold) + " gold!\n")
                break
            else:
                pass

            print("\nThe " + str(enemyname) + " attacks for " + str(enemydamage) + " damage!")
            currenthp = currenthp - enemydamage

            if currentenemyhp <= 0:
                print("\n* * * * * * Round Won * * * * * *")
                print("You defeated the " + str(enemyname))
                print("You looted " + str(enemygold) + " gold from " + str(enemyname))
                currentgold = currentgold + enemygold
                print("You have " + str(currentgold) + " gold!\n")
                break
            else:
                pass

            if currenthp <= 0:
                death()
            else:
                print("You have " + str(currenthp) + " health remaining!\n")

        elif choice == "potion":
            print("\nYou have these potions in your bag:\n" + str(potionplayerlist))
            chosenpotion = input("Which potion do you want to use?\n-->")
            chosenpotion = chosenpotion.lower()

            for potion in potionplayerlist:
                if chosenpotion == "health":

                    print("\nYou drink the Health potion and restore " + str(HealthPotion.value) + " HP!")
                    currenthp = currenthp + HealthPotion.value
                    potionplayerlist.remove(potion)
                    print("You now have " + str(currenthp))
                    print("Potions left:\n" + str(potionplayerlist))

                elif chosenpotion == "hp up":

                    print("\nYou drink the HP up potion and increase your hp by " + str(HPincrease.value) + " points!")
                    maxhp = maxhp + HPincrease.value
                    currenthp = maxhp
                    potionplayerlist.remove(potion)
                    print("You now have " + str(maxhp))
                    print("Potions left:\n" + str(potionplayerlist))

                elif chosenpotion == "strength":

                    print("\nYou drink the Strength potion and your damage has increased by " + str(StrengthPotion.value))
                    currentattack = currentattack + StrengthPotion.value
                    potionplayerlist.remove(potion)
                    print("You now have " + str(currentattack) + " damage")
                    print("Potions left:\n" + str(potionplayerlist))

                elif chosenpotion == "poison":
                    poison = poison + PoisonPotion.value
                    print("\nYou throw the glowing green veil at the " + str(enemyname) + " inflicting it with " + str(poison) + " poison damage")
                    potionplayerlist.remove(potion)
                    print("Potions left:\n" + str(potionplayerlist))

                else:
                    print("\nYou frantically search through the potions that you have")

            print("\nThe " + str(enemyname) + " attacks for " + str(enemydamage) + " damage!")
            currenthp = currenthp - enemydamage
            print("You have " + str(currenthp) + " health remaining!\n")

            if currenthp <= 0:
                death()
            else:
                pass

        else:
            print("\nThe " + str(enemyname) + " is getting ready to strike what are you gonna do?\n")
    wave = wave + 1
    return wave, currenthp, currentgold

def potionbuy(potionname, potionprice):
    global currentgold

    print("\nAhh I see you are interested in the " + str(potionname))
    print("The cost is " + str(potionprice) + " gold")

    while True:
        confirm = input("YES or NO\n--> ")
        if confirm == "yes" or confirm == "y":
            potionplayerlist.append(potionname)
            currentgold = currentgold - (potionprice)

            print("\nYou add a " + str(potionname) + " to your bag")
            print("Current Potions: " + str(potionplayerlist))
            print("\nYou have " + str(currentgold) + " gold.")
            break
        elif confirm == "no" or confirm == "n":
            print("\nChanged your mind?")
            break
        else:
            print("\nWhat was that?")

def potionselling(potionname, potionsell):
    global currentgold

    print("\nSo you want to sell " + str(potionname))
    print("I'll buy it for " + str(potionsell) + " gold")

    while True:
        confirm = input("YES or NO\n--> ")
        if confirm == "yes" or confirm == "y":
            potionplayerlist.remove(potionname)
            currentgold = currentgold + (potionsell)

            print("\nYou remove " + str(potionname) + " from your bag")
            print("Current Potions: " + str(potionplayerlist))
            print("\nYou have " + str(currentgold) + " gold.")
            break
        elif confirm == "no" or confirm == "n":
            print("\nChanged your mind?")
            break
        else:
            print("\nWhat was that?")

def main():

    global wave
    global currenthp
    global currentgold
    global maxhp
    global currentattack

    # Player Stats
    # Keep player hp out of while loop to remain consistent throughout the waves

    print("Welcome to the Grand Arena")
    print("")


    while currenthp > 0:
        shop = input("\nDo you want to continue the FIGHT, visit the SHOP, or drink a POTION?\n--> ")
        shop = shop.lower()

        # works but need to change the odds of getting gnome
        Opponent = [GiantSpider, GoldenGnome, Zombie, Drake, Slime]
        RandomEnemy = randrange(0, len(Opponent))

        if shop == "shop":
            print("\nWelcome to the shop")

            purchase = input("Are you BUYING or SELLING?\n--> ")
            purchase = purchase.lower()

            if purchase == "buying" or purchase == "buy":
                while True:
                    print("\nWhat would you like to buy?")
                    print("EXIT to leave the shop")

                    potionadd = input("If you want a DESCRIPTION of each potion let me know otherwise,\n\nWe have these potions: \n"+ str(potionlist) + "\n--> ")
                    potionadd = potionadd.lower()

                    if potionadd == "health":
                        potionbuy(HealthPotion.name, HealthPotion.price)

                    elif potionadd == "hp up":
                        potionbuy(HPincrease.name, HPincrease.price)

                    elif potionadd == "strength":
                        potionbuy(StrengthPotion.name, StrengthPotion.price)

                    elif potionadd == "poison":
                        potionbuy(PoisonPotion.name, PoisonPotion.price)

                    elif potionadd == "description" or potionadd == "desc":
                        # health potion
                        print("\nThe Health potion will restore 4 health")
                        # hp increase potion
                        print("\nThe HP Increase potion will restore you to full health as well as increase your max hp by " + str(HPincrease.value))
                        # strength potion
                        print("\nThe Strength potion increase your max damage by " + str(StrengthPotion.value))
                        # poison potion
                        print("\nThe Poison potion will deal " + str(PoisonPotion.value) + " damage and decrease by 1 each turn in combat")

                    elif potionadd == "exit":
                        break

                    else:
                        print("is that all")

            elif purchase == "selling" or purchase == "sell":
                while True:
                    print("\nWhat would you like to sell?")
                    print("EXIT to leave the shop")

                    potionremove = input("\nI see you have" + str(potionplayerlist) + "\n--> ")
                    potionremove = potionremove.lower()

                    if potionremove == "health":
                        potionselling(HealthPotion.name, HealthPotion.sell)

                    elif potionremove == "hp up":
                        potionselling(HPincrease.name, HPincrease.sell)

                    elif potionremove == "strength":
                        potionselling(StrengthPotion.name, StrengthPotion.sell)

                    elif potionremove == "poison":
                        potionselling(PoisonPotion.name, PoisonPotion.sell)

                    elif potionremove == "exit":
                        break

                    else:
                        print("Is that all?")

            else:
                print("\nQuit wasting my time and get out")

        elif shop == "fight":
            wave = wave

            if wave % 10 == 0:
                print('\nRound: ' + str(wave))
#                print("\nPrepare for a Boss Fight")
            else:
                print('\nRound: ' + str(wave))

            if RandomEnemy == 0:
                wave = wave
                print("\nA Giant Spider repels down from the ceiling!")
                fight(GiantSpider.name, GiantSpider.hp, GiantSpider.damage, GiantSpider.gold)

            elif RandomEnemy == 1:
                wave = wave
                print("\nA shiny gold Gnome just stares into your soul.")
                fight(GoldenGnome.name, GoldenGnome.hp, GoldenGnome.damage, GoldenGnome.gold)

            elif RandomEnemy == 2:
                wave = wave
                print("\nA Zombie climbs out from the ground and begins to shuffle towards you.")
                fight(Zombie.name, Zombie.hp, Zombie.damage, Zombie.gold)

            elif RandomEnemy == 3:
                wave = wave
                print("\nA drake swoops down from above!")
                fight(Drake.name, Drake.hp, Drake.damage, Drake.gold)

            elif RandomEnemy == 4:
                wave = wave
                print("\nA dark green slime inches out from the grates")
                fight(Slime.name, Slime.hp, Slime.damage, Slime.gold)

            else:
                pass

        elif shop == "potion":
            print("\nYou have these potions in your bag:\n" + str(potionplayerlist))
            potionselect = input("Which potion do you want to use?\n-->")
            potionselect = potionselect.lower()

            for potion in potionplayerlist:
                if potionselect == "health":

                    print("\nYou drink the Health potion and restore " + str(HealthPotion.value) + " HP!")
                    currenthp = currenthp + HealthPotion.value
                    potionplayerlist.remove(potion)
                    print("You now have " + str(currenthp))
                    print("Potions left:\n" + str(potionplayerlist))

                elif potionselect == "hp up":

                    print("\nYou drink the HP up potion and increase your hp by " + str(HPincrease.value) + " points!")
                    maxhp = maxhp + HPincrease.value
                    currenthp = maxhp
                    potionplayerlist.remove(potion)
                    print("You now have " + str(maxhp))
                    print("Potions left:\n" + str(potionplayerlist))

                elif potionselect == "strength":

                    print("\nYou drink the Strength potion and your damage has increased by " + str(StrengthPotion.value))
                    currentattack = currentattack + StrengthPotion.value
                    potionplayerlist.remove(potion)
                    print("You now have " + str(currentattack) + " damage")
                    print("Potions left:\n" + str(potionplayerlist))

                elif potionselect == "poison":
                    print("\nYou shake the veil and watch as the glowing green liquid swirls inside")

                else:
                    print("\nTime to continue the fight?")



        else:
            print("\nYou look around trying to decide your next course of action")
            print("\nChoose to FIGHT, visit the SHOP, or drink a POTION")


main()
