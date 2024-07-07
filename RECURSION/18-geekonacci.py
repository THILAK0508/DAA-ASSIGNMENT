def disp(a, b, c, n):
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c
    else:
        return disp(a, b, c, n-1) + disp(a, b, c, n-2) + disp(a, b, c, n-3)

T = int(input())

for _ in range(T):
    inputs = input().split()
    a = int(inputs[0])
    b = int(inputs[1])
    c = int(inputs[2])
    n = int(inputs[3])

    print(disp(a, b, c, n))
