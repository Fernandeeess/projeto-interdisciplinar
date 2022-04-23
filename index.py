print("Sistema de conversação de base decimal para binario, hexadecimal, octal")
print("[1] para binario")
print("[2] para hexadecimal")
print("[3] para octal")
selected = int(input("Selecione uma das opções acima, ex(1,2,3): "))

def decToBin():
    print("decimal/binario")
    valor = int(input("Digite o valor em decimal: "))
    resultado = "" 
    while(valor != 0 or valor < 0):
            resto = valor % 2
            valor = valor // 2
            resultado = resultado + str(resto);      
    # resultado.reverse()
    print(resultado)

def decToHexa():
    valor = int(input("Digite o valor em decimal: "))
    resultado = "" 
    while(valor != 0 or valor < 0):
        resto = valor % 16
        valor = valor // 16
        if(resto > 9 and resto< 16):
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
            
        resultado = resultado + str(resto);
    
    print(resultado[::-1]);

def decToOctal():
    print("teste3")

if (selected == 1):
    decToBin()
elif (selected == 2):
    print("decimal/hexadecimal")
    decToHexa()
elif (selected == 3):
    print("decimal/octodecimal")
    decToOctal()
else:
    print("nenhuma da opções anteriores foram selecionadas")


