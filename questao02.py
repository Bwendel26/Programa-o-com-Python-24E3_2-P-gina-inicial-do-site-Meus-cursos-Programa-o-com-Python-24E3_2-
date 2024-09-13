# Solicita os minutos do usuário e converte para horas e minutos
minutos = int(input("Insira a quantidade de minutos: "))
print(f"{minutos} minutos é igual a {minutos // 60} horas e {minutos % 60} minutos.")

# Solicita horas e minutos e converte para minutos totais
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
print(f"{horas} horas e {minutos} minutos equivalem a {horas * 60 + minutos} minutos.")