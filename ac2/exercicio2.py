def calcula_salario(valor_hora, num_horas, irpf):
    salario_bruto = valor_hora * num_horas
    imposto = salario_bruto * irpf
    salario_liq = salario_bruto - imposto
    return salario_liq


def main():

    salario = calcula_salario(15, 160, 0.275)
    print(f"O Salário líquido: {salario}")

main()