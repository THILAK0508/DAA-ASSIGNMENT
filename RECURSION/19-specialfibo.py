def compute_f(a, b, n):
    if n == 0:
        return a
    elif n == 1:
        return b
    
    f_prev1 = a
    f_prev2 = b
    
    for i in range(2, n + 1):
        f_current = f_prev1 ^ f_prev2
        f_prev1 = f_prev2
        f_prev2 = f_current
    
    return f_prev2

T = int(input().strip()) 

results = []

for _ in range(T):
    a, b, n = map(int, input().strip().split())
    result = compute_f(a, b, n)
    results.append(result)

for result in results:
    print(result)
