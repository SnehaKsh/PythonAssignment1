#code to find out numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

final=[]
for x in range(1500, 2700):
    if (x%7 == 0) and (x%5 ==0):
        final.append(x)
print(final)
