# n=int(input("Enter the number"))
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n=n//10
# print(sum)

def sum(n):
    if n==0:
        return 0
    return n%10 + sum(n//10)
print(sum(1423))