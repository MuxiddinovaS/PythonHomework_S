
#Write a Python script to sort (ascending and descending) a dictionary by value.

#skipped because we didn't cover thiis topic in the lesson


#Write a Python script to add a key to a dictionary.
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)


#Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print(result)


#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = 5
squares = {}
for x in range(1, n+1):
    squares[x] = x * x

print(squares)


#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
squares = {x: x*x for x in range(1, 16)}

print(squares)


#Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}

print("The created set is:", my_set)


#Write a Python program to iterate over sets.
my_set = {10, 20, 30, 40, 50}

print("Elements in the set:")
for item in my_set:
    print(item)


#Write a Python program to add member(s) to a set.

my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6, 7])

print("Updated set:", my_set)

#Write a Python program to remove item(s) from a given set.
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
my_set.discard(10)  
removed_item = my_set.pop()
print("Updated set:", my_set)
print("Randomly removed item:", removed_item)


#Write a Python program to remove an item from a set if it is present in the set.

my_set = {1, 2, 3, 4, 5}
item_to_remove = 3
my_set.discard(item_to_remove)

print("Updated set:", my_set)


