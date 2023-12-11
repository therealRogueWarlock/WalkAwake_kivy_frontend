import datetime as dt

class AlarmManager(object):
    alarms: dict[str, object]

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AlarmManager, cls).__new__(cls)
        
        return cls.instance

    def __init__(self) -> None:
        self.alarms = {
            'Monday': None,
            'Tuesday': None,
            'Wednesday': None,
            'Thursday': None,
            'Friday': None,
            'Saturday': None,
            'Sunday': None,
        }
        
        

    def set_alarm(self, day: str, time: dt.time):
        self.alarms[day] = time


if __name__ == '__main__':
    m = AlarmManager()
    [print(f'{d:10}: {t}') for (d, t) in m.alarms.items()]