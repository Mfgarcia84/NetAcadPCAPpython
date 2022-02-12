def anoBissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 != 0:
            return False
        elif ano % 100 == 0 and ano % 400 == 0:
            return True
        else:
            return True
    else:
        return False


dadosDeTeste = [1900, 2000, 2016, 1987]
resultadoDosTestes = [False, True, True, False]
for i in range(len(dadosDeTeste)):
    ano = dadosDeTeste[i]
    resultado = anoBissexto(ano)
    print(ano, "-->", end="")
    if resultado == resultadoDosTestes[i]:
        print("OK")
    else:
        print("Falha")







