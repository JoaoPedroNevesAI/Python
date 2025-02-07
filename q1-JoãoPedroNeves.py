#Soma dos números primos:
n=int(input("Digite um número qualquer: "))
p=1
while n>0:
    for x in range(2,n):
        print(x)
        if n%x==0:
            p=0
            if p==1:
                print(f"{n} é primo.")
            else:
                print(f"{n} não é primo.")
        else:
            break