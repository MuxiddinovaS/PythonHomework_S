#Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.
def modify_string(txt):
    result = []
    i = 0
    count = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        # Вставляем _ только после каждых трёх символов
        if count == 3:
            # Если текущий символ — гласная или следующий уже содержит "_", сдвигаем подчёркивание
            if txt[i] in "aeiou" or (i + 1 < len(txt) and txt[i+1] == "_"):
                pass  # ждём
            elif i != len(txt) - 1:
                result.append("_")
                count = 0
        i += 1

    # Удаляем подчёркивание в конце, если оно случайно попало
    if result and result[-1] == "_":
        result.pop()

    return ''.join(result)

print(modify_string("hello"))          # hel_lo
print(modify_string("assalom"))        # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef

#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input())
for i in range(n):
    print(i ** 2)

 #Print first 10 natural numbers using a while loop
k=1
while k <= 10:
    print(k)
    k += 1

#Print the following pattern
#1
#1 2
#1 2 3
# 2 3 4
#1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Calculate sum from 1 to n:

n = int(input("Enter number: "))
total = sum(range(1, n + 1))
print("Sum is:", total)

#Print multiplication table of a given number
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)


#Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)

        
        
#Count the total number of digits in a number
num = int(input())
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)


#Print reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


#Print list in reverse:
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)


#Numbers from -10 to -1:
for i in range(-10, 0):
    print(i)


#Message "Done":
for i in range(5):
    print(i)
else:
    print("Done!")


#Prime numbers between 25–50:
for num in range(25, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


#Fibonacci sequence (10 terms):
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b


#Factorial of number:
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")



#Return Uncommon Elements of Lists
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
        elif c1[elem] > c2[elem]:
            result.extend([elem] * (c1[elem] - c2[elem]))

    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
        elif c2[elem] > c1[elem]:
            result.extend([elem] * (c2[elem] - c1[elem]))

    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]


