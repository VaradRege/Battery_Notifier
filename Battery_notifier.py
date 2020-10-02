# pip install py-notifier
from pynotifier import Notification

# pip install psutil
import psutil

# psutil.sensors_battery() will return the information related to the battery
battery = psutil.sensors_battery()

# battery.percent will return the current battery percentage
percent = battery.percent

# Notification(title, description, duration) -- to send notification to desktop
Notification("Battery Percentage",
             str(percent)+ "% Percent Remaining",
             duration=10).send()


























