from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from conexao import conexao1
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Config.set('graphics', 'resizable', False) # janela nao alteravel de tamanho
#Config.set('graphics','width','500')  # largura janela
#Config.set('graphics','height','500') #altura janela
conn = conexao1()
sqlittle = """SELECT * FROM Usuarios """


class adc(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adc, self).__init__(*kwargs)
        self.ids.elemento.text = text
        self.ids.q.text = text

    def check(self):
        self.pegar = self.ids.elemento.text
        sqlittle3 = """ SELECT Usuario FROM Usuarios WHERE Usuario= '""" + self.pegar + """' """
        adc.check.elemento1 = aloca(conn, sqlittle3)
        adc.check.elemento2 = str(adc.check.elemento1[0][0])

    def puxa_inf(self):
        sqlittle4 = """SELECT * FROM Usuarios WHERE Usuario='""" + adc.check.elemento2 + """' """
        c = conn.cursor()
        c.execute(sqlittle4)
        list = c.fetchall()
        adc.puxa_inf.informacoes1 = str(list[0][0])
        adc.puxa_inf.informacoes2 = str(list[0][1])

        caixa().wid()
class adc1(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(adc1, self).__init__(*kwargs)
        self.ids.caixas22.text = text


def collect(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    return c.fetchall()


def aloca(connects,sqlittle2):
    c = connects.cursor()
    c.execute(sqlittle2)
    var = c.fetchall()
    return var


usuario1 = collect(conn, sqlittle)
lista = []

for i, j in usuario1:
    lista.append(i)


class caixa(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(*kwargs)

        for element in lista:
            strelement = str(element)
            self.ids.box3.add_widget(adc(text=strelement))

    def wid(self):
        print(adc.puxa_inf.informacoes1)
        print(adc.puxa_inf.informacoes2)



class maker_3d(App):
    def build(self):
        self.adc = adc()
        return caixa()


maker_3d().run()



