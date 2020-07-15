
import mysql.connector #imprta o driver mysql
import os

class conncetToBd:

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="transactions"
        )

        mycursor = mydb.cursor()
    except:
        print("Não foi possível realizar a conexão com o banco")
    
    def select_all(self):

        try:

            sql2 = "SELECT * FROM extrato"

            mycursor.execute(sql2)

            myresult = mycursor.fetchall()

            return myresult
        except Error as e:
            print(e)


