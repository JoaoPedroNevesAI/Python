n=int(input("Digite um valor: "))
def pn(n):
    if n>0:
        return "É positivo!"
    elif n==0:
        return "É 0!"
    else:
        return "É negativo!"
print(pn(n))