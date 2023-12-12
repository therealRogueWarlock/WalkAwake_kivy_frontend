from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu

class TimeSettings(Screen):
    name = 'time_settings'

    selected_timezone: str = ''


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Timezone'


    def on_pre_enter(self, *args):
        # Add all Timezones to a List
        self.add_timezones()
    
        return super().on_pre_enter(*args)
    

    def on_pre_leave(self, *args):
        # Save Settings to Back End

        return super().on_pre_leave(*args)


    def add_timezones(self) -> None:
        # Adds from GMT-11 to GMT+12 to a list
        # using List Comprehension
        tmp_items = [
            {
                'viewclass': 'OneLineListItem',
                'text': self.gmt_ify(i),
                'on_release': lambda val=i: self.select(self.gmt_ify(val)),
            }
            for i in range(-11, 13)
        ]

        # Set the List of Timezones in the Drop Down Menu
        self.timezones: MDDropdownMenu =\
            MDDropdownMenu(caller=self.ids.SelectedTimezone,\
                           items=tmp_items, width_mult=2)
    

    def open_menu(self) -> None:
        self.timezones.open()


    def gmt_ify(self, time) -> str:
        # Ensure a Number has a +/- in front
        return f'GMT{"-" if time < 0 else "+"}{time.__abs__()}'
    

    def select(self, selected):
        self.selected_timezone = selected

        # Update UI
        self.ids.SelectedTimezone.text = selected

        # Close the Drop Down Menu
        self.timezones.dismiss()
