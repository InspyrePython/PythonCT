
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
		exec(open('fightgame.py', 'r').read())
		pass
	elif app == 'B':
		import os
		os.system('clear')
		exec(open('ballcollecter.py', 'r').read())
		pass
	elif app == 'W':
		import os
		os.system('clear')
		exec(open('wordbomb.py', 'r').read())
		pass
except KeyboardInterrupt:
	import os
	os.system('clear')
	pass