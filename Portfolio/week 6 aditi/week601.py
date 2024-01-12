def convertbinary(m):
    a=[]
    n=int(m)
    while n!=0:
        a.append(n%2)
        n=n//2
    a.reverse()
    return a
print(*convertbinary(14))