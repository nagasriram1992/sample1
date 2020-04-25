import time
def function():
	start = time.time()
	for x in range(1,1000):
		print(x)
	end = time.time()
	print((end - start),'secs')

function()