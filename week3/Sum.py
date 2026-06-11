sum = 0

for i in range(1,11):
    sum += i
    if i < 10:
        print(i, end=" ")
    else:
        print(1, end=" ")

print(sum)