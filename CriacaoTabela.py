from conexao import conexao1
from sqlite3 import Error
from conexao import conexao2
import sqlite3

varconexao = conexao2()

var_comando_sql = """ CREATE TABLE Perfis 
        (Perfil STRING(50), Preço_Filamento REAL(50), Preço_Hora REAL(50), Multiplicador_Filamento REAL(50)); """



def criacao(connection, comando_sql):
    try:
        c = connection.cursor()
        c.execute(comando_sql)

    except Error as er:
        print(er)


criacao(varconexao, var_comando_sql)