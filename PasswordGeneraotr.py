import random as r
import string as s
choice='y'
sethigh=s.ascii_letters+s.digits+s.punctuation
setlow=s.ascii_letters
setmid=s.ascii_letters+s.digits
while choice=='y':
    length=int(input("Enter the required length of password:"))
    complexity=input("Enter the complexity of password (low/medium/high):")
    if complexity.lower()=='low':
        password=''
        for i in range(0,length):
            password+=r.choice(setlow)
        print("Password generated for low complexity:",password)
        choice=input("Do you want to generate another password? (y/n):")
        if choice.lower()=='n':
            print("Thank you for using Password generator")
            break
        else :
            continue
    elif complexity.lower()=='medium':
        password=''
        for i in range(0,length):
            password+=r.choice(setmid)
        print("Password generated for low complexity:",password)
        choice=input("Do you want to generate another password? (y/n):")
        if choice.lower()=='n':
            print("Thank you for using Password generator")
            break
        else :
            continue
    elif complexity.lower()=='high':
        password='' 
        for i in range(0,length):
            password+=r.choice(sethigh)
        print("Password generated for low complexity:",password)
        choice=input("Do you want to generate another password? (y/n):")
        if choice.lower()=='n':
            print("Thank you for using Password generator")
            break
        else :
            continue
    else:
        print("Select a correct option")
