from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

class Settings(Screen):
    name = 'settings'

    def __init__(self, **kw):
        super().__init__(**kw)
        
        self.ids.Header.text = 'Settings'

    def on_enter(self, *args):
        Window.clear()
        return super().on_enter(*args)