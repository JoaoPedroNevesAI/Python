#Número e seus divisores:
numero=int(input("Olá! Insira um número desejado e será mostrado seus divisores: "))
contador=0
lista=[]
if numero==0 or numero<0:
    print("ERRO")
else:
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            contador=contador+1
            lista.append(divisor)
    print(f"A quantidade de dividores são: {contador}")
    print(lista)