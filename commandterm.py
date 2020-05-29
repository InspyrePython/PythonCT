
import time
def clear():
	import os
	os.system('clear')
clear()
print('================PyOS Command Terminal=================')
command = input('--PyOS user ')
if command == 'install python3 inspyre':
	f = open('packer.pyosl.txt', 'a')
	f.write('[app]\n\t[lock]\n\t\t{inspyre: \n\t\t"state" = "coding"} [un-lock]\n\t [un-app]')
	try:
		clear()
		import sys
		print('Installing Inspyre..')
		for i in range(1, 11):
			import time
			j=9-i
			time.sleep(1)
			sys.stdout.write('[' + '#'*i + ' '*j + ']')
			sys.stdout.write('\u001b[1000D')
			sys.stdout.flush()
	except KeyboardInterrupt:
		clear()
		pass
elif command == 'api wikipedia.open fetch:all':
	import requests
	wikiwire = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Pet_door&rvslots=*&rvprop=content&formatversion=2&format=json')
	wikiresponse = wikiwire.json()
	print(wikiresponse)
	time.sleep(3)
	import os
	os.system('clear')
else:
	print('Unknown Command. Try again?')
	pass