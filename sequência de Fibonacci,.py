# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
#  escreva um programa na linguagem que desejar onde, informado um número, ele calcule a
#  sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence
#  ou não a sequência.


lista = [0, 1]
escolha = 123


while True:
    soma = lista[-1] + lista[-2]
    lista.append(soma)
    if(soma >= escolha):
        break
print(lista)

if(escolha in lista):
    print("Esse numero esta presente na lista")
else:
    print("Esse numero nao esta presente")

#-------------------------------------------------------#



