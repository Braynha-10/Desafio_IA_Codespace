#Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Pede ao usuário para inserir uma string
string = input("Digite uma string: ")

# Pede ao usuário para inserir um número inteiro
numero_repeticoes = int(input("Digite o número de vezes para repetir a string: "))

# Repete a string o número de vezes especificado
string_repetida = f'{string}-'* numero_repeticoes

# Imprime a string repetida
print(f"String repetida:\n {string_repetida}")

# Usamos input() para solicitar ao usuário que digite uma string e um número inteiro.
# Armazenamos a string na variável string e o número inteiro na variável numero_repeticoes.
# Usamos o operador * para multiplicar a string pelo número inteiro, criando uma nova string que é a string original repetida o número de vezes especificado. Armazenamos essa string repetida na variável string_repetida.
# Finalmente, imprimimos a string repetida