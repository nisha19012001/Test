def decorator_func(f):
	def wrapper(num,den):
		try:
			print("Entering inside decorator function")
			if(den==0):
				raise Exception("Division by zero")
			result = f(num,den)
			print(result)
		except Exception as e:
			print(e)
	return wrapper
	
			
@decorator_func
def divide(numerator,denominator):
	print("Entering inside actual function")
	result = numerator/denominator
	return result

n1 = int(input("Enter numerator"))
n2 = int(input("Enter denominator"))
divide(n1,n2)
