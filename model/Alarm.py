from dataclasses import dataclass

@dataclass()
class Alarm:
    Day: str
    Time: str
    Enabled: bool


def as_alarm(jdict):
    if 'alarms' not in jdict:
        return jdict
    
    return [Alarm(a['Day'], a['Time'], a['Enabled']) for a in jdict['alarms']]

# =============
# |  Testing  |
# =============
if(__name__ == '__main__'):
    test_obj = Alarm('Monday', '21:00', True)
    print(test_obj.__dict__)