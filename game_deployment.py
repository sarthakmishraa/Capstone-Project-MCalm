import random
from typing import Counter

# returns the nearest multiple to 4
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near
  
def lose1():
    return "You Lose \nBetter luck next time"
    # print ("\n\nYOU LOSE !")
    # print("Better luck next time !")
    # exit(0)

def win1():
    return "You Win"
      
# checks whether the numbers are consecutive
def check(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True
  
# starts the game
def start1(a):
    xyz = []
    last = 0
    while True:
        print ("Enter 'f' to take the first chance.")
        print("Enter 's' to take the second chance.")
        chance = a
          
        # player takes the first chance
        if chance == "f":
            return chance
        # player takes the second chance
        elif chance == "s":
            return chance
        else:
            return "Invalid input or No input in Chance Box"

variable1 = 0
counter = True
def start2(a,b):
    xyz = []
    last = 0
    chance = a
    while True:  
        # player takes the first chance
        if chance == "f":
            while True:
                if last == 20:
                    # return "You Lose"
                    lose1()
                else:
                    j=1
  
                    print ("You are going first and now enter the values")
                    tempf = b.split(' ')
                    # print(temp)
                    for k in range(0, len(tempf)):
                        xyz.append(int(tempf[k]))

                    comp = 4 - len(tempf)
                    # store the last element of xyz.
                    last = xyz[-1] 
                      
                    # checks whether the input 
                    # numbers are consecutive
                    if check(xyz) == True:
                        if last >= 21:
                            # return "You Lose"
                            lose1()
                        
                        else:
                            #"Computer's turn."
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print ("Order of inputs after computer's turn is: ")
                            # print (xyz)
                            last = xyz[-1]
                            if last == 20:
                                lose1()
                            return xyz
                    else:
                        print ("\nYou did not input consecutive integers.")
                        return "You Lose"
                        lose1()
                          
        # player takes the second chance
        elif chance == "s":
            global counter
            while counter:
                random_number = random.randint(1,3)
                for i in range(random_number):
                    xyz.append(i+1)
                last = xyz[-1]
                counter = False
                return xyz
            comp = 1
            while True:
                if last >= 21:
                    win1()
                if last == 20:
                    return "You Win!"
                    win1()
                else:
                    j=1
  
                    print ("You are going second and now enter the values")
                    tempf = b.split(' ')
                    # print(temp)
                    for k in range(0, len(tempf)):
                        xyz.append(int(tempf[k]))

                    comp = 4 - len(tempf)
                    # store the last element of xyz.
                    last = xyz[-1] 

                    # checks whether the input 
                    # numbers are consecutive
                    if check(xyz) == True:
                        if last >= 20:
                            # return "You Lose"
                            win1()
                        
                        else:
                            #"Computer's turn."
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print ("Order of inputs after computer's turn is: ")
                            # print (xyz)
                            last = xyz[-1]
                            if last >= 21:
                                win1()
                            return xyz
                    else:
                        print ("\nYou did not input consecutive integers.")
                        return "You Win"
                        lose1()

                # if variable1 == 0:
                #     variable1 = variable1 + 1
                #     return xyz
            print ("\n\nCONGRATULATIONS !!!")
            print ("YOU WON !")
            exit(0)

'''
# returns the nearest multiple to 4
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near
  
def lose1():
    print ("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)
      
# checks whether the numbers are consecutive
def check(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True
  
# starts the game
def start1(a):
    xyz = []
    last = 0
    while True:
        print ("Enter 'f' to take the first chance.")
        print("Enter 's' to take the second chance.")
        chance = a
          
        # player takes the first chance
        if chance == "f":
            while True:
                if last == 20:
                    lose1()
                else:
                    # print ("\nYour Turn.")
                    # print ("\nHow many numbers do you wish to enter?")
                    # inp = int(input('> '))
                      
                    # if inp > 0 and inp <= 3:
                    #     comp = 4 - inp
                    # else:
                    #     print ("Wrong input. You are disqualified from the game.")
                    #     lose1()
              
                    # i, j = 1, 1
                    j=1
  
                    print ("You are going first and now enter the values")
                    tempf = input().split(' ')
                    # print(temp)
                    for k in range(0, len(tempf)):
                        xyz.append(int(tempf[k]))

                    comp = 4 - len(tempf)
                    # store the last element of xyz.
                    last = xyz[-1] 
                      
                    # checks whether the input 
                    # numbers are consecutive
                    if check(xyz) == True: 
                        if last == 21:
                            lose1()
                              
                        else:
                            #"Computer's turn."
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print ("Order of inputs after computer's turn is: ")
                            print (xyz)
                            last = xyz[-1]
                    else:
                        print ("\nYou did not input consecutive integers.")
                        lose1()
                          
        # player takes the second chance
        elif chance == "s":
            comp = 1
            last = 0
            while last < 20:
                #"Computer's turn"
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print ("Order of inputs after computer's turn is:")
                print (xyz)
                if xyz[-1] == 20:
                    lose1()
                      
                else:
                    print ("\nYour turn.")
                    # print ("\nHow many numbers do you wish to enter?")
                    # inp = input('> ')
                    # inp = int(inp)

                    print ("Enter your values")
                    
                    temps = input().split(' ')
                    # print(temp)
                    for k in range(0, len(temps)):
                        xyz.append(int(temps[k]))

                    last = xyz[-1]
                    if check(xyz) == True:
                        # print (xyz)
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        # if inputs are not consecutive
                        # automatically disqualified
                        print ("\nYou did not input consecutive integers.")
                        # print ("You are disqualified from the game.")
                        lose1()
            print ("\n\nCONGRATULATIONS !!!")
            print ("YOU WON !")
            exit(0)
              
        else:
            print ("wrong choice")
                          
          
game = True    
while game == True:
        print ("Player 2 is Dwight.")
        print("Get ready to play the game")
        start1()
        
        # ans = input('> ')
        # if ans =='Yes':
        #     start1()
        # else:
        #     print ("Do you want quit the game?(yes / no)")
        #     nex = input('> ')
        #     if nex == "yes":
        #         print ("You are quitting the game...")
        #         exit(0)
        #     elif nex == "no":
        #         print ("Continuing...")
        #     else:
        #         print ("Wrong choice")
'''