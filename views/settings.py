from kivy.uix.screenmanager import Screen


class Settings(Screen):
    name = 'settings'

    def __init__(self, **kw):
        super().__init__(**kw)
        
        self.ids.Header.text = 'Settings'

    def on_pre_enter(self):
        print("Maybe preload Settings?")
