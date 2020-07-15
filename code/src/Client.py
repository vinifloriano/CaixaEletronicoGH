from src.database.connection import conncetToBd
from src.database.connection import conncetToBd
import random
from datetime import datetime
from datetime import date
conexao = conncetToBd()
mydb = conexao.mydb
mycursor = conexao.mycursor

class Client:

    def create(self):
        cnpj = str(input("Digite o cnpj:  "))
        nome = str(input("Digite o nome: "))
        localizacao = str(input("Digite a localização:  "))
        insc_est = str(input("Digite a inscrição estadual:  "))

        values = (cnpj, nome,  localizacao, insc_est)

        try:
            mycursor.execute(
                "INSERT INTO cliente(cnpj, nome, localizacao, insc_est) VALUES(%s, %s, %s, %s)", values)
            mydb.commit()
        except ConnectionError:
            print('Não foi possível cadastrar um novo usuário...     ')

        return 'Created', 201

    def query(self):

        cnpj = input("Digite o CNPJ: ")
        mycursor.execute(
            f"SELECT  nome,  localizacao, insc_est, ativo FROM cliente WHERE cnpj={cnpj}")
        origem_valores = mycursor.fetchall()
        for i in origem_valores:

            novo_nome = input(f"Nome: {i[0]}, digite novo nome: ")
            nova_localizacao = input(f"Localização: {i[1]}, digite nova localização: ")
            nova_incricao = input(f"Inscrição Estadual: {i[2]}, digite nova inscrição estadual: ")
            texto_ativo = "ativo"
            if (i[3] == 0): texto_ativo = "inativo"
            novo_ativo = input(f"O cliente está {texto_ativo}, digite 1 para ativar ou 0 para desativar: ")

            if novo_nome == "": novo_nome = i[0]
            if nova_localizacao == "": nova_localizacao = i[1] 
            if nova_incricao == "": nova_incricao = i[2] 
            if novo_ativo == "": novo_ativo = i[3]

            values = (novo_nome, nova_localizacao, nova_incricao, novas_funcionalidades, novo_ativo)

            try:
                mycursor.execute(
                    "UPDATE cliente SET nome = %s, localizacao = %s, insc_est = %s, ativo = %s where cnpj = "+cnpj, values)
                mydb.commit()
            except ConnectionError:
                print('Não foi possível cadastrar um novo usuário...     ')
        
        return 200

    def listar(self):
        mycursor.execute(
            f"SELECT * FROM cliente")
        origem_valores = mycursor.fetchall()
        for i in origem_valores:
            print()
            print(f"Cnpj: {i[0]}")
            print(f"Nome: {i[1]}")
            print(f"Localização: {i[2]}")
            print(f"Inscrição Estadual: {i[3]}")
            texto_ativo = "ativo"
            if (i[4] == 0): texto_ativo = "inativo"
            print(f"O cliente está {texto_ativo}")
            print()
        return 200
