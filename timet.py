import time
try:
	start = time.time()
	for m in range(0,60):
		for s in range(0,60):
			time.sleep(1)
			print(m,':',s)
except KeyboardInterrupt:
	end = time.time()
	print(end - start)
finally:
	print('Done')