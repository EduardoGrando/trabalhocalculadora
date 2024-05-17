#Faca uma calculadora no estilo hp

#Deveremos socilitar ao usuario informar as opcoes disponiveis para o usuario para obter resultado, atraves de um loop whilw
#Seguido de print com as opcoes disponiveis

while True:
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")

    #Neste momento colocaremos uma entrada de dados para que o usuario escolha a opcao desejaada 
    
    opcao = input("Digite a opção desejada: ")
    
    #Se a opcao for ==X, deveremos parar a operacao e encerramos a calculadora pois determinada funcao esta situada para encerrar a operacao
    #Caso a mesma seja situada pelo usuario

    if opcao == 'X':
        print("Saindo da calculadora...")
        break
    
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida. Tente novamente.")
        continue
    
    numeros = []
    
    while True:
        valor = input("Digite um valor numérico (ou 'P' para parar): ")
        if valor == 'P':
            break
        try:
            numero = float(valor)
            numeros.append(numero)
        except ValueError:
            print("Valor inválido. Tente novamente.")
    
    if not numeros:
        print("Nenhum número foi informado. Tente novamente.")
        continue
    
    resultado = numeros[0]
    
    for i in range(1, len(numeros)):
        if opcao == '1':
            resultado += numeros[i]
        elif opcao == '2':
            resultado -= numeros[i]
        elif opcao == '3':
            resultado *= numeros[i]
        elif opcao == '4':
            if numeros[i] == 0:
                print("Erro: Divisão por zero. Operação cancelada.")
                resultado = None
                break
            resultado /= numeros[i]
    
    if resultado is not None:
        operacao = {
            '1': 'adição',
            '2': 'subtração',
            '3': 'multiplicação',
            '4': 'divisão'
        }[opcao]
        print(f"Resultado da {operacao}: {resultado}")
    
    print()