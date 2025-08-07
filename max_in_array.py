num = [2,5,4,7,9,5,44,2,3,43,]
min = num[0]
max = num[0]
for i in range (len(num)):
    if num[i] > max:
        max = num[i]
    elif num[i] < min:
        min = num[i]
print("min : ",min)
print("max : ",max)