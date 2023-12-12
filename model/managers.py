import datetime as dt
from model.Alarm import Alarm, as_alarm
from WalkAwake import *
import json


class AlarmManager(object):
    old_alarms: dict[str, object]
    alarms: list[Alarm]
    manager: AlarmModule.AlarmManager

    def __init__(self, manager) -> None:
        self.manager = manager
        # Read alarms from Back End
        path = 'data/Alarms.json'
        with open(path) as p:
            self.alarms = json.load(p, object_hook=as_alarm)
        # Parse alarms (json.loads('json string'))

        # Check if self.alarms is empty
        if len(self.alarms) == 0:
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
            if day == alarm.Day:
                alarm.Time = time.strftime('%H:%M')
                alarm.Enabled = True

    def save_alarms(self):
        formatted = json.dumps(self.alarms, default=lambda alarm: alarm.__dict__)
        formatted = f'{{"alarms":{formatted}}}'
        self.manager.UpdateAlarms(formatted)
        pass

    def stop_alarm(self):
        self.manager.StopAlarm()

    def snooze(self):
        self.manager.Snooze()


class CallbackManager(object):
    callback_functions: dict = {} # dict[str, function]
    manager: AlarmModule.AlarmManager

    def __init__(self, manager) -> None:
        self.manager = manager
        self.manager.RegisterCallback(self.callback)

    def callback(self, info: str):
        fun = self.callback_functions[info]
        if fun: # fun is None if not found from info
            fun()

    def registerCallback(self, identifier: str, cb_function) -> None:
        # Register the Callback using the Identifier to differentiate
        self.callback_functions[identifier] = cb_function


    def unregister(self, identifier: str) -> None:
        # Remove the callback function
        self.callback_functions.pop(identifier)


class GenericManager(object):
    backend: object
    alarms: AlarmManager
    callbacks: CallbackManager

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GenericManager, cls).__new__(cls)

        return cls.instance

    def __init__(self) -> None:
        self.backend = AlarmModule.AlarmManager()
        self.alarms = AlarmManager(self.backend)
        self.callbacks = CallbackManager(self.backend)

    pass


if __name__ == '__main__':
    m = AlarmManager(None)

    j = json.dumps(m.alarms, default=lambda a: a.__dict__)
    j = f'{{"alarms":{j}}}'

    print(f'{j}')

    c = CallbackManager(None)
    c.callback('this is not in the DICT')