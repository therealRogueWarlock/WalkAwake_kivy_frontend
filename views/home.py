from kivy.uix.screenmanager import Screen


class Home(Screen):
    name = 'home'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.counter = 0

    def on_click_button(self):
        self.counter += 1
        count_label = self.ids.DisplayCountLabel
        count_label.text = str(self.counter)
        print(self.manager.screens)
        print(self.counter)

    def on_pre_enter(self):
        print("pre enter main")
