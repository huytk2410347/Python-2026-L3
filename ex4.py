n = int(input("Enter a number: "))
result = 0 # sum all divisors
for i in range(1, n):
    if n % i == 0:
     result += i
if result == n:
    print(n, "is a perfect number.")
else:
    print(n, "is not a perfect number.")