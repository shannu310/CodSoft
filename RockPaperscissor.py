import random as r
userscore=0
systemscore=0
while(True):
    print("Rock Paper Scissor Game")
    userc=int(input("Choose the action: 1.Rock 2.Paper 3.Scissors"))
    sysc=r.randint(1,3)
    if userc==sysc:
        print("Game tied")
        print("User:",userc)
        print("System:",sysc)
    elif userc==1 and sysc==3:
        print("User won!!")
        print("User:",userc)
        print("System:",sysc)
        userscore+=1
    elif userc==1 and sysc==2:
        print("System won!!")
        print("User:",userc)
        print("System:",sysc)
        systemscore+=1
    elif userc==2 and sysc==1:
        print("User won!!")
        print("User:",userc)
        print("System:",sysc)
        userscore+=1
    elif userc==2 and sysc==3:
        print("System won!!")
        print("User:",userc)
        print("System:",sysc)
        systemscore+=1
    elif userc==3 and sysc==1:
        print("System won!!")
        print("User:",userc)
        print("System:",sysc)
        systemscore+=1
    elif userc==3 and sysc==2:
        print("User won!!")
        print("User:",userc)
        print("System:",sysc)
        userscore+=1
    ch=input("Do you to play again? (y/n)")
    if ch.lower()=='n':
        break
    else :
        continue
print("User score:",userscore)
print("System score:",systemscore)
   