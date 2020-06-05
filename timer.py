
import time
import sys
i = 0
import time, sys
TimerAppOpened = True
j=0
while TimerAppOpened:
	try:
		i+=1
		time.sleep(1)
		sys.stdout.write(u"\u001b[1000D")
		sys.stdout.flush()
		sys.stdout.write(f'{j} minutes and {i} seconds.')
		sys.stdout.flush()
		if i == 59:
			j+=1
			i=0
			continue
	except KeyboardInterrupt:
		TimerAppOpened=False
		import os
		os.system('clear')
		pass
