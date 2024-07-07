def stringlen(n):
   if n =="":
      return 0
   return 1+stringlen(n[1:])
x = "THILAK"
print(stringlen(x))