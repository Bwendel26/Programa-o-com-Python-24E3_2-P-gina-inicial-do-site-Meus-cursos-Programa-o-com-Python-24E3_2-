nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
novo_nome = nome1[:len(nome1)//2] + nome2[len(nome2)//2:]
print(f"Nome criativo: {novo_nome}")
