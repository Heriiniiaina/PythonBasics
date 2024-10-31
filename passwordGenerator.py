import string
import secrets
import random

def contains_upper(password:str) -> bool:
    for char in password:
        if char in string.ascii_uppercase:
            return True
    return False

def contains_symbols(password:str)->bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length:int,uppercase:bool,symbols:bool ):
    p:string = string.ascii_lowercase +  string.digits 
    if uppercase:
        p+=string.ascii_uppercase
    if symbols:
        p+=string.punctuation
    newPassword:str = ""
    for i in range(length):
        newPassword+= p[secrets.randbelow(len(p))]
    return newPassword
if __name__ == '__main__':
    
    for i in range(1,6):
        newPassword = generate_password(length=10,uppercase=False, symbols=True)

        print(f"{i}: {newPassword} (U: {contains_upper(newPassword)}  S: {contains_symbols(newPassword)})")