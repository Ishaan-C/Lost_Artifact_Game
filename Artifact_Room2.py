# Room 2 - Monster 1 Battle
from Artifact_Room3 import Room3

class Room2:

    def __init__(self, player):
        self.player = player


    def RRoom2(self):
        print("WELCOME TO ROOM 2! Beat the Titan to proceed...")
        self.MONSTER1()
        self.BATTLE1()

    def MONSTER1(self):
        self.monster = {
            "UName": "Titan",
            "health": 200
        }

    def BATTLE1(self):
        print("You go first. These are the stats of the Titan.")
        print("Name: Titan \nHealth: 200")

        if input("Do you want to go to the shop?   Y/N\n").upper() == "Y":
            self.player.shop()

        while self.monster["health"] > 0:
            # Player chooses which items to use
            for i in range(len(self.player.inventory)):
                if self.player.inventory[i] == "Magic Sword":
                    self.uo = input("Would you like to use the Magic Sword?   Y/N\t")
                    if self.uo.upper() == "Y":
                        self.monster["health"] -= 300
                        print("Remaining health:",self.monster["health"])
                    else:
                        continue

                if self.player.inventory[i] == "Basic Sword":
                    self.uo = input("Would you like to use the Basic Sword?   Y/N\t")
                    if self.uo.upper() == "Y":
                        self.monster["health"] -= 20
                        print("Remaining health:",self.monster["health"])
                    else:
                        continue

                if self.player.inventory[i] == "Health Potion":
                    self.uo = input("Would you like to use the Health Potion? Y/N\t")
                    if self.uo.upper() == "Y":
                        self.player.heal()
                    else:
                        continue

            if self.monster["health"]>0:            
                if self.player.player["health"] >= 10:
                    print("The Titan strikes back! He flicks his finger and pushes you against a brick wall")
                    self.player.take_damage(15)
                else:
                    print("The Titan jumps on you! Too late...")
                    self.player.take_damage(40)
                    
        print("You defeated the Titan. Congratulations brave warrior! Proceed to Room 3\v")
        print("You've earned a reward.")
        self.player.addCoins(1000)
        Stage3=Room3(self.player)
        Stage3.RRoom3()
