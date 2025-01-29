a=input("Digite a lista 1: ").split()
b=input("Digite a lista 2: ").split()
c=[]
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        c.append(i)
print(c)