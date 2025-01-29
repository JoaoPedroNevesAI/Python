nums=input().split()
eh_primo=False
primos=[]
for i in range(0,len(nums)):
    item=int(nums[i])
    for x in range(2,item):
        if (item%x)==0:
            eh_primo=False
            break
        else:
             eh_primo=True
    if eh_primo==True:
            primos.append(f"{item} {i}")
if primos==[]:
     print("-1 -1")
else:
    for item in primos:
        print(item)