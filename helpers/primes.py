def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_up_to_length(length):
    limit = 10 ** length - 1
    return [n for n in range(2, limit + 1) if is_prime(n)]

# Example: Get primes with up to 2 digits (i.e. primes ≤ 99)
print(primes_up_to_length(10))



def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True
