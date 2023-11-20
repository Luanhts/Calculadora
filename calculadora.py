def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y
while True:
    print("Opcções")
    print("1. adição")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. sair")

    escolha = input("Escolha a operação desejada: ")

    if escolha == '5':
        print("Encerrando a calculadora...")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Escolha inválida. Tente Novamente.")
        continue
    
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if escolha == '1':
        print("Resultado: ", adicao(num1, num2))

    elif escolha == '2':
        print("Resultado: ",subtracao(num1, num2) )
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1,num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1,num2))























