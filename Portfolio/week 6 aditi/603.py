def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
check = 17 
result = isprime(check)

if result:
    print(f"{check} is a prime number.")
else:
    print(f"{check} is not a prime number.")
