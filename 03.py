dados = {
    1: 31490.7866,
    2: 37277.9400,
    3: 37708.4303,
    4: 0.0000,
    5: 0.0000,
    6: 17934.2269,
    7: 0.0000,
    8: 6965.1262,
    9: 24390.9374,
    10: 14279.6481,
    11: 0.0000,
    12: 0.0000,
    13: 39807.6622,
    14: 27261.6304,
    15: 39775.6434,
    16: 29797.6232,
    17: 17216.5017,
    18: 0.0000,
    19: 0.0000,
    20: 12974.2000,
    21: 28490.9861,
    22: 8748.0937,
    23: 8889.0023,
    24: 17767.5583,
    25: 0.0000,
    26: 0.0000,
    27: 3071.3283,
    28: 48275.2994,
    29: 10299.6761,
    30: 39874.1073
}


faturamentoUteis = [valor for valor in dados.values() if valor > 0]

menorFaturamento = min(faturamentoUteis)

maiorFaturamento = max(faturamentoUteis)

mediaFaturamento = sum(faturamentoUteis) / len(faturamentoUteis)


dias_acima_da_media = sum(1 for valor in faturamentoUteis if valor > mediaFaturamento)


print(f"Menor faturamento no mês : {menorFaturamento}")
print(f"Maior faturamento no mês : {maiorFaturamento}")
print(f"Numero de dias do mês de faturamento superior a média mensal: {dias_acima_da_media}")
