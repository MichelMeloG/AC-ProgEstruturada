import random


def main():

    vida_a = 100
    atq_a = random.randint(10, 20)
    defesa = random.randint(1, 5)
    vida_m = random.randint(60, 80)
    atq_m = random.randint(20, 30)


    print(f"Aventureiro: {vida_a} - att {atq_a} - defesa {defesa}")
    print(f"Monstro: vida {vida_m} - att {atq_m}")

    rodada = 1


    while vida_a > 0 or vida_m > 0:
        print(f"rodada: {rodada}")

        dano_av = random.randint(1, atq_a)
        
        
        vida_m = vida_m - dano_av

        dano_m = random.randint(1, atq_m) - defesa
        if dano_m < 0:
            dano_m = 0 

        vida_a = vida_a - dano_m
            
        if vida_m <= 0:
            print("monstro morreu")
            break

        elif vida_a <= 0:
            print("O aventureiro foi morto")
            break            

        else:
            print(f"Aventureiro: {vida_a} - att {atq_a} - defesa {defesa}")
            print(f"Monstro: vida {vida_m} - att {atq_m}")

        rodada += 1
        
    
main()
