def multiply(x,y):
    if y == 0:
        return 0
    elif y > 0:
        return x + multiply(x, y - 1)
    else:
        return -multiply(x, -y)
x,y=9,8
ans=multiply(x,y)
print(ans)