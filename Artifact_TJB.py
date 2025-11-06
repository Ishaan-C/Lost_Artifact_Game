#This class begins the story

from Artifact1 import Artifact
from Artifact_Room1 import Room1


class TJB:

    def __init__(self, player):
        self.player = player


    
    def introduction(self):
        print("Brave adventurer! You have been chosen to take the perilous path to recover the Lost Artifact of Olympus. The ancient Romans groan beneath a merciless sun, their once-fertile fields cracked and barren, crops withered to dust as the life of the land seeps away. The Artifact is their only hope. Your task is to solve puzzles and defeat monsters that come along the way. Proceed to the shop to buy any aid...")
        self.player.shop()
        print("Congrats on your first purchase! You are in front of the Temple of the Sun. Let's proceed to Room 1...\v")
        Stage1=Room1(self.player)
        Stage1.RRoom1()





