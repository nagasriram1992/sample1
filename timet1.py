import time
import itertools
try:
	start = time.time()
	for m,s in itertools.product(range(0,60),range(0,60)):
			time.sleep(1)
			print(m,':',s)
except KeyboardInterrupt:
	end = time.time()
	print(end - start)
finally:
	print('Done')


	# this code is not for stop watch