def dia_semana(numero):
    if numero == 1:
        return "domingo"
    elif numero == 2:
        return "segunda"
    elif numero == 3:
        return "terça"
    elif numero == 4:
        return "quarta"
    elif numero == 5:
        return "quinta"
    elif numero == 6:
        return "sexta"
    elif numero == 7:
        return "sábado"
    else:
        return ""

def testa_dia_semana():
    print(dia_semana(1))
    print(dia_semana(2))
    print(dia_semana(3))
    print(dia_semana(4))
    print(dia_semana(5))
    print(dia_semana(6))
    print(dia_semana(7))

def main():
    testa_dia_semana()

main()
