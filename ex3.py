n = int(input("Enter a number: "))  
Prime = True
for i in range(2, n):
        if n % i == 0:
            Prime = False
            break
if Prime:
    print (n,"is a prime number")
else:
    print(n,"is a not prime number")

 
