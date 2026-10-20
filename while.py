password = input("Enter the password: ").format()
secret = "verysecret"
while password != secret:
    print("Incorrect password. Try again.")
    password = input("Enter the password: ").format()
print("Access granted.")