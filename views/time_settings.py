from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from theme import Text


# time_settings
class TimeSettings(Screen):
    name = 'time_settings'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.Header.text = 'Timezone'
        
    def on_pre_enter(self, *args):
        self.add_timezones()
    
        return super().on_pre_enter(*args)

    def add_timezones(self) -> None:
        for i in range(-11, 13):
            prefix = '-' if i < 0 else '+'  # Ternary
            value = i.__abs__()             # Absolute Value
            
            text = f'GMT{prefix}{value}'    # Combing GMT & Prefix & Value

            self.ids.Timezones.values.append(text)
     
    def spinner_clicked(self, value):
        print(value)
        pass

