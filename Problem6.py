# Python Program for compound interest

principal = int(input("The principal amount is : "))
rate = int(input("The rate per annum is : "))
years = int(input("The interest for a number of years is : "))

total_amount = principal* (1+ (rate/100))**years
interest= total_amount - principal 
print("The interest is : ", int(interest))
print("The total amount is : ", int(total_amount))
