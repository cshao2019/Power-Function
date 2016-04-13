#Integer Input
def int_input(question):
	answer = raw_input(question)
	try:
		return int(answer)
	except ValueError:
		return int_input(question)
		
#Float input
def float_input(question):
	answer = raw_input(question)
	try:
		return float(answer)
	except ValueError:
		return float_input(question)
	
#Recursive power function
def recursive_power_function(base, exponent):
	if exponent == 0:
		return 1
	return base * recursive_power_function(base, exponent -1)	
	

