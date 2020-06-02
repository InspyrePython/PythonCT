
import getkey
pass
try:
	print('=====Game Hub=====')
	print('[F] Fight Game')
	print('[B] Ball Collecter')
	print('[W] Word Bomb')
	app = getkey.getkey().upper()
	if app == 'F':
		import os
		os.system('clear')
		import fightgame
		pass
	elif app == 'B':
		import os
		os.system('clear')
		import ballcollecter
		pass
	elif app == 'W':
		import os
		os.system('clear')
		import wordbomb
		pass
except KeyboardInterrupt:
	import os
	os.system('clear')
	pass