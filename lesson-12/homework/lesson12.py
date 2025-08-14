# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.


import threading

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes(start, end, result):
    """Check primes in the given range and store them in result list."""
    primes = [num for num in range(start, end) if is_prime(num)]
    result.extend(primes)

if __name__ == "__main__":
    start_range = int(input("Enter start of range: "))
    end_range = int(input("Enter end of range: "))
    thread_count = int(input("Enter number of threads: "))

    step = (end_range - start_range) // thread_count
    threads = []
    results = []

    for i in range(thread_count):
        sub_start = start_range + i * step
        sub_end = start_range + (i + 1) * step if i != thread_count - 1 else end_range + 1
        thread = threading.Thread(target=check_primes, args=(sub_start, sub_end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results.sort()
    print(f"Prime numbers between {start_range} and {end_range}:\n{results}")


# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.


import threading
from collections import Counter

def process_lines(lines, counter):
    """Count word occurrences in the given lines."""
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)

if __name__ == "__main__":
    filename = input("Enter file name: ")
    thread_count = int(input("Enter number of threads: "))

    # Read file
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    step = len(lines) // thread_count
    threads = []
    counters = []

    for i in range(thread_count):
        sub_lines = lines[i * step: (i + 1) * step] if i != thread_count - 1 else lines[i * step:]
        thread = threading.Thread(target=process_lines, args=(sub_lines, counters))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Merge results
    final_counter = Counter()
    for c in counters:
        final_counter.update(c)

    print("\nWord Occurrences:")
    for word, count in final_counter.most_common(10):  # Top 10 words
        print(f"{word}: {count}")
