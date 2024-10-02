import json

def calcular_faturamento():
    # Lendo o arquivo JSON
    with open('faturamento.json') as f:
        dados = json.load(f)

    faturamento_diario = dados['faturamento']
    
    # Extraindo os valores de faturamento, ignorando dias sem faturamento
    valores_faturamento = [valor for valor in faturamento_diario.values() if valor > 0]
    
    if not valores_faturamento:
        print("Não há dias com faturamento.")
        return

    # Cálculo do menor e maior faturamento
    menor_faturamento = min(valores_faturamento)
    maior_faturamento = max(valores_faturamento)

    # Cálculo da média mensal
    media_mensal = sum(valores_faturamento) / len(valores_faturamento)

    # Contar dias com faturamento superior à média mensal
    dias_acima_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

    # Resultados
    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Número de dias acima da média mensal: {dias_acima_media}")

# Chamada da função
calcular_faturamento()