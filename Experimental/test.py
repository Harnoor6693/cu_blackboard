choice = 'n'
username = ""
password = ""
while(choice!='y'):
    choice = str(input("Continue with same login details(y/n): ")).lower().strip()
    if choice:
        choice=choice[0]
        if choice=='n':
            while( (len(username)<=0) and (len(password)<=0)):
                username = input("Enter username:")
                password = input("Enter Passowrd: ")
        elif ((choice!='y') and (choice!='n')):
            print("Enter a valid choice !!! (y/n) ")
    else:
        print("Enter a valid choice !!! (y/n) ")
        choice = 'n'

print(f"username:{username}  password:{password}")