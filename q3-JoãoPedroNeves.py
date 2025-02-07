#Código do estado e dizer qual é:
print("Olá! Por favor, digite o código referido à capital desejado:")
codigo=int(input())
match codigo:
    case 71:
        print("O estado com esse código é Salvador.")
    case 79:
        print("O estado com esse código é Acaraju.")
    case 81:
        print("O estado com esse código é Recife.")
    case 82:
        print("O estado com esse código é Maceió.")
    case 83:
        print("O estado com esse código é João Pessoa.")
    case 84:
        print("O estado com esse código é Natal.")
    case 86:
        print("O estado com esse código é Teresina.")
    case 88:
        print("O estado com esse código é Fortaleza.")
    case 98:
        print("O estado com esse código é São Luís")
    case default:
        print("ERRO")