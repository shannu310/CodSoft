contact=[]
def addcont(contact):
    name=input("Enter the name of the contact:")
    phnum=int(input("Enter the phone number:"))
    email=input("ENter the email address:")
    address=input("Enter the email address:")
    contact.append([name,phnum,email,address])
def viewcont(contact):
    print("Contacts")
    for i in contact:
        print(i)
def searchcont(contact):
    name=input("Enter the name of the contact:")
    for i in range(0,len(contact)):
        if contact[i][0].lower()==name.lower():
            print("Contact found")
            print(contact[i])
            break
        else:
            print("contact  not found")
def updatecont(contact):
    name=input("Enter the contact name you want to update:")
    for i in range(0,len(contact)):
        if contact[i][0].lower()==name.lower():
            choice=int(input("Select the update option: 1.NAME 2.NUMBER 3.EMAIL 4.ADDRESS:"))
            if choice==1:
                nam=input("Enter the new name:")
                contact[i][0]=nam
                print("After updating the contact...")
                print(contact[i])
                break
            elif choice==2:
                num=int(input("Enter the phone number:"))
                contact[i][1]=num
                print("After updating the contact...")
                print(contact[i])
                break
            elif choice==3:
                emai=input("Enter the new EMAIL:")
                contact[i][2]=emai
                print("After updating the contact...")
                print(contact[i])
                break
            elif choice==4:
                addr=input("Enter the new Address:")
                contact[i][3]=addr
                print("After updating the contact...")
                print(contact[i])
                break
            else:
                print("Choose correct option")
        else:
            print("Contact not found")
            break
def deletecon(contact):
    name=input("Enter the name of the contact to delete")
    for i in range(0,len(contact)):
        if contact[i][0].lower()==name.lower():
            print("Contact deleted...")
            contact.pop(i)
        else:
            print("Contact not found")
            break
while(True):
    choice=int(input("Enter the required operation in contact book...1.Add Contact 2.Print COntacts 3.Search 4.Update 5.Delete"))
    if(choice==1):
        addcont(contact)
    elif choice==2:
        viewcont(contact)
    elif choice==3:
        searchcont(contact)
    elif choice==4:
        updatecont(contact)
    elif choice==5:
        deletecon(contact)
    else:
        print("Select a valid option")
        break
    c=input("Do you want to continue? y/n")
    if c.lower()=='n':
        break
    else:
        continue












    
