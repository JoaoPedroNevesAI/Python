n=input("Digite seu número e expoente: ").split()
def funcao():
    potencia = 1
    for i in range(0, int(n[1])):
        potencia=potencia*int(n[0])
    return print(potencia)
funcao()