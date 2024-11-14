#This is a password generator using random characters.
#This may not be 100% safe, as it uses python random library and it saves the passwords in plain text
#But, still, i wanted to practice some coding.

#https://github.com/brnomt

import random
import string

# Pedir al usuario el número de caracteres
num = int(input("Number of characters in password: "))

#This function will ask the user which types of characters they want in their password.
def sel_charas():
    chars = []
    print("Select the types of characters you want in your password (you can combine options).")
    print("1.- Letters \n2.- Numbers \n3.- Symbols")
    
    options = input("Enter the options as a comma-separated list (e.g., 1,2): ")
    options = options.split(",")  # Dividir la entrada en una lista de opciones
    
    for opt in options:
        if opt.strip() == '1':
            chars.append(random_char)
        elif opt.strip() == '2':
            chars.append(random_num)
        elif opt.strip() == '3':
            chars.append(random_sym)
    
    return chars

#If the user select letters, this function will be called
def random_char():
    c = random.choice(string.ascii_letters)
    return c

#If the user select numbers, this function will be called
def random_num():
    n = random.choice(string.digits)
    return n

#If the user select symbols, this function will be called
def random_sym():
    symlist = ['$','@','#','&']
    s = random.choice(symlist)
    return s

#This function will generate the password,
#using the amount of characters the user wants and the characters the user selected

def generate_password(num_chars, char_functions):
    password = []
    for _ in range(num_chars):
        char_func = random.choice(char_functions)  # Elegir aleatoriamente una función de carácter
        password.append(char_func())               # Llamar a la función para obtener el carácter
    return ''.join(password)

selected_functions = sel_charas()
if selected_functions:
    passwd = generate_password(num, selected_functions)
    print(passwd)
else:
    print("No valid character types selected.")
# Imprimir la contraseña generada

#This function will ask the user if the password should be saved
def save_pass():
    opc = input("Want to save the password? [Y/N]: ")
    if opc.lower() == "y":
        with open("saved_passwords.txt", "a") as f:
            f.write(passwd + '\n')
        print("Password Saved!")
        print("NOTE: PASSWORDS ARE SAVED IN PLAIN TEXT")

save_pass()