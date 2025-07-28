p = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
}

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


def get_primes(count):
    if count < 2:
        return set()

    is_prime = [True] * (count + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= count):
        if is_prime[p]:
            for i in range(p * p, count + 1, p):
                is_prime[i] = False
        p += 1
