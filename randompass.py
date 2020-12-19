import random

name = input(str)
password = (
    random.choice(name)
    + random.choice(name)
    + random.choice(name)
    + str(random.randint(1000, 9999))
)
print(password.lower())
