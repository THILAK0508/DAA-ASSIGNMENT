def count_zeros(num):
    if num == 0:
        return 1
    
    if num < 10:
        return 0
    
    last_digit = num % 10
    
    zeros_in_remaining = count_zeros(num // 10)

    if last_digit == 0:
        return zeros_in_remaining + 1
    else:
        return zeros_in_remaining
num = 10203040
print("Number of zeros : ",count_zeros(num))
