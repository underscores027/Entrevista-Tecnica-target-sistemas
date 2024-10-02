import math

def is_fibonacci_number(numero_fibonacci):
    # Função auxiliar para verificar se um número é um quadrado perfeito
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    
    if numero_fibonacci < 0:
        return False
    
    return (is_perfect_square(5 * numero_fibonacci**2 + 4) or
            is_perfect_square(5 * numero_fibonacci**2 - 4))

def solicitar_inteiro():
    entrada = input("Insira um número inteiro: ")
    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        return int(entrada)
    print("Entrada inválida. Tente novamente.")
    return solicitar_inteiro()


numero_fibonacci = solicitar_inteiro()

if is_fibonacci_number(numero_fibonacci):
    print(f"{numero_fibonacci} é da sequência de Fibonacci.")
else:
    print(f"{numero_fibonacci} não é da sequência de Fibonacci.")
