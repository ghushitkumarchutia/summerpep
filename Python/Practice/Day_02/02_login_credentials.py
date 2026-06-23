# Python program to login credentials

username = input("Enter your username: ")
password = input("Enter your password: ")

db_users = {
    "User1": "pass1#123",
    "User2": "pass2#123",
    "User3": "pass3#123",
    "User4": "pass4#123",
    "User5": "pass5#123"
}

if type(username) == str and type(password) == str:
    if username in db_users:
        if len(password) >= 8:
            if db_users[username] == password:
                print("Login Successful")
            else:
                print("Invalid credientials!!!")
        else:
            print("Password must be atleast 8 char long!!!")
    else:
        print("User not found!!!")
else:
    print("Username and password must be strings!!!")