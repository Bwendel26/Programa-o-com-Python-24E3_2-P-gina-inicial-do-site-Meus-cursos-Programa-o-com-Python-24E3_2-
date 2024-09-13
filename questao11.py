import random

n_dados = int(input("Quantos dados você quer lançar? "))
resultados = [random.randint(1, 6) for _ in range(n_dados)]
print("Resultados dos dados:", resultados)
