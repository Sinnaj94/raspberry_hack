import math
import time
import subprocess

def triggerLamp(key,id,state):
	state_written = "off"
	if state:
		state_written = "on"
	print("Triggering lamp " + str(id) + " from key " + str(key) + " " + str(state_written))
	#TODO: insert hack here
	subprocess.call("python steckdose.py " + str(id) + " " + str(state) + " " + str(key), shell=True)

#returns an array of all keys
def getAllKeys():
	_return = []
	start = 0
	for x in range(0,pow(2,5)):
		_return.append(toBin(x))
	return _return

def toBin(number):
	_return = list("00000")
	while(number > 0):
		#logarithm to base of 2
		base = int(math.floor(math.log(number,2)))
		_return[base] = '1'
		number = number - pow(2,base)
	_return = _return[::-1]
	_return = ''.join(_return)
	return _return

def hackTheShit():
	_keys = getAllKeys()
	_lamps = [1,2,4]
	_state = 0
	while(True):
		for _key in _keys:
			for _lamp in _lamps:
				triggerLamp(_key, _lamp, _state)
				time.sleep(.3)
		if _state == 1:
			_state = 0
		else:
			_state = 1

#triggerLamp("00000","1", True)
hackTheShit()

