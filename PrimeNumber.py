import math

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers in the range:")

for num in range(start, end + 1):
    if num < 2:
        continue
    prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
