import random
import string
from pathlib import Path

passwords = {}
password_file = Path(__file__).with_name("passwords.txt")

#load existing password file 

try:
    with password_file.open("r") as file:
        for line in file:
            site, pwd = line.strip().split(":", 1)
            passwords[site] = pwd
except FileNotFoundError:
    pass


def save_passwords():
    with password_file.open("w") as file:
        for site, pwd in passwords.items():
            file.write(f"{site}:{pwd}\n")


# generate random password 
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password



while True:
    print("\n-----------PERSONAL PASSWORD MANAGER-----------")
    print("1.Save Password")
    print("2. View Passwords")
    print("3.Generate Password")
    print("4.Update Password")
    print("5. Exit")

# user input
    choice = input("Enter your choice:")

    # save password
    if choice == "1":
        site = input("Enter site name or url: ")
        pwd = input("Enter password: ")

        passwords[site] = pwd
        save_passwords()

        print("Saved!")

    # view password
    elif choice == "2":
        if not passwords:
            print("No data!")    
        else:
            for site,pwd in passwords.items():
                print(site, ":", pwd)

    # Generate Password
    elif choice == "3":
        password = generate_password()
        print("Password: ",password)

    # Update Password
    elif choice == "4":
        site = input("Enter site to update password: ")
        if site in passwords:
            pwd = input("Enter new password : ")
            passwords[site] = pwd
            save_passwords()
            print("Password Updated!")


        else:
            print("Site not found!")

    elif choice == "5":
        print("Exited!")
        break

    