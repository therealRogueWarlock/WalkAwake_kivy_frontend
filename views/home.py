from datetime import date, datetime
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy import utils

class Home(Screen):
    name = 'home'

    def __init__(self, **kw):
        super().__init__(**kw)

        # Set initial values
        self.set_next_alarm()
        self.set_date()
        self.set_time()

        # Schedule for Updates
        Clock.schedule_interval(lambda dt: self.set_date(), 300)
        Clock.schedule_interval(lambda dt: self.set_time(), 1)

    def Settings(self) -> None:
        return

    #
    def set_date(self) -> None:
        today = date.today()
        self.ids.Date.text = today.strftime("%d %b, %Y")
        return

    def set_time(self) -> None:
        now = datetime.now()
        self.ids.CurrentTime.text = now.strftime("%H:%M")
        return

    def set_next_alarm(self) -> None:
        # Get Alarm for Tomorrow if one is made
        alarm_tomorrow = '' or 'None Tomorrow'
        self.ids.NextAlarm.text = alarm_tomorrow
        return
