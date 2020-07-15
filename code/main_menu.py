import os
import time
from menu_cli import principal_cli
from menu_mov import principal_mov
from menuADM import principal_adm


def principal():

    while True:
        time.sleep(2)
        os.system("cls")
        print(" === SISTEMA DE CAIXA ELETRÔNICO === ")
        print("1 - Módulo Administração")
        print("2 - Módulo Cliente")
        print("3 - Módulo Movimentação")
        print("4 - Sair do Sistema do Banco")
        opcao = int(input("Digite o Opção Desejada:"))

        if opcao == 1:
            principal_adm()
        elif opcao == 2:
            principal_cli()
        elif opcao == 3:
            principal_mov()
        elif opcao == 4:
            print("\n Saindo do Programa...")
            break
        else:
            print("Opcão incorreta, por favor digite novamente...")

principal()
