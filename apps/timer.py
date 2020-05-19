
import time
import sys
i = 0
import time, sys
TimerAppOpened = True
while TimerAppOpened:
	try:
		i+=1
		time.sleep(1)
		sys.stdout.write(u"\u001b[1000D")
		sys.stdout.flush()
		time.sleep(1)
		sys.stdout.write(str(i))
		sys.stdout.flush()
	except KeyboardInterrupt:
		TimerAppOpened=False
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
