
#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
a= 2/0
print(a)


#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def get_integer_input():
    user_input = input("Enter an integer: ")
    if not user_input.strip().lstrip('-').isdigit():
        raise ValueError("Invalid input! Not an integer.")
    return int(user_input)

try:
    number = get_integer_input()
    print(f"You entered the integer: {number}")
except ValueError as e:
    print(f"Error: {e}")


    #Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.


    def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Prompt the user for a file name
filename = input("Enter the file name to open: ")
open_file(filename)

#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

def get_number(prompt):
    value = input(prompt)
    try:
        # Try converting to float (works for int and float)
        return float(value)
    except ValueError:
        raise TypeError(f"Invalid input '{value}'. Expected a numerical value.")

try:
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"You entered: {num1} and {num2}")
except TypeError as e:
    print(f"Error: {e}")

#Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

def open_file_with_permission_check(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except PermissionError:
        print(f"Error: Permission denied to access the file '{filename}'.")

# Prompt the user for a file name
filename = input("Enter the file name to open: ")
open_file_with_permission_check(filename)






#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

# Define a sample list
my_list = [10, 20, 30, 40, 50]

try:
    # Ask the user for an index
    index = int(input("Enter an index to access the element in the list: "))
    
    # Try to access and print the element at the given index
    print(f"The element at index {index} is {my_list[index]}")
    
except IndexError:
    print("Error: The index you entered is out of range.")
    
except ValueError:
    print("Error: Please enter a valid integer index.")


#Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    # Prompt user to enter a number
    number = float(input("Please enter a number: "))
    print(f"You entered: {number}")

except KeyboardInterrupt:
    print("\nInput cancelled by user (KeyboardInterrupt).")

except ValueError:
    print("Invalid input. Please enter a valid number.")



#Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    # Prompt the user to enter two numbers
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    # Perform the division
    result = numerator / denominator
    print(f"The result of the division is: {result}")

except ArithmeticError as e:
    print(f"Arithmetic error occurred: {e}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")



#Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.


filename = input("Enter the filename to open: ")

try:
    # Try opening the file with default encoding (usually 'utf-8')
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")

except UnicodeDecodeError:
    print("Error: Unable to decode the file. There may be an encoding issue.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")


     
     #Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

my_list = [1, 2, 3, 4, 5]

try:
    # Attempting to call a non-existent method 'sort_descending' (this will raise AttributeError)
    my_list.sort_descending()
    
except AttributeError as e:
    print(f"AttributeError: {e}")
    print("Hint: You might be trying to use a method that doesn't exist for list objects.")



#Write a Python program to read an entire text file.

# Prompt the user for the filename
filename = input("Enter the filename to read: ")

try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()  # Read the entire file content
        print("\nFile Content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")




#Write a Python program to read first n lines of a file.

# Prompt the user for the filename and number of lines to read
filename = input("Enter the filename to read: ")
try:
    n = int(input("Enter the number of lines to read: "))

    with open(filename, 'r') as file:
        print(f"\nFirst {n} lines of the file:\n")
        for i in range(n):
            line = file.readline()
            if not line:
                print("[End of file reached]")
                break
            print(line, end='')

except FileNotFoundError:
    print("Error: The file was not found.")

except ValueError:
    print("Error: Please enter a valid number for the number of lines.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")


#Write a Python program to append text to a file and display the text.

# Prompt user for filename
filename = input("Enter the filename to append text to: ")

# Prompt user for text to append
text_to_append = input("Enter the text you want to append: ")

try:
    # Open the file in append mode and write the new text
    with open(filename, 'a') as file:
        file.write(text_to_append + '\n')  # Append with a newline

    # Now open the file again in read mode to display the content
    with open(filename, 'r') as file:
        content = file.read()
        print("\nUpdated File Content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")




#Write a Python program to append text to a file and display the text.

# Prompt user for filename
filename = input("Enter the filename to append text to: ")

# Prompt user for text to append
text_to_append = input("Enter the text you want to append: ")

try:
    # Open the file in append mode and write the new text
    with open(filename, 'a') as file:
        file.write(text_to_append + '\n')  # Append with a newline

    # Now open the file again in read mode to display the content
    with open(filename, 'r') as file:
        content = file.read()
        print("\nUpdated File Content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")




#Write a Python program to read last n lines of a file.

# Prompt the user for the filename and number of lines to read
filename = input("Enter the filename: ")

try:
    n = int(input("Enter the number of last lines to read: "))

    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

        # Get the last n lines using slicing
        last_lines = lines[-n:]

        print(f"\nLast {n} lines of the file:\n")
        for line in last_lines:
            print(line, end='')

except FileNotFoundError:
    print("Error: The file was not found.")

except ValueError:
    print("Error: Please enter a valid number.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to read a file line by line and store it into a list.

# Prompt the user for the filename
filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        # Read lines and store them in a list
        lines_list = [line.strip() for line in file]

    print("\nLines stored in the list:\n")
    print(lines_list)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to read a file line by line and store it into a variable.

# Prompt the user for the filename
filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        # Read lines one by one and store them in a single string variable
        content = ""
        for line in file:
            content += line  # line already contains newline characters

    print("\nFile content stored in a variable:\n")
    print(content)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to read a file line by line and store it into an array.

# Prompt the user for the filename
filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        # Read each line and store it in a list (array), stripping newlines
        lines_array = [line.strip() for line in file]

    print("\nLines stored in the array (list):\n")
    print(lines_array)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")




#Write a Python program to find the longest words.

# Prompt the user for the filename
filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        words = file.read().split()  # Split the content into words

        # Find the length of the longest word(s)
        max_length = max(len(word) for word in words)
        
        # Get all words that match the max length
        longest_words = [word for word in words if len(word) == max_length]

    print(f"\nLongest word length: {max_length}")
    print("Longest word(s):")
    for word in longest_words:
        print(word)

except FileNotFoundError:
    print("Error: The file was not found.")

except ValueError:
    print("Error: The file is empty or has no valid words.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")




#Write a Python program to count the number of lines in a text file.

# Prompt the user for the filename
filename = input("Enter the filename to count lines: ")

try:
    with open(filename, 'r') as file:
        # Count lines using a generator expression
        line_count = sum(1 for line in file)

    print(f"\nThe file contains {line_count} lines.")

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to count the frequency of words in a file.

from collections import Counter
import re

# Prompt the user for the filename
filename = input("Enter the filename to analyze: ")

try:
    with open(filename, 'r') as file:
        text = file.read().lower()  # Read and convert to lowercase

        # Remove punctuation and split into words
        words = re.findall(r'\b\w+\b', text)

        # Count word frequencies
        word_freq = Counter(words)

    print("\nWord frequencies:\n")
    for word, count in word_freq.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")




#Write a Python program to get the file size of a plain file.

import os

# Prompt the user for the filename
filename = input("Enter the filename: ")

try:
    # Get the file size in bytes
    file_size = os.path.getsize(filename)
    print(f"\nThe size of '{filename}' is {file_size} bytes.")

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to write a list to a file.

# Sample list
my_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Prompt the user for the output filename
filename = input("Enter the filename to write the list to: ")

try:
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(item + '\n')

    print(f"\nList has been written to '{filename}' successfully.")

except Exception as e:
    print(f"An error occurred: {e}")



#Write a Python program to copy the contents of a file to another file.

# Prompt the user for source and destination filenames
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()  # Read the entire content

    with open(destination_file, 'w') as dest:
        dest.write(content)  # Write the content to the new file

    print(f"\nContents of '{source_file}' have been copied to '{destination_file}' successfully.")

except FileNotFoundError:
    print("Error: The source file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to combine each line from the first file with the corresponding line in the second file.

# Prompt the user for both filenames
file1 = input("Enter the first filename: ")
file2 = input("Enter the second filename: ")

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Use zip to combine corresponding lines
        for line1, line2 in zip(f1, f2):
            combined = line1.strip() + " " + line2.strip()
            print(combined)

except FileNotFoundError:
    print("Error: One or both files were not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to read a random line from a file.

import random

# Prompt the user for the filename
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("The file is empty.")
    else:
        random_line = random.choice(lines)
        print("\nRandom line from the file:")
        print(random_line.strip())

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to assess if a file is closed or not.

# Prompt the user for the filename
filename = input("Enter the filename to open: ")

try:
    file = open(filename, 'r')  # Open the file

    # Check if the file is closed
    print(f"Is the file closed? {file.closed}")  # Should print False

    file.close()  # Now close the file

    # Check again
    print(f"Is the file closed after closing? {file.closed}")  # Should print True

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



#Write a Python program to remove newline characters from a file.

# Prompt the user for the input filename
input_file = input("Enter the filename to read and remove newlines: ")

# Prompt for an output file name (optional)
output_file = input("Enter the filename to save cleaned content (or leave blank to just display): ")

try:
    with open(input_file, 'r') as file:
        content = file.read()

    # Remove newline characters
    cleaned_content = content.replace('\n', '')

    if output_file:
        with open(output_file, 'w') as outfile:
            outfile.write(cleaned_content)
        print(f"\nNewlines removed and content written to '{output_file}'.")
    else:
        print("\nCleaned content (no newlines):\n")
        print(cleaned_content)

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")





#Write a Python program that takes a text file as input and returns the number of words in a given text file.

#Note: Some words can be separated by a comma with no space.


import re

# Prompt the user for the filename
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        text = file.read()

        # Use regex to split on any non-word character (spaces, commas, periods, etc.)
        words = re.findall(r'\b\w+\b', text)

        word_count = len(words)

    print(f"\nTotal number of words in '{filename}': {word_count}")

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")





#Write a Python program to extract characters from various text files and put them into a list.

import os

# Prompt the user to enter filenames separated by commas
filenames = input("Enter the filenames (separated by commas): ").split(',')

# List to store all characters
all_characters = []

for fname in filenames:
    fname = fname.strip()  # Remove any extra spaces
    try:
        with open(fname, 'r') as file:
            content = file.read()
            # Extend the list with each character from the file
            all_characters.extend(list(content))
    except FileNotFoundError:
        print(f"Error: File '{fname}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{fname}': {e}")

# Display the result
print("\nExtracted characters from all files:")
print(all_characters)



#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string

# Loop through uppercase letters A to Z
for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    try:
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
        print(f"Created: {filename}")
    except Exception as e:
        print(f"Error creating {filename}: {e}")


#Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string

# Prompt the user for output filename and number of letters per line
filename = input("Enter the filename to create: ")
letters_per_line = int(input("Enter the number of letters per line: "))

try:
    with open(filename, 'w') as file:
        alphabet = string.ascii_lowercase  # or use ascii_uppercase for A–Z
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i+letters_per_line]
            file.write(line + '\n')

    print(f"\nFile '{filename}' created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
