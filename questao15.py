print("Você está em um castelo antigo.")
escolha = input("Você vê uma porta à esquerda ou uma escada à direita. Para onde você vai? (porta/escada): ")

if escolha == "porta":
    escolha2 = input("Você encontra uma biblioteca ou um laboratório. Onde você entra? (biblioteca/laboratório): ")
    if escolha2 == "biblioteca":
        print("Você descobre um livro antigo que revela um segredo escondido.")
    else:
        print("Você encontra uma poção mágica que lhe concede um poder especial.")
else:
    escolha2 = input("Você encontra um jardim secreto ou uma sala de tesouros. Onde você vai? (jardim/sala de tesouros): ")
    if escolha2 == "jardim":
        print("Você encontra uma flor rara que pode curar qualquer doença.")
    else:
        print("Você encontra um baú cheio de joias e moedas de ouro.")
