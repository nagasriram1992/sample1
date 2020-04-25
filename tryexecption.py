try:
 z = int(input('Enter a:'))
 b = int(input('Enter b:'))
 c = a/b
 print('z = ', z)
 l = [1,2,3]
 printl([3])
except ZeroDivisionError:
 print('b value should not be zero')
except ValueError:
 print('b value should be integer')
except :
 print('invalid list error')
 print('after try')
