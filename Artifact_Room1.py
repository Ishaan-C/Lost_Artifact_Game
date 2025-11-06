#Room 1
import sys
from Artifact_Room2 import Room2
class Room1:
    def __init__(self,player):
        self.player = player



    def RRoom1(self):
        print("WELCOME TO ROOM 1! Solve these riddles to proceed...")
        self.check()
        


    def riddles(self):
        self.questions=["What has keys but can't open locks?","What has hands but can't clap?","What gets wetter as it dries?"]
        self.answers=["piano","clock","towel"]

    def check(self):
        print("Your task for getting past room 1 is to answer a set of questions. Get one wrong and it's over!")
        self.riddles()
        for i in range (3):
            ans=input(self.questions[i]+"\n")
            if ans.lower()!=self.answers[i]:
                print("YOU FAILED! TRY AGAIN NEXT TIME")
                sys.exit(0)
            else:
                continue

        print("You passed! Now proceeding to Room 2...\v")
        Stage2=Room2(self.player)
        Stage2.RRoom2()

    



