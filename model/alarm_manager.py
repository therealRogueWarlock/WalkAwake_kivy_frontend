import datetime as dt
from Alarm import Alarm
import json

class AlarmManager(object):
    old_alarms: dict[str, object]
    alarms: list[Alarm]

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AlarmManager, cls).__new__(cls)
        
        return cls.instance

    def __init__(self) -> None:
        # Read alarms from Back End

        # Parse alarms (json.loads('json string'))

        # Check if self.alarms is empty

        # if empty: use default
        self.alarms = [
            Alarm('Sunday', '00:00', False),
            Alarm('Monday', '00:00', False),
            Alarm('Tuesday', '00:00', False),
            Alarm('Wednesday', '00:00', False),
            Alarm('Thursday', '00:00', False),
            Alarm('Friday', '00:00', False),
            Alarm('Saturday', '00:00', False),
        ]
        

    def set_alarm(self, day: str, time: dt.time):
        for alarm in self.alarms:
            if(day == alarm.Day):
                alarm.Time = time.strftime('%H:%M')
                alarm.Enabled = True

    def save_alarms(self):
        formatted = json.dumps(self.alarms, default=lambda alarm: alarm.__dict__)
        formatted = f'{{"alarms:{formatted}"}}'
        # Save the Alarms using the C++ Library
        pass

if __name__ == '__main__':
    m = AlarmManager()

    j = json.dumps(m.alarms, default=lambda a: a.__dict__)
    j = f'{{"alarms":{j}}}'

    print(f'{j}')