import re
import collections

receber_txt = input("Digite seu texto: \n ")
palavras = receber_txt.split()

frases = re.split(r"[.!?]", receber_txt)

palavras_frequntes = collections.Counter(palavras)
caracteres= len(receber_txt.replace(" ", ""))

print(f'Seu texto tem {caracteres} caracteres, {len(palavras)} palavras, as seguintes frases: {frases} e as seguintes palavras mais frequentes: {palavras_frequntes.most_common(5)}')
