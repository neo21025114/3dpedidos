from kivy.app import App
from conexao import conexao1
from conexao import conexao2
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from AdicaoPecas import AdicionarPerfil, sql_perfil
from subprocess import Popen

Config.set('graphics', 'resizable', False) # janela nao alteravel de tamanho
#Config.set('graphics','width','500')  # largura janela
#Config.set('graphics','height','500') #altura janela
conn = conexao1()
conn2 = conexao2()

sqlittle = """SELECT * FROM Modelos """
sqlittle2 = """SELECT * FROM Perfis"""



class adiciona_checkboxes(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adiciona_checkboxes, self).__init__(*kwargs)
        self.ids.elemento.text = text
        self.ids.q.text = text

    def retorna_elemento_selecionado(self):
        adiciona_checkboxes.retorna_elemento_selecionado.pegar = self.ids.elemento.text

    def retorna_todas_informacoes_peca_selecionada(self):
        sqlittle4 = """SELECT * FROM Modelos WHERE Peça='""" +adiciona_checkboxes.retorgina_elemento_selecionado.pegar+ """' """
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
lista3=[]
for i, j, k, l, m in pecas:
    lista.append(i)

for n, o, p, q in perfis:
    lista2.append(n)

for r,s,t,u in perfis:
    lista3.append(r)

tamanho = len(lista2)
print(tamanho)
adctamanho = str(tamanho+1)


class caixa(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for element in lista:
            strelement = str(element)
            self.ids.box3.add_widget(adiciona_checkboxes(text=strelement))
        for element2 in lista2:
            strelement2 = str(element2)
            self.ids.box22.add_widget(adiciona_checkboxes2(text=strelement2))



    def reset(self):
        n = 0
        if len(lista3) != 0:
            for element4 in lista3:
                n = n + 1
                if n == tamanho:

                    sqlittlePerfil = """SELECT Perfil FROM Perfis WHERE Perfil='Perfil """+adctamanho+"""'"""
                    c = conn2.cursor()
                    c.execute(sqlittlePerfil)
                    retorna_novo_perfil = c.fetchall()
                    elemento_unico = str(retorna_novo_perfil[0][0])
                    self.ids.box22.add_widget(adiciona_checkboxes2(text=elemento_unico))
                    print("aq foi")
        else:

            sqlittlePerfil = """SELECT Perfil FROM Perfis WHERE Perfil='Perfil """ + adctamanho + """'"""
            c = conn2.cursor()
            c.execute(sqlittlePerfil)
            retorna_novo_perfil = c.fetchall()
            elemento_unico = str(retorna_novo_perfil[0][0])
            self.ids.box22.add_widget(adiciona_checkboxes2(text=elemento_unico))
            print("aq foi tbm")

    def juncao(self):
        print(adiciona_checkboxes2.retorna_elemento_selecionado.pegar)
        print(adiciona_checkboxes.retorna_elemento_selecionado.pegar)


class CustomScreen(ScreenManager):
    def __init__(self, **kwargs):
        super(CustomScreen, self).__init__(**kwargs)
        self.add_widget(caixa())
        self.add_widget(adicao_perfil(name='tela_nova'))
        self.add_widget(tela_concluido(name='telinha'))

    #def abre_nova_peca(self):
     #   CustomScreen().add_widget(adicao_pecas())
      #  print("ate aq")

    #def __init__(self,text='pass', **kwargs):
        #super(CustomScreen, self).__init__(*kwar
       # self.ids.bot_perfil.text = text
      #  print("helow")


class tela_concluido(Screen):
    def __init__(self, **kwargs):
        super(tela_concluido, self ).__init__(**kwargs)


class adicao_perfil(Screen):
    def __init__(self, **kwargs):
        super(adicao_perfil, self).__init__(**kwargs)

    def adiciona_perfil(self):
        fila = str(self.ids.filamento.text)
        hour = str(self.ids.hora.text)
        multi = str(self.ids.mult.text)
        soma = tamanho + 1
        perfil = 'Perfil '+str(soma)
        AdicionarPerfil(conn2, sql_perfil, perfil, fila, hour, multi)
    def tela_concluido(self):
        process = Popen(['python3', 'settings.py'])


class maker_3d(App):
    def build(self):
        return CustomScreen()



maker_3d().run()




