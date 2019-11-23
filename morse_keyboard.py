from msvcrt import getch
import winsound
import time
from collections import OrderedDict
alphabet_dict = {
    "a": "10111",
	"b": "111010101",
	"c": "11101011101",
	"d": "1110101",
	"e": "1",
	"f": "101011101",
	"g": "111011101",
	"h": "1010101",
	"i": "101",
	"j": "1011101110111",
	"k": "111010111",
	"l": "101110101",
	"m": "1110111",
	"n": "11101",
	"o": "11101110111",
	"p": "10111011101",
	"q": "1110111010111",
	"r": "1011101",
	"s": "10101",
	"t": "111",
	"u": "1010111",
	"v": "101010111",
	"w": "101110111",
	"x": "11101010111",
	"y": "1110101110111",
	"z": "11101110101",
	" ": "0000000"
}

def beeper(inpt, unit=75, frequency=600):
	bits = list(filter(None,str(inpt).replace("0","s0s").split("s")))
	for idx, x in enumerate(bits):
		print(round(idx/len(bits)*100,2),"%")
		try:
			if x == "0":
				time.sleep(unit/1000)
			elif len(x) == 1:
				winsound.Beep(frequency,unit)
			else:
				winsound.Beep(frequency,unit*3)
		except BaseException as e:
			print(e)
			return e
	print("100.0 %")
	print("---")
	time.sleep(unit/1000*3)

while True:
	key = str(getch(), "ascii")
	try:
		if key in alphabet_dict.keys():
			print(key)
			beeper(alphabet_dict[key])
		else:
			print("not in range")
	except Exception as e:
		raise e
