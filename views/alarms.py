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
        self.bind_days()
        self.disable_all()

        self.alarm_manager = GenericManager().alarms

    def on_pre_enter(self, *args):
        self.alarms = self.alarm_manager.alarms
        self.set_all()
        return super().on_pre_enter(*args)

    def bind_days(self) -> None:
        self.days_binds = {}
        # Set the Days
        self.days_binds['Monday'] = self.ids.Monday
        self.days_binds['Tuesday'] = self.ids.Tuesday
        self.days_binds['Wednesday'] = self.ids.Wednesday
        self.days_binds['Thursday'] = self.ids.Thursday
        self.days_binds['Friday'] = self.ids.Friday
        self.days_binds['Saturday'] = self.ids.Saturday
        self.days_binds['Sunday'] = self.ids.Sunday   
        pass

    def disable_all(self) -> None:
        for _, btn in self.days_binds.items():
            btn.md_bg_color = Colours.DISABLED
                
        pass

    def set_all(self) -> None:
        for alarm in self.alarms:
            print(f'[{"ALARMS.PY":16}] {alarm.Day:10}: {alarm.Time if alarm.Enabled else alarm.Enabled}')
            self.days_binds[alarm.Day].md_bg_color = Colours.ENABLED if alarm.Enabled else Colours.DISABLED

        # [self.days_binds[d].md_bg_color = (Colours.ENABLED if t else Colours.DISABLED) for (d, t) in self.alarms.items()]


    def go_to(self, day: str) -> None:
        selected: Alarm = Alarm('', '', False)
        for a in self.alarms:
            selected = a if a.Day.lower() == day.lower() else selected

        print(f'[{"ALARMS.PY":16}] {selected.Day}: {selected.Time if selected.Enabled else "None"}')
        return
        # self.manager.get_screen('alarm')
        self.manager.current = 'alarm'
