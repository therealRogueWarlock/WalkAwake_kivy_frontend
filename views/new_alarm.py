from kivy.uix.screenmanager import Screen

class NewAlarm(Screen):
    name = 'new_alarm'

    def __init__(self, **kw):
        super().__init__(**kw)
    
        self.ids.Header.text = 'New Alarm'
