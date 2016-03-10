#Function
def power(base,exponent): 
	if exponent == 0:
		return 1 
	answer = base 
	multiplyTimes = 1 
	#condition to check how many times base is multiplied with itself
	while exponent > multiplyTimes: 
		multiplyTimes += 1
		answer = answer * base 
	return answer

#---Main Program---

base = int(raw_input("Enter a base number: "))
exponent = int(raw_input("Enter an exponent number: "))

#special case
if base == 0 and exponent == 0: 
	print("That is undefined.")
	exit()

else: #normal operations
	answer = power(base,exponent) #calling the function
	print("Your answer is {}.".format(answer))

#Need a loop
#need a condition when multiply times == exponent then stop and then 
#print the result in the main program