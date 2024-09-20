def is_prime(func):
    def prime(*args):
        result = func(*args)
        if result < 2:
            print('Составное')
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print('Составное')
        print('Простое')
        return result
    return prime


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)