# 5) Escreva um programa que inverta os caracteres de um string.
#
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua
# preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

letras = []
lista_invertida = []
var = 'Frases'

for i in var:
    letras.append(i)

for i in range(len(letras)-1,-1,-1):
   lista_invertida.append(letras[i])
print(''.join(lista_invertida))