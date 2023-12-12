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
        # self.get_alarms() # This should work

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
        # Serialize the Alarms as a JSON string
        formatted =\
            json.dumps(self.alarms,\
                       default=lambda alarm: alarm.__dict__)

        # Prepend & Append needed overhead
        formatted = f'{{"alarms":{formatted}}}'

        # Update the Back End
        self.manager.UpdateAlarms(formatted)


    def stop_alarm(self):
        self.manager.StopAlarm()


    def snooze(self):
        # self.manager.Snooze() # This causes a weird bug
        pass


    def get_alarms(self) -> list[Alarm]:
        # Get Alarms from backend
        alarms_json = self.manager.GetAlarms()
        
        # Parse Alarms to List of Alarms
        self.alarms = json.loads(alarms_json, object_hook=as_alarm)

        return self.alarms

class CallbackManager(object):
    callback_functions: dict = {} # dict[str, function]
    manager: AlarmModule.AlarmManager

    def __init__(self, manager) -> None:
        self.manager = manager
        
        # Register function as Callback
        # function used by Back End
        self.manager.RegisterCallback(self.callback)

    def callback(self, info: str):
        fun = self.callback_functions[info]
        if fun: # fun is None (falsy) if not found from info
            fun() # Function is indeed a Fun one :)

    def registerCallback(self, identifier: str, cb_function) -> None:
        # Register the Callback using the Identifier to differentiate
        self.callback_functions[identifier] = cb_function


    def unregister(self, identifier: str) -> None:
        # Remove the callback function
        self.callback_functions.pop(identifier)


class GenericManager(object):
    # C++ Back End
    backend: object

    # Managers
    alarms: AlarmManager
    callbacks: CallbackManager

    # Singleton on Constructor
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GenericManager, cls).__new__(cls)

        return cls.instance


    def __init__(self) -> None:
        self.backend = AlarmModule.AlarmManager()
        self.alarms = AlarmManager(self.backend)
        self.callbacks = CallbackManager(self.backend)

