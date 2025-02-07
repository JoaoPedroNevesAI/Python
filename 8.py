p=float(input("Preço: "))
vm=int(input("Valor mensal: "))
if p<30 or vm<500:
    v=p*1.1
    print(v)
if 30<=p<80 or 500<=vm<1200:
    v=p*1.15
    print(v)
else:
    v=p*0.2
    print(v)