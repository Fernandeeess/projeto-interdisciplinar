converter = True;
def continuarOuNao():
    
    continuar = str(input("Se quiser continuar convertendo digite [Y] "))
    if (continuar == "Y" or continuar == "y"):
        converter = True
    else:
        print("valor invalido")


def decToBin():
    print("Decimal/Binario")
    valor = int(input("Digite o valor em decimal: "))
    resultado = ""
    while(valor != 0 or valor < 0):
        resto = valor % 2
        valor = valor // 2
        resultado = resultado + str(resto)
    # resultado.reverse()
    print(resultado[::-1], "Binario")
    continuarOuNao()


def decToHexa():
    print("Decimal/Hexadecimal")
    valor = int(input("Digite o valor em decimal: "))
    resultado = ""
    while(valor != 0 or valor < 0):
        resto = valor % 16
        valor = valor // 16
        if(resto > 9 and resto < 16):
            if resto == 10:
                resto = "A"
            elif resto == 11:
                resto = "B"
            elif resto == 12:
                resto = "C"
            elif resto == 13:
                resto = "D"
            elif resto == 14:
                resto = "E"
            elif resto == 15:
                resto = "F"

        resultado = resultado + str(resto)

    print(resultado[::-1], "Hexadecimal")
    continuarOuNao()


def decToOctal():
    print("Decimal/Octal")
    valor = int(input("Digite o valor em decimal: "))
    resultado = ""
    while(valor != 0 or valor < 0):
        resto = valor % 8
        valor = valor // 8
        resultado = resultado + str(resto)
    # resultado.reverse()
    print(resultado[::-1], "Octal")
    continuarOuNao()


while converter == True:
    print("")
    print("Sistema de conversação de base decimal para binario, hexadecimal, octal")
    print("")
    print("[1] para binario")
    print("")
    print("[2] para hexadecimal")
    print("")
    print("[3] para octal")
    print("")
    selected = int(input("Selecione uma das opções acima, ex(1,2,3): "))

    if (selected == 1):
        decToBin()
    elif (selected == 2):
        decToHexa()
    elif (selected == 3):
        decToOctal()
    else:
        print("nenhuma da opções anteriores foram selecionadas")
