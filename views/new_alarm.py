from kivy.uix.screenmanager import Screen

from theme import Colours

class NewAlarm(Screen):
    name = 'new_alarm'
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
    
        self.ids.Header.text = 'New Alarm'
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
        for day, _ in self.days.items():
            self.toggle(day, force=True, v=False)

    def toggle(self, day, force = False, v: bool = False) -> None:
        if(day not in self.days.keys()):
            return
        
        if(force):
            self.days[day] = v
        else:
            self.days[day] ^= True

        self.update_background(day, self.days[day])

        return

    def update_background(self, day: str, enabled: bool):
        self.days_bind[day].md_bg_color = Colours.ENABLED if enabled else Colours.DISABLED

    def save_alarm(self):
        # Add Logic to Save the Dates
        print('\"saving\"...')
        pass
