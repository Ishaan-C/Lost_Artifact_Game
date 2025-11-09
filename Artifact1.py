#This is a class to set up all functions associated with the game
#This is a class to set up all functions associated with the game
import sys
class Artifact:


    def setUp(self):

        self.name = input("Enter your username: ")

        self.player = {
            "UName": self.name,
            "coins": 1000,
            "health": 100
        }
        self.inventory=[]
    

    def addCoins(self, hp):
        self.player["coins"]+=hp
        print("Coins added. New balance: ", self.player["coins"])


    
    def spendCoins(self,price,item):
        if(self.player["coins"]>=price):
            self.player["coins"]-=price
            self.inventory.append(item)
            print("Item succesfully bought. New balance: ",self.player["coins"])
        else:
            print("Insufficient coins")


    def take_damage(self, damage):
        self.player["health"] -= damage
        if self.player["health"] <= 0:
            print("Player is dead!")
            sys.exit(0)
        else:
            print(f"Player took {damage} damage. Health now: {self.player['health']}")


    def heal(self):
        if self.player["health"]<=60:
            self.player["health"]+=40
        else:
            self.player["health"]=100
        self.inventory.remove("Health Potion")


    def display(self):
        print("Name:",self.player["UName"])
        print("Coins:",self.player["coins"])
        print("Health:",self.player["health"])
        print("Inventory:",self.inventory)


    def shop(self):
        self.ShopItem=int(input("Enter your choice: \n1.Magic Sword--deals 300 HP damage at a time--900 coins\n2.Basic Sword--deals 20HP damage at a time--100 coins\n3.Health Potion--Heals upto 40HP--250 coins\n"))
        if(self.ShopItem==1):
            self.spendCoins(900,"Magic Sword")
        elif(self.ShopItem==2):
            self.spendCoins(100,"Basic Sword")
        elif(self.ShopItem==3):
            self.spendCoins(250,"Health Potion")
        else:
            print("Invalid Choice")


