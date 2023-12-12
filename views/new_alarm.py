from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDTimePicker

from datetime import time
from model.managers import GenericManager, AlarmManager
from theme import Colours

class NewAlarm(Screen):
    name = 'new_alarm'

    alarm_manager: AlarmManager
    
    selected_time: time
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

    time_picker: MDTimePicker

    def __init__(self, **kw):
        super().__init__(**kw)

        # Retrieve the Alarm Manager
        self.alarm_manager = GenericManager().alarms
    
        # Continue Setup
        self.ids.Header.text = 'New Alarm'
        self.bind_days()
        self.time_picker = MDTimePicker()
        self.time_picker.bind(time=self.get_time)


    def on_pre_enter(self, *args):
        self.disable_all()
        return super().on_pre_enter(*args)


    def get_time(self, instance, time):
        self.selected_time = time

        # Show Time on the UI Button
        formatted_time = time.strftime('%H:%M')
        self.ids.TimeButton.text = formatted_time # UI


    def bind_days(self) -> None:
        # Set the Days
        self.days_bind['Monday'] = self.ids.Monday
        self.days_bind['Tuesday'] = self.ids.Tuesday
        self.days_bind['Wednesday'] = self.ids.Wednesday
        self.days_bind['Thursday'] = self.ids.Thursday
        self.days_bind['Friday'] = self.ids.Friday
        self.days_bind['Saturday'] = self.ids.Saturday
        self.days_bind['Sunday'] = self.ids.Sunday   


    def disable_all(self) -> None:
        for day, _ in self.days.items():
            self.toggle(day, force=True, v=False)

    def toggle(self, day, force = False, v: bool = False) -> None:
        if(day not in self.days.keys()):
            return None
        
        if(force): # Force a value if needed
            self.days[day] = v
        else: # Default (normal) just flips value
            self.days[day] ^= True

        # Update the UI
        self.update_background(day, self.days[day])


    def update_background(self, day: str, enabled: bool) -> None:
        self.days_bind[day].md_bg_color =\
            Colours.ENABLED if enabled else Colours.DISABLED


    def save_alarm(self) -> None:
        # Get the Days that are Enabled
        selected_days = [str(day) for day in self.days if self.days[day]]

        # Set the Time in Alarm Manager for Selected Days
        # using List Comprehension (very pythonic)
        [self.alarm_manager.set_alarm(day, self.selected_time)\
         for day in selected_days]
        
        # Save the Alarms through Back End
        self.alarm_manager.save_alarms()

