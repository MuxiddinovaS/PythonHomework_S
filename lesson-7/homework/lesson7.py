
def is_prime(n):
    if n < 2:  # 0 va 1 tub emas
        return False
    for i in range(2, int(n**0.5) + 1):  # faqat kvadrat ildizgacha tekshiramiz
        if n % i == 0:
            return False
    return True

print(is_prime(4))  # False
print(is_prime(7))  # True


def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print(digit_sum(24))   # 6
print(digit_sum(502))  # 7




def powers_of_two(n):
    k = 1
    while 2 ** k <= n:
        print(2 ** k, end=' ')
        k += 1

powers_of_two(10)  # 2 4 8

