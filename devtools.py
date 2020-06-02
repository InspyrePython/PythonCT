
import getkey
from colorama import Fore, Style
devtools = True
while devtools:
	try:
		print('Welcome to PythonOS Dev Edition.')
		print('Apps: ')
		print('[I] Open PythonOS\' code editor.')
		print('🖩 [C] Calculator App.')
		print('[G] Gmail Sender')
		print('Get PythonOS for your team:' +  Fore.BLUE, 'https://docs.google.com/forms/d/e/1FAIpQLScC1Y2yw58kS0RPRXnDL130Gq6sZQqOUI92JoHlzWqYGc9Htw/viewform')
		print(Style.RESET_ALL, ' ')
		app = getkey.getkey().upper()
		if app == 'I':
			import os
			os.system('clear')
			import inspyre
		elif app == 'C':
			import os
			os.system('clear')
			import calculator
		elif app == 'G':
			import os
			os.system('clear')
			import gmail
		else:
			import os
			os.system('clear')
	except KeyboardInterrupt:
		print(Style.RESET_ALL, '')
		import os
		os.system('clear')
		devtools=False
		pass