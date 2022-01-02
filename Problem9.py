# Python program to print all Prime numbers in an Interval

lower=int(input("Enter the lower number : "))
upper=int(input("Enter the upper number : "))
print("The prime numbers given in this interval are : ")

for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num-1):
            if (num%i ==0):
                break
        else:
            print(num)
