def decorator_func(f):
	def wrapper(num,den):
		try:
			if(den==0):
				raise Exception("Division by zero")
			result = f(num,den)
			print(result)
		except Exception as e:
			print(e)
	return wrapper
	
			
@decorator_func
def divide(numerator,denominator):
	result = numerator/denominator
	return result

n1 = int(input("Enter numerator"))
n2 = int(input("Enter denominator"))
divide(n1,n2)
