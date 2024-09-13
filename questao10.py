import random

personagens = ["um cavaleiro", "uma princesa", "um dragão"]
acoes = ["encontrou um tesouro", "lutou contra um monstro", "descobriu um segredo"]
locais = ["em uma caverna", "na floresta encantada", "em um castelo"]

historia = f"{random.choice(personagens)} {random.choice(acoes)} {random.choice(locais)}."
print(historia)
