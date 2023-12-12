from dataclasses import dataclass

@dataclass()
class Alarm:
    Day: str
    Time: str
    Enabled: bool


def as_alarm(jdict) -> list[Alarm] | object:
    # Check jdict is a Dict with an item 'alarms'
    if 'alarms' not in jdict:
        return jdict
    
    # List Comprehension to convert into a list
    return [Alarm(a['Day'], a['Time'], a['Enabled']) for a in jdict['alarms']]

