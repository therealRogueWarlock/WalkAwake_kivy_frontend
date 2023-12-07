# Home
from .home import Home

# Settings
from .settings import Settings
from .wifi_settings import WifiSettings
from .time_settings import TimeSettings

# Alarms
from .alarms import Alarms
from .set_alarm import SetAlarm
from .set_alarm_for import SetAlarmFor
from .new_alarm import NewAlarm

# Camera
from .camera import Camera

# Setup
Screens = [Home, Settings, WifiSettings, TimeSettings, Alarms, SetAlarm, SetAlarmFor, NewAlarm, Camera]
