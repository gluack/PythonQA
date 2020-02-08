import random

def magic(user, a, b):
    return {user: random.randint(a, b)}

x = str(input("Як тебе звати, Бешкетнику?: "))

print("Магічне число твого імені:",(magic(x, 0, 1000)))
