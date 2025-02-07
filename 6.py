c=int(input("Digite o código: "))
s=float(input("Digite o seu salário: "))
match c:
    case 1:
        v=s*1.5
        print(v)
    case 2:
        v=s*1.35
        print(v)
    case 3:
        v=s*1.2
        print(v)
    case 4:
        v=s*1.1
        print(v)
    case 5:
        print("Não tem aumento.")