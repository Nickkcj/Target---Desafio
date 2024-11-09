import json

#Usando o JSON que vocês providenciaram de exemplo:
with open('C:/Users/NickC/Target - Desafio/Target---Desafio/faturamento.json', 'r') as file:
    dados_json = json.load(file)

#Agora vamos extrair apenas os valores desse JSON e sem pegar os zeros dos finais de semana/feriados
valores = [item['valor'] for item in dados_json if item['valor'] != 0.0]

#Definimos um valor absurdamente alto para substituir ao percorrer a lista
def achar_menor_valor(valores):
    menor_valor = 999999999999999
    for itens in valores:
        if itens < menor_valor:
            menor_valor = itens

##OU menor_valor = min(valores) mas evitarei de usar funcoes prontas

    return menor_valor

#Aqui definimos um valor absurdamente baixo para substituir ao percorrer a lista
def achar_maior_valor(valores):
    maior_valor = -99999999999999
    for itens in valores:
        if itens > maior_valor:
            maior_valor = itens

##OU maior_valor = max(valores) mas evitarei de usar funcoes prontas
            
    return maior_valor

#Aqui calculamos os dias maiores que a media, excluindo os zeros com list comprehension
def n_dias_superior_media(valores):
    valores = [valor for valor in valores if valor != 0]
    n_dias = 0
    media = sum(valores) / len(valores)
    for itens in valores:
        if itens > media:
            n_dias += 1

    return n_dias


menor_valor = achar_menor_valor(valores)
maior_valor = achar_maior_valor(valores)
dias_superior_media = n_dias_superior_media(valores)


print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento superior à média: {dias_superior_media}")


    
