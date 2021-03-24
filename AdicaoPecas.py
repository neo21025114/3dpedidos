from conexao import conexao1
from sqlite3 import Error


sql_peca = """ INSERT INTO Modelos (Peça, Tempo, Peso)"""

sql_peca = """ INSERT INTO Modelos (Peça, Peso, Tempo)

               VALUES(?, ?, ?);
            """

sql_perfil = """INSERT INTO Perfis (Perfil, Preço_Filamento, Preço_Hora, Multiplicador_Filamento)
                VALUES(?, ?, ?, ?)
            """

def consulta(connect, command):
    ce = connect.cursor()
    ce.execute(command)
    fila = ce.fetchall()
    return fila


def AdicionarPerfil(connection, commander, a, b, c,d):
    try:
        ca = connection.cursor()
        ca.execute(commander, (a, b, c,d))
        connection.commit()
    except Error as er:
        print(er)


def AdicionarPeca(conexao, comando_sql, e, f, g):

    try:
        c = conexao.cursor()
        c.execute(comando_sql, (e, f, g))
        conexao.commit()
    except Error as er:
        print(er)

