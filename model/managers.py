import datetime as dt
from model.Alarm import Alarm
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


class CallbackManager(object):
    callback_functions: dict = {} # dict[str, function]

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CallbackManager, cls).__new__(cls)
        
        return cls.instance
    
    def callback(self, info: str):
        fun = self.callback_functions[info]
        if(fun): # fun is None if not found from info
            fun()
        

    def registerCallback(self, identifier: str, cb_function) -> None:
        # Register the Callback using the Identifier to differentiate
        self.callback_functions[identifier] = cb_function


    def unregister(self, identifier: str) -> None:
        # Remove the callback function
        self.callback_functions.pop(identifier)


if __name__ == '__main__':
    m = AlarmManager()

    j = json.dumps(m.alarms, default=lambda a: a.__dict__)
    j = f'{{"alarms":{j}}}'

    print(f'{j}')

    c = CallbackManager()
    c.callback('this is not in the DICT')