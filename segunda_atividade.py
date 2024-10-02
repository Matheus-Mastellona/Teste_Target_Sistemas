def gerar_fibonacci(quantidade):
    if quantidade <= 0:
        return []
    elif quantidade == 1:
        return [1]
    
    fib = [1, 1]  # Começando a sequência de Fibonacci com os dois primeiros números
    for i in range(2, quantidade):
        proximo_numero = fib[i-1] + fib[i-2]
        fib.append(proximo_numero)
    
    return fib

def fibonate(quantidade):
    fibonacci = gerar_fibonacci(quantidade)
    # Aplicando a transformação desejada (exemplo: multiplicar por 2)
    fibonate_resultado = [num * 2 for num in fibonacci]
    return fibonate_resultado

# Exemplo de uso:
quantidade = 5
resultado_fibonate = fibonate(quantidade)
print(f"Fibonacci transformado (fibonate): {resultado_fibonate}")