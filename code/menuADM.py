import os
import time
#importa o arquivo de functions
import functions as fun


#importa a biblioteca de data para python
from datetime import date

def principal_adm():
    func = fun.functionsADM()
    trigger = 0

    while trigger == 0:
        login = func.open()
        
        if login == "open": 
            trigger =1
            print('\033[32m'+"=========Bem-Vindo=========== "+'\033[0;0m')
            nceduls= func.take_ceduls()
        else:
            print('\033[31m'+"Login inválido"+'\033[0;0m')

    while True:
        try:
            time.sleep(4)
            os.system("cls")
            print(" === MÓDULO ADMINISTRATIVO === ")
            print("1 - Alimentação de cedulas")
            print("2 - Emitir relatorio")
            print("3 - Sangria")
            print("4 - Log-out")
            print("5 - Vizualizar logs de extratos")
            print("6 - Voltar ao menu principal")
            opcao = int(input("Digite o Opção Desejada:"))


            if opcao == 4:
                print('\033[31m'"\n Saindo do Programa..."'\033[0;0m')
                break

            elif opcao ==1:
                func.takeOperation("Alimentacao de cedulas")
                statusC = func.ceduls_control(nceduls)
                if statusC == 1:
                    print('\033[32m'+"Tudo okay com as notas"+'\033[0;0m')
                    print('-------- Valor minimo : ' + '\033[32m' + "2000"+'\033[0;0m')
                    print('--------Valor no caixa: ' + '\033[32m' + nceduls + '\033[0;0m')
                else:
                    print('\033[31m'+"reposição necessaria"+'\033[0;0m')
                    print('-------- Valor minimo : ' + '\033[32m' + "2000"+'\033[0;0m')
                    print('--------Valor no caixa: ' + '\033[31m' + f"{nceduls}" + '\033[0;0m')
                    
            elif opcao ==2:
                func.takeOperation("Emicao de relatorio")
                op = func.view_op()
                print("================================")
                print(op)
                print('\033[32m'+"Emitindo documento..."+'\033[0;0m')
                arquivo = open('relatorioDeOpracoes.txt', 'w')
                arquivo.write(str(op))
                arquivo.close()

            elif opcao ==3:
                valor_S = func.sangria()
                desc = str(valor_S)
                func.takeOperation(desc)
                print('\033[32m'+"Aguarde enquanto é registrado..."+'\033[0;0m')

            elif opcao ==5:
                func.view_log_extract()
                desc = "Vizualizacao do log de extratos"
                func.takeOperation(desc)
                print('\033[32m'+"Emitindo documento..."+'\033[0;0m')

            elif opcao == 6:
                print("Saindo do programa...")
                break

        except ValueError:
            print("Não foi possivel realizar esta operação",)








#Copyriht by: Lukas Maia