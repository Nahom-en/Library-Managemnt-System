#creating login and sign up page

userstrack = 1
credentials = {userstrack: {'firstname': 1, 'lastname': 1, 'username': 1, 'password': 1}}

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
            credentials[userstrack] = {'firstname': 1, 'lastname': 1, 'username': 1, 'password': 1}
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
            credentials[userstrack] = {'firstname': 1, 'lastname': 1, 'username': 1, 'password': 1}
        credentials[userstrack]['lastname'] = lnask

    print(f"User {userstrack}:")
    print(f"First Name: {credentials[userstrack]['firstname']}")
    print(f"Last Name: {credentials[userstrack]['lastname']}")

    

def login():
    ask = input("Enter Your ID: ").lower()
    while fnask != str:
        fnask = str(input("Please insert proper characters.\nWhat is your First Name: ")).lower()

def home():
    ask = int(input("WELCOME TO LIBRARY.\n1)To Register.\n2)To Login.\n"))
    while ask!=1 and ask!=2:
        ask = int(input("Invalid Selection.\n1)To Register.\n2)To Login.\n"))
    if ask ==1:
        signup()
    elif ask == 2:
        login()
home()
