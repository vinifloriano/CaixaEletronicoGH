import os
import time

from src.Client import Client
import functions as fun

cliente = Client()

def principal_cli():
    func = fun.functionsADM()
    trigger = 0

    while trigger == 0:
        login = func.open()
        
        if login == "open": 
            trigger=1
            print('\033[32m'+"=========Bem-Vindo=========== "+'\033[0;0m')
        else:
            print('\033[31m'+"Login inválido"+'\033[0;0m')

    while True:
        time.sleep(2)
        os.system("cls")
        print(" === MÓDULO CLIENTE === ")
        print("1 - Cadastrar Banco ou Fintech")
        print("2 - Editar Cadastro")
        print("3 - Listar Banco ou Fintech")
        print("4 - Voltar para o menu principal")
        opcao = int(input("Digite o Opção Desejada:"))

        if opcao == 1:
            cliente.create()
        elif opcao == 2:
            cliente.query()
        elif opcao == 3:
            cliente.listar()
            print("Digite enter para voltar ao menu")
            input()
        elif opcao == 4:
            print("\n Saindo do Programa...")
            break
