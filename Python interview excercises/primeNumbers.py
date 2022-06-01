def isPrimeNumber(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(isPrimeNumber(5))

print(isPrimeNumber(2))