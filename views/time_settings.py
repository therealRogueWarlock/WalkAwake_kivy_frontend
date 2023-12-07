from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner, SpinnerOption
from theme import Text, Colour


# time_settings
class TimeSettings(Screen):
    name = 'time_settings'
    selected_timezone: str = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Timezone'
        
    def on_pre_enter(self, *args):
        self.setup_spinner_options()

        self.add_timezones()
    
        return super().on_pre_enter(*args)
    
    def on_pre_leave(self, *args):
        # Save the Settings to C++
        print(f'Selected Timezone: {self.selected_timezone}')
        return super().on_pre_leave(*args)

    def setup_spinner_options(self):
        # Save option for Intellisense
        spinner: Spinner = self.ids.Timezones
        option: SpinnerOption = spinner.option_cls

        # Images
        option.background_normal = ''
        # Colours
        option.background_color = Colour.INVISIBLE
        option.outline_width = 2
        option.outline_color = Colour.ACCENT

    def add_timezones(self) -> None:
        for i in range(-11, 13):
            prefix = '-' if i < 0 else '+'  # Ternary
            value = i.__abs__()             # Absolute Value
            
            text = f'GMT{prefix}{value}'    # Combing GMT & Prefix & Value

            self.ids.Timezones.values.append(text)
     
    def spinner_clicked(self, value):
        self.selected_timezone = value
        pass

