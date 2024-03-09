def eq_seg_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 1 / 2) / (2 * a)
    x2 = (-b - delta ** 1 / 2) / (2 * a)
    return x1, x2


def bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def main():
    print(eq_seg_grau(1, -6, 8))
    print(bissexto(1900))
    print(bissexto(2000))

main()