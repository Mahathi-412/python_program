def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
d, p = map(int, input().split())  
n = d // p 
op = 0  
for i in range(1, n + 1):
    valid_prime = True  
    for part in range(1, p):  
        equivalent_hour = i + part * n
        if not is_prime(equivalent_hour):
            valid_prime = False 
            break
    if valid_prime and is_prime(i):
        op += 1
print(op)
