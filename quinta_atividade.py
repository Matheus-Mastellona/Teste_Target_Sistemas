# String a ser invertida (pode ser modificada ou recebida como entrada)
string_original = input("Digite uma string para ser invertida: ")

# Inicializando a string invertida
string_invertida = ""

# Invertendo a string manualmente
for caractere in string_original:
    string_invertida = caractere + string_invertida  # Adiciona o caractere no início da string invertida

# Exibindo o resultado
print(f"String invertida: {string_invertida}")