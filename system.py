
import bloodyterminal as bs
import time, os, requests
print('PythonOS Login')

def play(filename, time):
	import replit
	music = replit.audio.play(filename)
	playing = True
	while playing:
		try:
			import time
			music.paused = False
			time.sleep(3)
			music.paused = True
			playing = False
		except replit.json.decoder.JSONDecodeError:
			pass
		except BrokenPipeError:
			pass
		except replit.NoSuchPlayerException:
			pass
user = input('Username: ')
password = input('Password: ')
print('Logging in..')
time.sleep(2)
os.system('clear')
print('Checking login...')
bs.btext.success('')
print('Checking network...')
time.sleep(2)
a = requests.get('https://www.google.com/').status_code
if a == 200 and os.cpu_count() > 3:
	bs.btext.success('Succeeded all tests.')
	pass;
elif os.cpu_count() < 3:
	bs.btext.warning('Failed processing.')
	pass;
elif a != 200:
	bs.btext.warning('Failed network connect.')
	pass;
else:
	bs.btext.error('Failed all tests. Trying again..')
	pass;

