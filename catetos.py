import math

cateto_oposto = input("Digite o valor do cateto oposto: ")
cateto_oposto = cateto_oposto.replace( ",", ".")

cateto_adjacente = input("Digite o valor do cateto adjacente: ")
cateto_adjacente = cateto_adjacente.replace(",",".")


if "." in cateto_oposto:
    cateto_oposto = float(cateto_oposto)
else:
    cateto_oposto = int(cateto_oposto)

if "." in cateto_adjacente:
    cateto_adjacente = float(cateto_adjacente)
else:
    cateto_adjacente = int(cateto_adjacente)


hipotenusa = math.sqrt((math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)))
hipotenusa = round(hipotenusa, 2)

print ("\nVamos decobrir o valor da hipotenusa!\n")

print(f"O valor da hipotenusa é: {hipotenusa}")
