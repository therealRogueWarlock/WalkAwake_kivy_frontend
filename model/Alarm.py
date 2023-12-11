from dataclasses import dataclass

@dataclass()
class Alarm:
    Day: str
    Time: str
    Enabled: bool


# =============
# |  Testing  |
# =============
if(__name__ == '__main__'):
    test_obj = Alarm('Monday', '21:00', True)
    print(test_obj.__dict__)