def inverter_string(texto):
    if not isinstance(texto, str):
        raise ValueError("O valor deve ser uma string.")

    caracteres_invertidos = []
    for caractere in texto:
        caracteres_invertidos.insert(0, caractere)  # Adiciona cada caractere no início da lista
    return ''.join(caracteres_invertidos)

def obter_string_usuario():
    while True:
        entrada = input("Insira uma string para inverter: ")
        if entrada.strip():  # Verifica se a string não está vazia
            return entrada
        print("Erro: A entrada não pode ser vazia. Tente novamente.")

def main():
    """Função principal do programa."""
    try:
        string_exemplo = obter_string_usuario()
        string_invertida = inverter_string(string_exemplo)
        print(f"String original: {string_exemplo}")
        print(f"String invertida: {string_invertida}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
