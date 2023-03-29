# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;



import json

f = json.load(open("dados.json"))

def maior():
    valor = None
    for i in f:
        if(valor is None or i['valor'] > valor):
            valor = i['valor']
    return valor

def menor():
    valor = None
    for i in f:
        if(valor is None or i['valor'] < valor):
            valor = i['valor']
    return valor

def media():
    valor = 0
    for i in f:
        valor = i['valor'] + valor
    mediaa  = valor / len(f)

    return mediaa

def dias_do_mes():
    valor  = media()
    dias = 0
    for i in f:
        if(i['valor'] > valor):
            dias = dias + 1
    return dias





print(maior())
print(menor())
print(media())
print(dias_do_mes())
