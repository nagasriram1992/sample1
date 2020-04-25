try:
 a = int(input('Enter a:'))
 b = int(input('Enter b:'))
 c = a/b
except ZeroDivisionError:
 print('b value should not be zero')
except ValueError:
 print('b value should be integer')
else:
 print(c)
finally:
 print('finally gets excuted anyways')
