import random
import string


def generate_passwoed():
    length=int(input("enter the desired password length: ").strip())
    include_uppercase=input("include uppercase letter? (yes/no): " ).strip().lower()
    include_special=input("include spercial character? (yes/no): " ).strip().lower()
    include_digit=input("include digit? (yes/no): " ).strip().lower()

    if length <4:
        print("the lenngth at least 4 character")
        return
    lowercase=string.ascii_lowercase
    uppercase =string.ascii_uppercase if include_uppercase=="yes" else ""
    special=string.punctuation if include_special=="yes" else ""
    digits=string.digits if include_digit=="yes" else ""

    all_character=uppercase + lowercase +special+digits

    required_characters = []
    if include_uppercase=="yes":
        required_characters.append(random.choice(uppercase))
    if include_special=="yes":
        required_characters.append(random.choice(special))
    if digits=="yes":
        required_characters.append(random.choice(digits))

    remaining_length=length - len(required_characters)

    password=required_characters
    for _ in range(remaining_length):
        chararcter = random.choice(all_character)
        password.append(chararcter)
    random.shuffle(password)

    str_password ="".join(password)
    return str_password
    


password = generate_passwoed()
print(password)










    




