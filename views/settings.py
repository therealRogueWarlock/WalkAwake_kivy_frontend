from kivy.uix.screenmanager import Screen


class Settings(Screen):
    name = 'settings'

    def on_pre_enter(self):
        print("pre enter settings")

    def __init__(self, **kw):
        super().__init__(**kw)

        # Set initial values

        # Schedule for Updates
