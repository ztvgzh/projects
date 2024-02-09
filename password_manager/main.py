from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        # 'wb'-> write  in binary
        key_file.write(key)'''

def load_key():
    file = open('password_manager/key.key', 'rb')
    key = file.read()
    file.close
    return key


key = load_key()
fer = Fernet(key)

def view():
    with open('password_manager/passwords.txt', 'r') as f:
        for line in f.readlines():
            # print(line.rstrip()) -> to show the whole line
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User name: {user}, \nPassword: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    with open('password_manager/passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add) \
                 to quit type 'q': \n").lower()
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue