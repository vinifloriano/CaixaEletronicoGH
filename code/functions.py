import os
import time

#faz a importacão do modulo prettytable
#from prettytable import PrettyTable
#from prettytable import from_csv
#from prettytable import from_html

#faz a importação da classe de conexão
from src.database.connection import conncetToBd
from src.database.connection import conncetToBd
conexao = conncetToBd()
mydb = conexao.mydb
mycursor = conexao.mycursor


login =["admin@2020","invite@2020"]
senha=["admin","invite"]
operations = []

#classe de funcoes do adm

class functionsADM:
   

    def open(self):
        
        

        print("==========LOGIN=============")
        
        VeLogin = str(input("Login: "))
        VeSenha = str(input("Senha: "))

        if VeLogin in login and VeSenha in senha:
            status= "open"
            return status 
        else:
            status = "closed"
            return status 
 

    def ceduls_control(self, numberCels):

        min_ = 2000

        if numberCels < min_ :
            status = 0
            return status
        else:
            status = 1
            return status

    def take_ceduls(self):
        nceduls = int(input("Numero de cedulas no caixa: "))
        return nceduls

    def takeOperation(self,desc):
        operations.append(desc)

    def view_op(self):
        return operations
        

    def sangria(self):

        valor_ = int(input("Valor da sangria: "))

        return valor_

    def view_log_extract(self):
        
        myc = conexao.select_all()

        arquivo = open('relatorioExtratos.txt', 'w')
        arquivo.write(str(myc))
        arquivo.close()