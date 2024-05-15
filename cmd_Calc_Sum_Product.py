print("********************\n")
print("Cal two number mult and sum\n")
num1 = input("Enter the first number: ")
num1 = int(num1)
num2 = input("Enter the second number: ")
num2 = int(num2)
add = num1+num2
def multiplication_and_sum(num1, num2):
    product = int(num1*num2)
    return product
	
result = multiplication_and_sum(num1, num2)
print("The resultant product is: ", result)
print("The resultant sum is: ", add)
a = input("Press any key to exit")
