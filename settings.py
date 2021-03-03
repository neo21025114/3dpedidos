from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.config import Config


Config.set('graphics', 'width', '200')  # largura janela
Config.set('graphics', 'height', '200') #altura janela


class box_novo(BoxLayout):
    def __init__(self):
        super(box_novo, self).__init__()


class nova_tela(App):
    def build(self):
        return box_novo()

nova_tela().run()