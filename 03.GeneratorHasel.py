import random
import string

def password_generator():
    password = ''
    for _ in range(random.randrange(2,5)):
        password += random.choice(string.digits) + random.choice(string.ascii_uppercase) + random.choice(string.punctuation) + random.choice(string.ascii_lowercase)
        list_pass = list(password)
        random.shuffle(list_pass)
        password = "".join(list_pass)
    print(f"Twoje haslo to {password}")

password_generator()

 





