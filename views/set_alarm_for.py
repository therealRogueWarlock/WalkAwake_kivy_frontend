from kivy.uix.screenmanager import Screen
from theme import Icons


# set_alarm_for
class SetAlarmFor(Screen):
    name = 'set_alarm_for'
    days_bind: dict[str, any] ={}
    days: dict = {
        'monday': False,
        'tuesday': False,
        'wednesday': False,
        'thursday': False,
        'friday': False,
        'saturday': False,
        'sunday': False
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.Header.text = 'Set On'
        
        self.bind_days()

    def on_pre_leave(self, *args):
        # Save Alarm to specific days
        return super().on_pre_leave(*args)

    def bind_days(self) -> None:
        # Set the Days
        self.days_bind['Monday'] = self.ids.Monday
        self.days_bind['Tuesday'] = self.ids.Tuesday
        self.days_bind['Wednesday'] = self.ids.Wednesday
        self.days_bind['Thursday'] = self.ids.Thursday
        self.days_bind['Friday'] = self.ids.Friday
        self.days_bind['Saturday'] = self.ids.Saturday
        self.days_bind['Sunday'] = self.ids.Sunday   
        pass

    def toggle(self, value):
        if(value not in self.days.keys):
            return
        
        self.days[value] ^= True
        self.update_background(value, self.days[value])

        return

    def update_background(self, day: str, enabled: bool):
        self.days_bind[day].background_normal = Icons.ROUND_BUTTON_ENABLED if enabled else Icons.ROUND_BUTTON_DISABLED
        self.days_bind[day].background_down = Icons.ROUND_BUTTON_ENABLED if enabled else Icons.ROUND_BUTTON_DISABLED