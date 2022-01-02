# Python program to check whether a number is Prime or not

number=int(input("Enter the number : "))
if number>1:
    for i in range(2, number-1):
        if (number%i==0):
            print("Number is not prime")
            break
    else:
        print("Number is prime")
