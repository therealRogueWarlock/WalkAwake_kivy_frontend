from kivy.uix.screenmanager import Screen
from model.managers import GenericManager
from datetime import datetime as dt


class WakeUp(Screen):
    name = 'wakeup'

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        self.ids.CurrentTime.text = dt.now().strftime('%H:%M')
        return super().on_enter(*args)

    def on_touch_down(self, touch):
        self.snooze()
        return super().on_touch_down(touch)

    def snooze(self):
        print('Snoozing')
        # Call Backend Snooze
        GenericManager().alarms.snooze()

        self.manager.transition.duration = 1
        self.manager.transition.direction = 'up'
        self.manager.current = 'camera'
