import random
import string


def random_string(length=8, characters=None):
    if characters is None:
        characters = list(string.ascii_letters + string.digits)
    result = []
    for i in range(length):
        result.append(random.choice(characters))

    random.shuffle(result)
    return result

def generate_password(length=16, symbols=True):
    return random_string(length, None if symbols else list(string.ascii_letters + string.digits + "!@#$%^&*()"))
