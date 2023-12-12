from kivy.uix.screenmanager import Screen
from model.managers import GenericManager, AlarmManager
from model.Alarm import Alarm
from theme import Colours

class Alarms(Screen):
    name = 'alarms'
    days_binds: dict
    alarms: list[Alarm]
    alarm_manager: AlarmManager

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Alarms'
        self.bind_days() # UI
        self.disable_all() # Update UI

        self.alarm_manager = GenericManager().alarms

    def on_pre_enter(self, *args):
        # Retrieve the Alarms
        self.alarms = self.alarm_manager.get_alarms()

        self.set_all() # Update UI

        return super().on_pre_enter(*args)

    def bind_days(self) -> None:
        self.days_binds = {}

        # Save a reference to the Widgets
        self.days_binds['Monday'] = self.ids.Monday
        self.days_binds['Tuesday'] = self.ids.Tuesday
        self.days_binds['Wednesday'] = self.ids.Wednesday
        self.days_binds['Thursday'] = self.ids.Thursday
        self.days_binds['Friday'] = self.ids.Friday
        self.days_binds['Saturday'] = self.ids.Saturday
        self.days_binds['Sunday'] = self.ids.Sunday


    def disable_all(self) -> None:
        for _, btn in self.days_binds.items():
            btn.md_bg_color = Colours.DISABLED
                

    def set_all(self) -> None:
        for alarm in self.alarms:
            self.days_binds[alarm.Day].md_bg_color =\
                Colours.ENABLED if alarm.Enabled else Colours.DISABLED


    def go_to(self, day: str) -> None:
        selected: Alarm = Alarm('', '', False) # Default
        for a in self.alarms: # Get the Selected Day
            selected = a if a.Day.lower() == day.lower() else selected
        
        # Handle Selected Day
