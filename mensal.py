# ) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
#
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do
# valor total mensal da distribuidora.

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

soma = SP + RJ  + MG + ES + Outros
print(f"Valor percentual do faturaento de SP foi {((SP/soma) * 100):.2f}%")
print(f"Valor percentual do faturaento de RJ foi {((RJ/soma) * 100):.2f}%")
print(f"Valor percentual do faturaento de MG foi {((MG/soma) * 100):.2f}%")
print(f"Valor percentual do faturaento de ES foi {((ES/soma) * 100):.2f}%")
print(f"Valor percentual do faturaento de Outros foi {((Outros/soma) * 100):.2f}%")