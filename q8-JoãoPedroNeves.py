N=int(input("Digite um número limite: "))
def limite(x):
    soma=0
    for x in range(0,x+1):
        soma=soma+x
    return print(soma)
limite(N)