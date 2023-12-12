from kivy.uix.screenmanager import Screen


class WifiSettings(Screen):
    name = 'wifi_settings'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Wifi'
