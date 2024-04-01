def power_modulo(a, b, m):
    result = 1  
    a = a % m   
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result
if _name_ == "_main_":
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    m = int(input("Enter the value of m: "))
    result = power_modulo(a, b, m)
    print(f"The result of ({a}^{b} % {m}) is: {result}")