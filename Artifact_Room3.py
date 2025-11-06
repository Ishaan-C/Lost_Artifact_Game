#Room 3- Number Guesser
import math
import random
import sys  
from Artifact_Room4 import Room4
class Room3:

    def __init__(self, player):
        self.player = player


    def RRoom3(self):
        print("WELCOME TO ROOM 3! You must guess the secret number to proceed...")

        self.secret_number=random.randint(1, 100)
        print("A magical lock bars your way. Guess the secret number between 1 and 100. You are allowed 7 tries.")

        self.attempts=0
        self.fl=False
    

        for i in range (7):
            self.inp=int(input(("Enter a number: ")))
            self.attempts+=1
            if(self.inp!=self.secret_number):
                self.hint(self.secret_number,self.attempts)
                continue
            else:
                self.fl=True
                print("Correct! You may proceed to the Final Room...\v")
                Stage3=Room4(self.player)
                Stage3.RRoom4()
        
        if self.fl==False:
            print("You failed!!")
            sys.exit(0)

    def hint(self,n,a):
        if a==1:
            if n>=50:
                print("It is greater than or equal to 50")
            else:
                print("It is less than 50")
        
        if a==2:
            if n%5==0:
                print("It is divisible by 5")
            else:
                print("It is not divisible by 5")
        
        if a==3:
            sqr=int(math.sqrt(n))
            if sqr<=36:
                print("The square root is less than or equal to 6")
                

        if a==5:
            print("The last digit of the number is",(n%10))

        






