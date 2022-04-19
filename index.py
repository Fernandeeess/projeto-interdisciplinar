



print("Sistema de conversação de base decimal para binario, hexadecimal, octodecimal")
print("[1] para binario")
print("[2] para hexadecimal")
print("[3] para octodecimal")
selected = int(input("Selecione uma das opções acima, ex(1,2,3): "))

if (selected == 1):
    print("decimal/binario")
    valor = int(input("Digite o valor em decimal: "))
    resultado = []
    while(valor != 0 or valor < 0):
            resto = valor % 2
            valor = valor // 2
            resultado.append(resto)       
    resultado.reverse()
    print(resultado)   
  
elif (selected == 2):
    print("decimal/hexadecimal")
elif (selected == 3):
    print("decimal/octodecimal")
else:
    print("nenhuma da opções anteriores foram selecionadas")


# =def convDecimalToBinarie(valueToConvert):
