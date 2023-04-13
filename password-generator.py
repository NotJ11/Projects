import random
import string           

charact = list( string.ascii_letters + string.digits + string.punctuation)

def generate_password():

    # Password length
    l = int(input(f"Password's length:  "))

    # Shuffling
    random.shuffle(charact)

    password = []
    for n in range(l):
        password.append(charact[n])
    
    #Converting it to string
    print('Password: ' + ''.join(password))
    
generate_password()

