# Python3 Document 
#project by VaradRege aka Philoshopher 
# Edit By Ayushjd098
#!/usr/bin/env python
import signal
import sys
from pynotifier import Notification
import time
import psutil 

def notify():

	battery = psutil.sensors_battery()

	old_bat = 0 

	while True:
		signal.signal(signal.SIGINT, signal_handler)
# For Future Refrence
# signal.pause()
# time.sleep(900)

		percent = battery.percent

		if percent < old_bat: 
			old_bat = percent - 10
			if percent < 20:
				Notification("Battery Level Reached Critical",
	             str(percent)+ "% Percent Remaining, Please Provide Power.",
	             duration=20).send()

			else:
				Notification("Battery Level Going Down",
				             str(percent)+ "% Percent Remaining",
				             duration=10).send()

		if percent > old_bat:
				Notification("Battery Stable :)",
				             str(percent)+ "% Percent Remaining",
				             duration=5).send()		
		old_bat = percent
		time.sleep(900)



def signal_handler(sig, frame):
	print('Exiting Gracefully...')
	print("Thanks For Using me")
	print("For more info visit: https://github.com/VaradRege/Battery_Notifier")
	sys.exit(0)
	
def starting_screen():
	print("*" * 50)
	print(" ")
	print("Hey,")
	print("This program is gonna moniter your Battery")
	print("By useing it you  accept our Terms & Condiations!")
	print("To stop press Ctrl + C ")
	print(" ")
	print("*" * 50)


if __name__ == '__main__':
	starting_screen()
	notify()
