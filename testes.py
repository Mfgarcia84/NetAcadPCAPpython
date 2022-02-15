
#Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
#Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

def anoBissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    else:
        return False


resultado = anoBissexto(1987)
print(resultado)