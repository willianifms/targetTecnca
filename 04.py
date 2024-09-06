SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

faturamentoTotal = SP + RJ + MG + ES + Outros
print(faturamentoTotal)

sp = (SP / faturamentoTotal) * 100
rj = (RJ / faturamentoTotal) * 100
mg = (MG / faturamentoTotal) * 100
es = (ES / faturamentoTotal) * 100
outros = (Outros / faturamentoTotal) * 100

print(f"faturamento de SP: R${SP} - {sp:.2f}%")
print(f"faturamento de RJ: R${RJ} - {rj:.2f}%")
print(f"faturamento de MG: R${MG} - {mg:.2f}%")
print(f"faturamento de ES: R${ES} - {es:.2f}%")
print(f"faturamento de Outros:{Outros} - R$ {outros:.2f}%")
