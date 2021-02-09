

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from conexao import conexao1

conn = conexao1()
sqlittle = """SELECT * FROM Usuarios """


class adc(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adc, self).__init__(*kwargs)
        self.ids.q.text = text

    def check(self):
        validacao = True
        return validacao



def collect(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    return c.fetchall()


usuario1 = collect(conn, sqlittle)
lista = []

for i,j in usuario1:
    lista.append(i)


class caixa(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(*kwargs)

        for element in lista:
            strelement = str(element)
            self.ids.box3.add_widget(adc(text=strelement))

    def adda_widget(self):
        if adc().check() is True:
            print("assim vai?")






class adc1(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adc, self).__init__(*kwargs)
        self.ids.q.text = text


class maker_3d(App):
    def build(self):
        return caixa()


maker_3d().run()