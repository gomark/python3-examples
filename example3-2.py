import sys
import fibo

print ("Hello world")

i = 1
j = 2
k = i*j
str1 = 'my name is putti'
str2 = ' tang'

print(str1 + ' ' + str2)
sys.stdout.write('.')
sys.stdout.write('.')

print ('last char=' + str1[-1])

for i in range(2, 5):
	print ('i=' + str(i))

def fn1(n):
	print('fn1=' + n)

fn1('Mark')

fibo.fib(10)
print (fibo.__name__)
print ('path=')
print (*sys.path)
print (sys.version_info)
print ('now, my versi')
