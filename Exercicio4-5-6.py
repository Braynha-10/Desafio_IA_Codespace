
while True:
  print("Selecione a operação desejada:")
  print("4. exercicio4")
  print("5. exercicio5")
  print("6. exercicio6")
  print("7. Sair")

  escolha = input("Digite sua escolha: ")

  if escolha in ('4', '5', '6', '7'):
    if escolha == '4':
        numero = int(input("Digite um número: "))

        if numero % 2 == 0:
            print(f"{numero} é par.")
        else:
            print(f"{numero} é ímpar.")

    elif escolha == '5':
        n = int(input("Digite o número de números: "))
        soma = 0

        for i in range(n):
            numero = float(input(f"Digite o {i+1}º número: "))
            soma += numero

        media = soma / n
        print(f"A média dos números é: {media}")


    elif escolha == '6':
        palavra = input("Digite uma palavra: ")
        palavra_invertida = palavra[::-1]

        if palavra == palavra_invertida:
            print(f"{palavra} é um palíndromo.")
        else:
            print(f"{palavra} não é um palíndromo.")


    elif escolha == '7':
        break
  else:
    print("Opção inválida. Por favor, digite um número entre 1 e 5.")