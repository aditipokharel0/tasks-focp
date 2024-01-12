def findfactors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

check = 36
result = findfactors(check)

print(f"The factors of {check} are: {result}")
