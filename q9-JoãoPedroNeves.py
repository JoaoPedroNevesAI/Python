ent=input().split()
temp=[]
meses=["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", 
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
for e in ent:
    temp.append(int(e))
maior=max(temp)
menor=min(temp)
for i in range(len(temp)):
    if maior==temp[i]:
        mes=meses[i]
        break  
for i in range(len(temp)):
    if menor==temp[i]:
        mes2=meses[i]
        break  
print(f"MAIOR: {maior}°C em {mes}")
print(f"MENOR: {menor}°C em {mes2}")