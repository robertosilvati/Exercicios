import time
import sys

def menu_selecao():
    print(" ")
    print("Menu de seleção, por favor escolha umas das opções abaixo")
    print("1 = Par ou Impar?")
    print("2 = Fazer uma soma")
    print("3 = Fazer uma média de 4 notas: ")
    print("4 = Sair")
    print(" ")

def selecao():
    opcoes_validas = [1, 2, 3, 4]
    while True:
        selecao = int(input("Qual opção você escolhe? "))
        if selecao in opcoes_validas:
            if selecao == 1:
                escolha_um_numero()
            elif selecao == 2:
                soma()
            elif selecao == 3:
                media()
            elif selecao == 4:
                parar_aplicacao()
            break
        else:
            print("Opção inválida. Você só pode escolher as opções acima.")
            print("Retornando ao menu de seleção..\n")
            tempo_espera()
            menu_selecao()

def saudacao():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Olá mundo, meu nome é Roberto")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def escolha_um_numero():
    escolha = int(input("coloque um numero =>> "))
    tempo_espera()
    if escolha % 2 == 0:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"O seu número escolhido {escolha} é par.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    else:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"O seu número escolhido {escolha} é ímpar.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    menu_selecao()
    selecao()

def soma():
    print("Parece que vamos brincar um pouco, vamos fazer a soma de dois numeros.")
    x = float(input("Coloque o primeiro numero aqui =>>  "))
    y = float(input("Coloque o segundo numero aqui =>>  "))
    resultado = x + y
    tempo_espera()
    print("")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"A soma de {x} + {y} é igual a {resultado}")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("")
    menu_selecao()
    selecao()

def media():
    print("")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Aqui vamos fazer uma média de 4 notas")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("")
    nota1 = float(input("Coloque a nota 1 aqui =>>  "))
    nota2 = float(input("Coloque a nota 2 aqui =>>  "))
    nota3 = float(input("Coloque a nota 3 aqui =>>  "))
    nota4 = float(input("Coloque a nota 4 aqui =>>  "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    tempo_espera()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f"O resultado das média é de =>> {media}")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    menu_selecao()
    selecao()

def parar_aplicacao():
    sys.exit()

def start():
    menu_selecao()
    selecao()

def tempo_espera(tempo = 3):
    for i in range(1,tempo + 1):
        if i  == 1:
            print("Processando.")
        elif i == 2:
            print("Processando..")
        elif i == 3:
            print("Processando...")
        time.sleep(1)

if (__name__ == "__main__"):
    start()

