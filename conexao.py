import sqlite3
from sqlite3 import Error


def conexao1():
    caminho = "C:\\Bancos\\AcaoFigurada.db"
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as er:
        print(er)

def conexao2():
    caminho = "C:\\Bancos\\Perfis.db"
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as er:
        print(er)