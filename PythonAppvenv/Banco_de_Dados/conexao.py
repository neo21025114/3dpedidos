import sqlite3
from sqlite3 import Error


def conexao1():
    caminho = "C:\\Banco\\AcaoFigurada.db"
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as er:
        print(er)

def conexao2():
    caminho = "C:\\Banco\\Perfis.db"
    try:
        con1 = sqlite3.connect(caminho)
        return con1
    except Error as er:
        print(er)