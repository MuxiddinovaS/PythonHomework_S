
#Create a list containing five different fruits and print the third fruit.
my_list = [ "banana", "apple", "pineapple", "grape", "peach"]
print(my_list[2])


#Create two lists of numbers and concatenate them into a single list.
l1= [1,2,3,4]
l2= [5,6,7,8]
combined = l1+l2
print(combined)


#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [10, 20, 30, 40, 50]

first = numbers[0]
middle_index = len(numbers) // 2
middle = numbers[middle_index]
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)


#Create a list of your five favorite movies and convert it into a tuple.
movies= ["Lovely runner", "Descendants of the sun", "Vincenzo", "Business Proporsal", "Crash Landing on You", "Marry my Husband"]
tuple_m= tuple(movies)
print(tuple_m)


#Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
if "Paris" in cities:
    print("Paris is in the list!")
else:
    print("Paris is not in the list.")



    #Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3]
duplicated = numbers * 2
print(duplicated)


#Given a list of numbers, swap the first and last elements.
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)



#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
t=(1,2,3,4,5,6,7,8,9,10)
sliced = t[3:7]
print(sliced)


#Create a list of colors and count how many times "blue" appears in the list.
colors= ["blue", "yellow", "pink", "white", "blue"]
blue_count = colors.count("blue")
print("Blue appears", blue_count, "times.")


#Given a tuple of animals, find the index of "lion".
animals = ("cat", "dog", "lion", "elephant", "tiger")
lion_index = animals.index("lion")
print("Index of lion:", lion_index)

#Create two tuples of numbers and merge them into a single tuple.

t1= (1,2,3,4)
t2= (5,6,7,8)
combined = t1+t2
print(combined)


#Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30, 40]
my_tuple = (5, 15, 25)
list_length = len(my_list)
tuple_length = len(my_tuple)
print("Length of list:", list_length)
print("Length of tuple:", tuple_length)


#Create a tuple of five numbers and convert it into a list.
t=(1,2,3,4,5)
list= list(t)
print(list)


#Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (12, 45, 7, 89, 23, 5)
maximum = max(numbers)
minimum = min(numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)


#Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "cherry", "date")
reversed_words = words[::-1]
print(reversed_words)



