from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner, SpinnerOption
from theme import Colours
from kivymd.uix.menu import MDDropdownMenu

# time_settings
class TimeSettings(Screen):
    name = 'time_settings'
    selected_timezone: str = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Timezone'

    def on_pre_enter(self, *args):
        self.add_timezones()
    
        return super().on_pre_enter(*args)
    
    def on_pre_leave(self, *args):
        # Save the Settings to C++
        # print(f'[{"TIME_SETTINGS.PY":16}] Selected Timezone: {self.selected_timezone}')
        
        return super().on_pre_leave(*args)

    def add_timezones(self) -> None:
        tmp_items = [
            {
                'viewclass': 'OneLineListItem',
                'text': self.gmt_ify(i),
                'on_release': lambda val=i: self.select(self.gmt_ify(val)),
            }
            for i in range(-11, 13) # Ah yes, Python...
        ]

        self.timezones: MDDropdownMenu = MDDropdownMenu(caller=self.ids.SelectedTimezone, items=tmp_items, width_mult=2)
     
    def open_menu(self) -> None:
        self.timezones.open()

    def gmt_ify(self, time) -> str:
        return f'GMT{"-" if time < 0 else "+"}{time.__abs__()}'
    
    def select(self, selected):
        self.selected_timezone = selected
        self.ids.SelectedTimezone.text = selected
        self.timezones.dismiss()
