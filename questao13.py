texto = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
print("Palíndromo" if texto == texto[::-1] else "Não é um palíndromo")
