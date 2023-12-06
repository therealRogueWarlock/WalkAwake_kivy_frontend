from kivy.uix.screenmanager import Screen


# set_alarm_for
class SetAlarmFor(Screen):
    name = 'set_alarm_for'

    def __init__(self, **kw):
        super().__init__(**kw)

        self.ids.Header.text = 'Set On'
