while True:
  print("Selecione a operação desejada:")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("5. Sair")

  escolha = input("Digite sua escolha (1/2/3/4/5): ")

  if escolha in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
    except ValueError:
      print("Entrada inválida. Por favor, digite números.")
      continue

    if escolha == '1':
      resultado = num1 + num2
      print(num1, "+", num2, "=", resultado)

    elif escolha == '2':
      resultado = num1 - num2
      print(num1, "-", num2, "=", resultado)

    elif escolha == '3':
      resultado = num1 * num2
      print(num1, "*", num2, "=", resultado)

    elif escolha == '4':
      if num2 == 0:
        print("Divisão por zero não é permitida!")
      else:
        resultado = num1 / num2
        print(num1, "/", num2, "=", resultado)

  elif escolha == '5':
    break
  else:
    print("Opção inválida. Por favor, digite um número entre 1 e 5.")
