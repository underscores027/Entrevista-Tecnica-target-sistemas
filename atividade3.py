import json
import os

def carregar_dados(json_file):
    if not os.path.exists(json_file):
        print(f"Erro: O arquivo '{json_file}' não foi encontrado.")
        return []

    try:
        with open(json_file, 'r') as file:
            dados = json.load(file)
            if 'faturamento' not in dados:
                print("Erro: A chave 'faturamento' não foi encontrada no arquivo JSON.")
                return []
            return dados['faturamento']
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{json_file}' está vazio ou não é um JSON válido.")
        return []
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return []

def calcular_faturamento(faturamento):
    faturamentos_validos = [f for f in faturamento if f['valor'] > 0]
    
    if not faturamentos_validos:  # Se não houver dias com faturamento
        return None, None, None, None, None, 0

    menor_faturamento = min(faturamentos_validos, key=lambda x: x['valor'])
    maior_faturamento = max(faturamentos_validos, key=lambda x: x['valor'])
    
    menor = menor_faturamento['valor']
    maior = maior_faturamento['valor']
    dia_menor = menor_faturamento['dia']
    dia_maior = maior_faturamento['dia']
    
    media = sum(f['valor'] for f in faturamentos_validos) / len(faturamentos_validos)
    dias_acima_media = sum(1 for f in faturamentos_validos if f['valor'] > media)

    return menor, dia_menor, maior, dia_maior, media, dias_acima_media

def main():
    faturamento = carregar_dados('JSON/faturamento_mensal.json')
    menor, dia_menor, maior, dia_maior, media, dias_acima_media = calcular_faturamento(faturamento)

    if menor is not None and maior is not None:
        print(f"Menor faturamento: {menor:.2f} (Dia: {dia_menor})")
        print(f"Maior faturamento: {maior:.2f} (Dia: {dia_maior})")
    else:
        print("Nenhum faturamento registrado.")

    if media is not None:
        print(f"Média de faturamento: {media:.2f}")
    else:
        print("Nenhuma média calculada.")

    print(f"Número de dias acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()