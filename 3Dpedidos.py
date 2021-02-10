from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from conexao import conexao1
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.config import Config

Config.set('graphics', 'resizable', False) # janela nao alteravel de tamanho
#Config.set('graphics','width','500')  # largura janela
#Config.set('graphics','height','500') #altura janela
conn = conexao1()
sqlittle = """SELECT * FROM Usuarios """


def collect(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    return c.fetchall()


usuario1 = collect(conn, sqlittle)
lista = []

for i, j in usuario1:
    lista.append(i)


class caixa(BoxLayout, Screen):

    def __init__(self, **kwargs):
        super().__init__(*kwargs)

        for element in lista:
            strelement = str(element)
            elementox = adc(text=strelement)
            self.ids.box3.add_widget(elementox)


    def adda_widget(self):
        if adc().check():
           print("oi")


   # def adda_widget1(self):
    #    self.ids.box3.add_widget(Butao2(text='adicionou'))

class adc(BoxLayout):
    def __init__(self, text='',pegar='0', **kwargs):
        super(adc, self).__init__(*kwargs)
        self.ids.elemento.text = text
        self.ids.q.text = text
        self.pegar = pegar

    def check(self):
        self.pegar = self.ids.elemento.text
        print(self.pegar)
        sqlittle3 = """ SELECT Usuario FROM Usuarios WHERE Usuario= '"""+self.pegar+"""' """
        aloca(conn, sqlittle3)

def aloca(connects,sqlittle2):
    c = connects.cursor
    c.execute(sqlittle2)

class maker_3d(App):
    def build(self):
        return caixa()


maker_3d().run()

teste1 = adc()

print(teste1.pegue())
