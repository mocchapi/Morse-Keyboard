from msvcrt import getch
import winsound
import time
global alphabet
global alphabet_letters
alphabet = [10111, 111010101, 11101011101, 1110101, 1, 101011101, 111011101, 1010101, 101, 1011101110111, 111010111, 101110101, 1110111, 11101, 11101110111, 10111011101, 1110111010111, 1011101, 10101, 111, 1010111, 101010111, 101110111, 11101010111, 1110101110111, 11101110101]
alphabet_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','s','u','v','x','y','z']

def beeper(int_in, unit=100, frequency=600, space=False):
	if space == True:
		for idx,_ in enumerate(range(7)):
			print(round(idx/7*100,2),"%")
			time.sleep(unit*7/1000)
		print("100.0 %")
		print("---")
		return
	bits = list(filter(None,str(int_in).replace("0","s0s").split("s")))
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
	key = ord(getch())
	try:
		if 96<key<123:
			key = key-97
			print(alphabet_letters[key])
			beeper(alphabet[key])
		elif key == 32:
			print("space")
			beeper(0,space=True)
		else:
			print("not in range")
	except Exception as e:
		raise e
