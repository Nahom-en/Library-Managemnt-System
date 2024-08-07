#creating login and sign up page

userstrack = 1
credentials = {}
books = {1:{"Title":"Power","Author":"David","Price":62},
         2:{"Title":"Atomic Habit","Author":"James Clear","Price":22}}
rentedbooks = {}

def signup():
    global userstrack
    global credentials

    credentials[userstrack] = {}  # Initialize the dictionary entry for the user

    fnask = input("SIGNUP\nWhat is your First Name: ").lower()
    while not fnask.isalpha():  # Ensure input contains only letters
        fnask = input("Please insert proper characters.\nWhat is your First Name: ").lower()
    credentials[userstrack]['firstname'] = fnask

    lnask = input("What is your Last Name: ").lower()
    while not lnask.isalpha():  # Ensure input contains only letters
        lnask = input("Please insert proper characters.\nWhat is your Last Name: ").lower()
    credentials[userstrack]['lastname'] = lnask

    pwd = input("Enter password: ")
    cpwd = input("Re-Enter the password you entered: ")
    while pwd != cpwd:
        pwd = input("Enter password: ")
        cpwd = input("Re-Enter the password you entered: ")
    credentials[userstrack]['password'] = pwd

    print("Account Created Successfully.\nLogging in to Your Account.")
    print(f"Your Id is: {userstrack}\nYour Password: {credentials[userstrack]['password']}")

    userstrack += 1

    login()

def login():
    ask = int(input("Enter Your ID: "))
    while ask not in credentials:
        ask = input("User not found.\nEnter Your ID: ")
    ask2 = int(input("Enter Your Password: "))
    while ask2 != credentials[ask]['password']:
        ask2 = str(input("Incorrect password.\nEnter Your Password: "))
    print(f"Login suceessful\nHello {credentials[ask]['firstname'].title()}")

    loggedin()

def home():
    ask = int(input("WELCOME TO X LIBRARY.\n1)To Register.\n2)To Login.\n"))
    while ask!=1 and ask!=2:
        ask = int(input("Invalid Selection.\n1)To Register.\n2)To Login.\n"))
    if ask ==1:
        signup()
    elif ask == 2:
        login()



def rentbook():
    if not books:
        while True:
            ask = input("All books have been rented\nPress '#' to go back.\n")
            if ask == '#':
                loggedin()
                return
    print("Available Books In Library\n")
    for i in books:
        print(f"Book Id: {i}\nTitle: {books[i]['Title']}\nAuthor: {books[i]['Author']}\nPrice: {books[i]['Price']} ETB\n\n**********\n")
    ask = int(input("Which book do you want to rent? (enter book id): "))
    if ask in books:
        ask2 = float(input("Please Enter the money: "))
        if ask2 == books[ask]['Price']:
            rentedbooks[ask] = books[ask]
            books.pop(ask)
            print("You Have Rented it successfully.")
            loggedin()
        elif ask2 > books[ask]['Price']:
            rentedbooks[ask] = books[ask]
            books.pop(ask)
            print(f"You Have Rented it successfully.\nTake your change\nYour change is {ask2 - rentedbooks[ask]['Price']} ETB")
            loggedin()
        else:
            print("Insufficient balance.")
            loggedin()
    else:
        print("Id not found.")
        loggedin()

def loggedin():
    askl = input("Welcome to X library.\n1) To rent books.\n2) To Return Books\n3) To Check your Books Cart.\n#) To Log out\n")
    while askl not in ['1', '2', '3', '#']:
        askl = input("Please Enter Valid Options.\n1) To rent books.\n2) To Return Books\n3) To Check your Books Cart.\n#) To LogOut\n")
    if askl == '1':
        rentbook()
    elif askl == '2':
        returnbook()
    elif askl == '3':
        cart()
    elif askl == '#':
        home()
        pass

def returnbook():
    if not rentedbooks:
        while True:
            ask = input("No books found.\nPress '#' to go back\n")
            if ask == '#':
                loggedin()
                return
    print("Which book do you want to return?")
    for i in rentedbooks:
        print(f"Book Id: {i}\nTitle: {rentedbooks[i]['Title']}\nAuthor: {rentedbooks[i]['Author']}\n\n**********\n")
    ask = int(input("Enter book Id to return: "))
    if ask in rentedbooks:
        books[ask] = rentedbooks[ask]
        rentedbooks.pop(ask)
        print("\n**********\n\nYou Have Returned it successfully.\n**********\n\n")
        loggedin()
    else:
        print("Id not found")
        loggedin()

def cart():
    if not rentedbooks:
        while True:
            ask = input("You haven't rented any books.\nPress '#' to go back\n")
            if ask == '#':
                loggedin()
                return
    print("You Have Rented\n")
    for i in rentedbooks:
        print(f"Book Id: {i}\nTitle: {rentedbooks[i]['Title']}\nAuthor: {rentedbooks[i]['Author']}\n\n**********\n")
    while True:
        ask = input("\nPress '#' to go back\n")
        if ask == '#':
            loggedin()
            return

        

home()
