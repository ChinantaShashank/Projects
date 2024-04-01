def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_alternate_primes(N):
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
        while True:
            if is_prime(num):
                break
            num += 1
    print()
N = int(input("Enter the value of N: "))
print("Output:")
print_alternate_primes(N)
