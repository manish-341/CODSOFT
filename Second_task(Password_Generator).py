#PASSWORD GENERATOR
import random,string

def password_generator(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "@#$%&"

    
    characters = lowercase + uppercase + digits + symbols

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    if length < 4:
        print("The length of the password should be 4.")
        return None

    password += random.choices(characters, k=length - 4)
    
    random.shuffle(password)
    return ''.join(password)


try:
    length = int(input("Enter the length of the password: "))
    result = password_generator(length)
    if result:
        print("Generated Password:", result)
except ValueError:
    print("Enter a valid number.")
