from kivy.uix.screenmanager import Screen


# wifi_settings
class WifiSettings(Screen):
    name = 'wifi_settings'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Wifi'
