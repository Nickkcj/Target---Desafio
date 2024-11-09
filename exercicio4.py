faturamento_mensal_por_distribuidora = {'SP': '67.836,43', 'RJ': '36.678,66', 'MG': '29.229,88', 'ES': '27.165,48', 'Outros': '19.849,53'}

#Como colocamos os valores das chaves do dicionario como strings, teremos que converter
def converter_valor(valor):
    return float(valor.replace('.', '').replace(',', '.'))

total = sum(converter_valor(valor) for valor in faturamento_mensal_por_distribuidora.values())

#Imprimir a porcentagem por estado
print("Percentual de representação do faturamento por estado:")
for estado, valor_str in faturamento_mensal_por_distribuidora.items():
    valor = converter_valor(valor_str)
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")



