from kivy.uix.screenmanager import Screen


# set_alarm
class SetAlarm(Screen):
    name = 'set_alarm'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Set Alarm'
