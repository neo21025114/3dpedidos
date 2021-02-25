from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.config import Config
from kivy.uix.scrollview import ScrollView
Config.set('graphics', 'resizable', False)


class TelaPrincipal(BoxLayout):

    def __init__(self, **kwargs):
        super(TelaPrincipal,self).__init__(**kwargs)


    def inserir(self):
        texto = str(self.ids.input.text)
        self.ids.box1.add_widget(Tarefas(text=texto))


class Tarefas(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(Tarefas, self).__init__(*kwargs)
        self.ids.tarefa.text = text


class layout(App):
    def build(self):
        return TelaPrincipal()


layout().run()