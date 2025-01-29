s=str(input("Digite uma palavra: "))
min=int(input("Digite um número mínimo: "))
max=int(input("Digite um número máximo: "))
def string(s, min, max):
    tamanho=len(s)
    return min<=tamanho<=max
print(string(s,min,max))