#formas obrigatórias:
# 1-círculo
# 2-triângulo
# 3-quadrado
# 4-Retângulo
# 5-Paralelograma
# 6-Losango
# 7-Trápézio

def circulo():
    raio = float(input("Qual é o raio do círculo? "))
    print("A área desse círculo é: ", 3.14 * raio ** 2)

def triângulo():
    base = float(input("Qual é o valor da base? "))
    altura = float(input("Qual é a altura? "))
    print("A área desse Triângulo é ",base * altura /2)

def quadrado():
    lado = float(input("Qual o valor dos lados? "))
    print("A área desse Quadrado é ",lado * lado)

def Retângulo():
    base = float(input("Qual o valor da base? "))
    altura = float(input("Qual a altura? "))
    print("A área desse Retângulo é ",base * altura)

def Paralelograma():
    base = float(input("Qual o valor da base? "))
    altura = float(input("Qual a altura? "))
    print("A área desse Paralelograma é ",base * altura)

def Losango():
    diagonal1 = float(input("Qual é o valor da maior diagonal? "))
    diagonal2 = float(input("Qual é o valor da menor diagonal? "))
    print("A área desse Losango é",diagonal1 * diagonal2 /2)

def trapezio():
    B = float(input("Qual a base maior? "))
    b = float(input("Qual a base menor? "))
    altura = float(input("Qual a altura? "))
    print("A área desse Trápézio é ",(B + b)* altura /2)

while True:
    print ("CALCULADORA")
    print ("1 - círculo")
    print ("2 - triângulo")
    print ("3 - quadrado")
    print ("4 - Retângulo")
    print ("5 - Paralelograma")
    print ("6 - Losango")
    print ("7 - Trápézio")
    print ("0 - Sair")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        circulo()

    elif opcao == "2":
        triângulo()
    elif opcao == "3":
        quadrado()
    elif opcao == "4":
        Retângulo()
    elif opcao == "5":
        Paralelograma()
    elif opcao == "6":
        Losango()
    elif opcao == "7":
        trapezio()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

