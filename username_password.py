user_names = ["Abdul-Malik", "Uthmaan", "Ayyoob", "Justin", "Masimthembe"]
passwords = ["0000", "1234", "5678", "2021", "4321"]

name = input("Enter Username: ")
password = input("Enter Password: ")

n = len(user_names)
p = len(passwords)
found = False

for x in range(n):

    if name == user_names[x] and password == passwords[x]:
        found = True

if found == True:
    print("Access Granted!")

else:
    print("Access Denied!")




