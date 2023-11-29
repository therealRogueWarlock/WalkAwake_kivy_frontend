from kivy.uix.screenmanager import Screen


class Settings(Screen):
    name = 'settings'

    def on_pre_enter(self):
        print("pre enter settings")
