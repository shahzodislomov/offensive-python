# password = input("Enter the password: ").format()
# secret = "verysecret"
# while password != secret:
#     print("Incorrect password. Try again.")
#     password = input("Enter the password: ").format()
# print("Access granted.")

file = open("test.txt", "r")
    
while (line := file.readline()):
    print(line.strip())
