import string
import random

tamanho = int(input("Digite a quantidade de caracteres da sua senha: "))

print("1- letras maiúsculas, minúsculas, números e caracteres especiais")
print("2- letras maiúsculas, minúsculas e números")
print("3- letras maiúsculas e minúsculas")
print("4- números")



pergunta = input("Digite um dos números acima: \n")

if pergunta == "1":
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    print(f"Sua senha segura é: {senha}")

elif pergunta == "2":
    caracteres = string.ascii_letters + string.digits
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    print(f"Sua senha segura é: {senha}")

elif pergunta == "3":
    caracteres = string.ascii_letters
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    print(f"Sua senha segura é: {senha}")

elif pergunta == "4":
    caracteres = string.digits
    senha = " ".join(random.choice(caracteres) for i in range(tamanho))
    print(f"Sua senha segura é: {senha}")
