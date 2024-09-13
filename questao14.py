votos = {'Opção 1': 0, 'Opção 2': 0, 'Opção 3': 0}

for _ in range(3):
    voto = input("Vote em 'Opção 1', 'Opção 2' ou 'Opção 3': ")
    if voto in votos:
        votos[voto] += 1

print("Resultados dos votos:")
for opcao, quantidade in votos.items():
    print(f"{opcao}: {quantidade} voto(s)")