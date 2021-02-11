import sqlite3
from sqlite3 import Error


def conexao1():
    caminho = "C:\\Users\\danrley.sena\\Documents\\Python\\Programas\\bancos\\Usuarios.db"
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as er:
        print(er)
