# more improved shotgun

import keyboard
from pynput.mouse import Button, Controller
from time import sleep

def improvise():
    # assult rifle takes ~3.5 seconds to fire a full clip. 

    
    keyboard.send(1928)

#while True:
#    keyboard.press(28)

something = False

m = Controller()


def skill(times=10, interval=0.01):
    for i in range(times):
        keyboard.send(33)
        sleep(interval)

print("Running.")

while 1:
	if keyboard.is_pressed("0E"):
		while something == True:
			skill()
			if keyboard.is_pressed("0E"):
				something == False