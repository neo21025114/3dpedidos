from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from conexao import conexao1
from conexao import conexao2
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from AdicaoPecas import adicao_pecas
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from random import random
from kivy.properties import NumericProperty

Config.set('graphics', 'resizable', False) # janela nao alteravel de tamanho
#Config.set('graphics','width','500')  # largura janela
#Config.set('graphics','height','500') #altura janela
conn = conexao1()
conn2 = conexao2()

sqlittle = """SELECT * FROM Modelos """
sqlittle2 = """SELECT * FROM Perfis1"""



class adiciona_checkboxes(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adiciona_checkboxes, self).__init__(*kwargs)
        self.ids.elemento.text = text
        self.ids.q.text = text

    def retorna_elemento_selecionado(self):
        adiciona_checkboxes.retorna_elemento_selecionado.pegar = self.ids.elemento.text

    def retorna_todas_informacoes_peca_selecionada(self):
        sqlittle4 = """SELECT * FROM Modelos WHERE Peça='""" +adiciona_checkboxes.retorna_elemento_selecionado.pegar+ """' """
        c = conn.cursor()
        c.execute(sqlittle4)
        print(c.fetchall())


class adiciona_checkboxes2(BoxLayout):

    def __init__(self, text='', **kwargs):
        super(adiciona_checkboxes2, self).__init__(*kwargs)
        self.ids.elemento.text = text
        self.ids.q.text = text

    def retorna_elemento_selecionado(self):
        adiciona_checkboxes2.retorna_elemento_selecionado.pegar = self.ids.elemento.text

    def retorna_todas_informacoes_peca_selecionada(self):
        sqlittle4 = """SELECT * FROM Perfil1 WHERE Perfil='""" + adiciona_checkboxes2.retorna_elemento_selecionado.pegar+ """' """
        c = conn.cursor()
        c.execute(sqlittle4)
        print(c.fetchall())


def retorna_todas_pecas(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    return c.fetchall()


def seleciona_peca(connects, sqlittle2):
    c = connects.cursor()
    c.execute(sqlittle2)
    var = c.fetchall()
    return var


perfis = retorna_todas_pecas(conn2, sqlittle2)
pecas = retorna_todas_pecas(conn, sqlittle)

lista = []
lista2 = []

for i, j, k, l, m in pecas:
    lista.append(i)

for k, l, m, n in perfis:
    lista2.append(k)

print(lista2)

class caixa(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(*kwargs)

        for element in lista:
            strelement = str(element)
            self.ids.box3.add_widget(adiciona_checkboxes(text=strelement))
        for element2 in lista2:
            strelement2 = str(element2)
            self.ids.box22.add_widget(adiciona_checkboxes2(text=strelement2))

    def abre_novo_perfil(self):
        ScreenManager().add_widget(CustomScreen(text='deu certo'))

    def juncao(self):
        print(adiciona_checkboxes2.retorna_elemento_selecionado.pegar)
        print(adiciona_checkboxes.retorna_elemento_selecionado.pegar)


class CustomScreen(Screen):
    def __init__(self,text='pass', **kwargs):
        super(CustomScreen, self).__init__(*kwargs)
        self.ids.bot_perfil.text = text
        print("helow")


class maker_3d(App):
    def build(self):
        self.adiciona_checkboxes = adiciona_checkboxes()
        self.adiciona_checboxes2 = adiciona_checkboxes2()
        return caixa()

maker_3d().run()



