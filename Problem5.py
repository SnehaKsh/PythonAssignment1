# Python Program for simple interest

principal = int(input("The principal amount is : "))
rate = int(input("The rate per annum is : "))
years = int(input("The interest for a number of years is : "))

interest = (principal*rate*years)/100
total_amount= principal + interest
print("The interest is : ", interest)
print("The total amount is : ", total_amount)
