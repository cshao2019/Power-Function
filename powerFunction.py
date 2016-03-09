#Function
def power(base,exponent): 
	answer = base 
	multiplyTimes = 1 
	#condition to check how many times base is multiplied with itself
	while exponent > multiplyTimes: 
		multiplyTimes += 1
		answer = answer * base 
	return answer

#Need a loop
#need a condition when multiply times == exponent then stop and then 
#print the result in the main program
