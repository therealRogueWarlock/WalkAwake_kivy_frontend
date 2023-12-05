from kivy.uix.screenmanager import Screen


class Alarms(Screen):
    name = 'alarms'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.Header.text = 'Alarms'

    def go_to(self, day: str) -> None:
        print(f'Going to: {screen}')
        self.manager.current = 'alarm'
