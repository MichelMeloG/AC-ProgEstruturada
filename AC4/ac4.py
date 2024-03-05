def ler_nome():
    usuario = input("qual o seu nome: ")
    return usuario

def ler_nota():
    ap1 = float(input("Nota da AP1: "))
    ap2 = float(input("Nota da AP2: "))
    asub = float(input("Nota da AS: "))
    ac = float(input("Nota da AC: "))
    return ap1, ap2, asub, ac

def validar_notas(ap1, ap2, asub, ac):
    if ap1 > 10 or ap1 < 0:
        return False
    if ap2 > 10 or ap2 < 0:
        return False
    if asub > 10 or asub < 0:
        return False
    if ac > 10 or ac < 0:
        return False
    return True

def maiores_notas(ap1, ap2, asub):
    if ap1 < asub:
        return ap2, asub
    elif ap2 < asub:
        return ap1, asub
    return ap1, ap2

def calcular_media(n1, n2, ac):
    """
    Calcula e retorna a média do usuário.
    """
    return (n1 + n2) * 0.4 + ac * 0.2

def informar_aprovacao(media):
    """
    Informa se o aluno passou ou não na disciplina.
    """
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabéns, você foi aprovado!")
    else:
        print("Você foi reprovado...")


def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_nota()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)



main()