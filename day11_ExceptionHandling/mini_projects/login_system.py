users = {
    "admin": "1234",
    "user": "abcd"
}

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if users[username] == password:
        print("Login successful")
    else:
        print("Wrong password")

except KeyError:
    print("User not found")
