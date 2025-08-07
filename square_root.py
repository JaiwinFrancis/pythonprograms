def root(n):
    i = 1
    while i * i <= n:
        i = i + 1
    return i - 1
num =  int(input("Enter a number : "))
result = root(num)
print("Number : ", result)