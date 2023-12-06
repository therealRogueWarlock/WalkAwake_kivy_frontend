from kivy.uix.screenmanager import Screen
from theme import Icons

class Alarms(Screen):
    name = 'alarms'
    days: dict[any, bool] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Alarms'
        self.bind_days()
        self.disable_all()

    def bind_days(self) -> None:
        # Set the Days
        self.days['Monday'] = self.ids.Monday
        self.days['Tuesday'] = self.ids.Tuesday
        self.days['Wednesday'] = self.ids.Wednesday
        self.days['Thursday'] = self.ids.Thursday
        self.days['Friday'] = self.ids.Friday
        self.days['Saturday'] = self.ids.Saturday
        self.days['Sunday'] = self.ids.Sunday   
        pass

    def disable_all(self) -> None:
        for day, btn in self.days.items():
            btn.background_normal = Icons.ROUND_BUTTON_DISABLED
            btn.background_down = Icons.ROUND_BUTTON_ENABLED
            if day == 'Monday':
                btn.background_normal = Icons.ROUND_BUTTON_ENABLED
                btn.background_down = Icons.ROUND_BUTTON_DISABLED
                
        pass

    def go_to(self, day: str) -> None:
        print(f'Going to: {day}')
        return
        # self.manager.get_screen('alarm')
        self.manager.current = 'alarm'
