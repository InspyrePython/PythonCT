
from colorama import Fore, Style
try:
	print('Welcome to PythonOS Dev Edition.')
	print('Apps: ')
	print('[I] Open PythonOS\' code editor.')
	print('[C] Calculator App.')
	print('Get PythonOS for your team:' +  Fore.BLUE, 'https://docs.google.com/forms/d/e/1FAIpQLScC1Y2yw58kS0RPRXnDL130Gq6sZQqOUI92JoHlzWqYGc9Htw/viewform')
	app = input(' ')
	if app == 'I':
		import inspyre
	elif app == 'C':
		import calculator
except KeyboardInterrupt:
	print(Style.RESET_ALL, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	
