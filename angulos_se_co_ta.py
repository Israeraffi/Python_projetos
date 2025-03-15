import math

while True:

    angulo = input("Digite o valor do angulo: ")
    angulo = angulo.replace("," , ".")

    if "." in angulo:
        angulo = float(angulo)
    else:
        angulo = int(angulo)

    print("\n1 - Seno\n2- Cosseno\n3 - Tangente\n4 - Sair")
    pergunta = int(input("\nDigite o número de sua opção: "))

    if pergunta == 1:
        seno = math.sin(math.radians(angulo))
        seno = round(seno, 2)
        print(f"O seno de {angulo} é: {seno}\n")

    elif pergunta == 2:
        cosseno = math.cos(math.radians(angulo))
        cosseno = round(cosseno, 2)
        print(f"O cosseno de {angulo} é: {cosseno}\n")

    elif pergunta == 3:
        tangente = math.tan(math.radians(angulo))
        tangente = round(tangente, 2)
        print(f"Atangente de {angulo} é: {tangente}\n")

    elif pergunta == 4:
        break
    
    while pergunta != 1 and pergunta != 2 and pergunta != 3 and pergunta != 4:
        print("\nDigite um dos números acima!")

        print("\n1 - Seno\n2- Cosseno\n3 - Tangente\n4 - Sair")
        pergunta = int(input("\nDigite o número de sua opção: "))

        if pergunta == 1:
            seno = math.sin(math.radians(angulo))
            seno = round(seno, 2)
            print(f"O seno de {angulo} é: {seno}\n")
            
        elif pergunta == 2:
            cosseno = math.cos(math.radians(angulo))
            cosseno = round(cosseno, 2)
            print(f"O cosseno de {angulo} é: {cosseno}\n")
            
        elif pergunta == 3:
            tangente = math.tan(math.radians(angulo))
            tangente = round(tangente, 2)
            print(f"Atangente de {angulo} é: {tangente}\n")
            
        elif pergunta == 4:
            break
