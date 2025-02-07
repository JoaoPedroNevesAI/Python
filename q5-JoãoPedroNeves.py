#Calcular a idade canina:
ic=int(input("Digite a idade de seu canino: "))
if ic<3:
    ih=ic*21
    print(f"A idade do seu cão equivalente à de um ser humano é: {ih}")
elif ic<5:
    ih=42+ic//2*5
    print(f"A idade do seu cão equivalente à de um ser humano é: {ih}")
elif ic<8:
    ih=42+ic//2*3
    print(f"A idade do seu cão equivalente à de um ser humano é: {ih}")
else:
    ih=ic*2
    print(f"A idade do seu cão equivalente à de um ser humano é: {ih}")