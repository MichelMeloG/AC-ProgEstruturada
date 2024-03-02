a = float(input("qual o valor do parametro a da equação: "))
b = float(input("qual o valor do parametro b da equação: "))
c = float(input("qual o valor do parametro c da equação: "))

delta = (b ** 2 - 4 * a * c)

x1 = ((-b) + delta ** (1 / 2)) / (2 * a)
x2 = ((-b) - delta ** (1 / 2)) / (2 * a)

print(f'A primeira raiz da equação é: {x1}')
print(f'A segunda raiz da equação é: {x2}')
