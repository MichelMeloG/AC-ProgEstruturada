def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (soma, subtraçao, multiplicaçao, divisao): ")

    if operacao == 'soma':
        print("Resultado:", soma(num1, num2))
    elif operacao == 'subtraçao':
        print("Resultado:", subtracao(num1, num2))
    elif operacao == 'multiplicaçao':
        print("Resultado:", multiplicacao(num1, num2))
    elif operacao == 'divisao':
        print("Resultado:", divisao(num1, num2))
    else:
        print("Operação inválida")

def main():
    calculadora()

main()
