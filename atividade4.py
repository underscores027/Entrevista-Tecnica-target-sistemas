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
                return {}
            return dados['faturamento']
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{json_file}' está vazio ou não é um JSON válido.")
        return {}
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return {}

def calcular_percentuais(faturamentos):
    """Calcula o percentual de representação de cada estado no faturamento total."""
    total = sum(faturamentos.values())
    
    if total == 0:
        print("Erro: O total de faturamento é zero, não é possível calcular percentuais.")
        return {}

    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamentos.items()}
    return percentuais

def main():
    faturamentos = carregar_dados('JSON/faturamento_regiao.json')

    if faturamentos:
        percentuais = calcular_percentuais(faturamentos)

        print("Percentuais de faturamento por estado:")
        for estado, percentual in percentuais.items():
            print(f"{estado}: {percentual:.2f}%")
    else:
        print("Nenhum faturamento disponível para calcular percentuais.")

if __name__ == "__main__":
    main()