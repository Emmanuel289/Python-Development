def fib(n):
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b

print 'The fibonnacci sequence upper bounded by 3000 is', fib(3000) \
