def pro(n):
    if n==0:
        return 1
    return (n%10) * pro(n//10)
print(pro(342))