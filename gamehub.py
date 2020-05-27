
import getkey
gamehub = True
while gamehub:
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
		elif app == 'B':
			import os
			os.system('clear')
			import ballcollecter
		elif app == 'W':
			import os
			os.system('clear')
			import wordbomb
	except KeyboardInterrupt:
		import os
		os.system('clear')
		gamehub = False
		pass