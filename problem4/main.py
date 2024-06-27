def generate_primes_grid(width, height, start):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(n):
        while True:
            n += 1
            if is_prime(n):
                return n

    primes = []
    current = start
    while len(primes) < width * height:
        current = next_prime(current)
        primes.append(current)

    result = ""
    for i in range(height):
        row = primes[i * width:(i + 1) * width]
        result += " ".join(f"{num:2}" for num in row) + "\n"

    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """