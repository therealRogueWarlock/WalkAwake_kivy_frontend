from kivy.uix.screenmanager import Screen
from theme import Icons


# set_alarm_for
class SetAlarmFor(Screen):
    name = 'set_alarm_for'
    days_bind: dict = {}
    days: dict[str, bool] = {
        'Monday': False,
        'Tuesday': False,
        'Wednesday': False,
        'Thursday': False,
        'Friday': False,
        'Saturday': False,
        'Sunday': False
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.Header.text = 'Set On'
        
        self.bind_days()

    def on_pre_enter(self, *args):
        self.disable_all()

        return super().on_pre_enter(*args)

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

    def disable_all(self) -> None:
        for day, enabled in self.days.items():
            self.update_background(day, enabled)

    def toggle(self, day) -> None:
        print(f'Attempting to toggle: {day}')
        if(day not in self.days.keys()):
            return
        
        self.days[day] ^= True
        self.update_background(day, self.days[day])

        return

    def update_background(self, day: str, enabled: bool):
        self.days_bind[day].background_normal = Icons.ROUND_BUTTON_ENABLED if enabled else Icons.ROUND_BUTTON_DISABLED
        self.days_bind[day].background_down = Icons.ROUND_BUTTON_ENABLED if enabled else Icons.ROUND_BUTTON_DISABLED

    def save_alarm(self):
        # Add Logic to Save the Dates
        print('\"saving\"...')
        pass