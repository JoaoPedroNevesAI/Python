#Quantos jogos tal aluno ganhou e qual grupo estará:
j=int(input("Digite quantas partidas você ganhou? "))
match j:
    case 6:
        print("Você está no grupo 1.")
    case 5:
        print("Você está no grupo 1.")
    case 4:
        print("Você está no grupo 2.")
    case 3:
        print("Você está no grupo 2.")
    case 2:
        print("Você está no grupo 3.")
    case 1:
        print("Você está no grupo 3.")
    case 0:
        print("Você está desqualificado.")
    case default:
        print("ERRO")