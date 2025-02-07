n=int(input("Insira um número: "))
s=0
while n>0:
    for x in range(1,n+1):
        if n%3==0:
            s=s+1
    n=int(input())
print(s)