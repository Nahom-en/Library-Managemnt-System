#creating login and sign up page

userstrack = 1
credentials = {userstrack: {'firstname': 1, 'lastname': 1, 'password': 1}}

def signup():
    global userstrack
    global credentials

    fnask = input("SIGNUP\nWhat is your First Name: ").lower()
    while not fnask.isalpha():  # Ensure input contains only letters
        fnask = input("Please insert proper characters.\nWhat is your First Name: ").lower()

    if credentials[userstrack]['firstname'] == 1:
        credentials[userstrack]['firstname'] = fnask
    else:
        userstrack += 1
        # Initialize the new userstrack entry if not already initialized
        if userstrack not in credentials:
            credentials[userstrack] = {'firstname': 1, 'lastname': 1, 'password': 1}
        credentials[userstrack]['firstname'] = fnask

    lnask = input("What is your Last Name: ").lower()
    while not lnask.isalpha():  # Ensure input contains only letters
        lnask = input("Please insert proper characters.\nWhat is your Last Name: ").lower()

    if credentials[userstrack]['lastname'] == 1:
        credentials[userstrack]['lastname'] = lnask
    else:
        userstrack += 1
        # Initialize the new userstrack entry if not already initialized
        if userstrack not in credentials:
            credentials[userstrack] = {'firstname': 1, 'lastname': 1, 'password': 1}
        credentials[userstrack]['lastname'] = lnask

    pwd = input("Enter password: ")
    cpwd = input("Re-Enter the password you entered: ")
    while pwd != cpwd:
        pwd = input("Enter password: ")
        cpwd = input("Re-Enter the password you entered: ")
    credentials[userstrack]['password'] = pwd
    print("Account Created Sucessfully.\nLogging in to Your Account.")
    print(f"Your Id is:{userstrack}\nYour Password: {credentials[userstrack]['password']}")

def login():
    ask = int(input("Enter Your ID: "))
    while ask not in credentials:
        ask = str(input("User not found.\nEnter Your ID: "))
    ask = int(input("Enter Your Password: "))
    while ask != credentials[ask]['password']:
        ask = str(input("Incorrect password.\nEnter Your Password: "))
    int(input("LOGIN SUCESSFUL\nWhat Service you want to use?\n1-To see available books\n2- To borrow books\n3- To return books"))

def home():
    ask = int(input("WELCOME TO LIBRARY.\n1)To Register.\n2)To Login.\n"))
    while ask!=1 and ask!=2:
        ask = int(input("Invalid Selection.\n1)To Register.\n2)To Login.\n"))
    if ask ==1:
        signup()
    elif ask == 2:
        login()

def borrow():
    pass
home()
