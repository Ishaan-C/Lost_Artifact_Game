#Room 4- Final Boss
class Room4:

    def __init__(self, player):
        self.player = player

    def RRoom4(self):
        print("WELCOME TO ROOM 4! Beat the EndBringerr to proceed...")
        self.MONSTER2()
        self.BATTLE2()

    def MONSTER2(self):
        self.monster = {
            "UName": "EndBringerr",
            "health": 1000
        }

    def BATTLE2(self):
        print("You go first. These are the stats of the EndBringerr.")
        print("Name: The EndBringerr \nHealth: 1000")

        if input("Do you want to go to the shop?   Y/N\n") == "Y":
            self.player.shop()

        while self.monster["health"] > 0:
            # Player chooses which items to use
            for i in range(len(self.player.inventory)):
                if self.player.inventory[i] == "Magic Sword":
                    self.uo = input("Would you like to use the Magic Sword?   Y/N\t")
                    if self.uo == "Y":
                        self.monster["health"] -= 300
                    else:
                        continue

                if self.player.inventory[i] == "Basic Sword":
                    self.uo = input("Would you like to use the Basic Sword?   Y/N\t")
                    if self.uo == "Y":
                        self.monster["health"] -= 20
                    else:
                        continue

                if self.player.inventory[i] == "Health Potion":
                    self.uo = input("Would you like to use the Health Potion? Y/N\t")
                    if self.uo == "Y":
                        self.player.heal()
                    else:
                        continue

            if self.monster["health"]>0:
                if self.player.player["health"] >= 10:
                    print("The EndBringerr blows its fiery breath upon you!")
                    self.player.take_damage(25)
                else:
                    print("The EngBringerr eats you! Too late...")
                    self.player.take_damage(100)
        print("You defeated the EndBringerr. ")
        print("You won 10000 coins as a reward! Here's your new balance-")
        self.player.addCoins(10000)
        print("Congratulations brave warrior! Thanks to you, the lost artifact has been found, and the people of Rome breathe hope once more. Ages of shadow and longing give way to light, and a new chapter begins for all who call this land home.")
    
        