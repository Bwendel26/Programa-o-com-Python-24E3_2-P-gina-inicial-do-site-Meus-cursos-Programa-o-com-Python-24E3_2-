import random

secreto = random.randint(1, 100)
palpite = int(input("Adivinhe o número entre 1 e 100: "))
if palpite == secreto:
    print("Você acertou!")
elif palpite < secreto:
    print("Muito baixo!")
else:
    print("Muito alto!")
