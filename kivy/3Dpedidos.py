
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from conexao import conexao1

conn = conexao1()
sqlittle = """SELECT * FROM Usuarios """


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

   # def adda_widget(self):
        #self.ids.box2.add_widget(adc1(text=strusuario))

   # def adda_widget1(self):
    #    self.ids.box3.add_widget(Butao2(text='adicionou'))




class adc(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adc, self).__init__(*kwargs)
        self.ids.b.text = text


class adc1(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adc, self).__init__(*kwargs)
        self.ids.c.text = text


class maker_3d(App):
    def build(self):
        return caixa()


maker_3d().run()