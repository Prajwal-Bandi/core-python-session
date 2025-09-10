'''Problem 1
Write a Python program that:

Accepts a sequence of words from the user in a single line (separated by spaces).
Stores the words in both a list and a tuple.
Displays the list and tuple on the screen.
Saves the list and tuple into a text file named qn01_data.txt.
Reads back the saved data from the file and prints it on the screen.'''


def user_words(user_input):
    user_list = user_input.split()
    user_tuple = tuple(user_list)
    return user_list, user_tuple

# Step 1: Accept user input
user_input = input('Enter a sequence of words (space-separated): ')

# Step 2: Get list and tuple
words_list, words_tuple = user_words(user_input)

# Step 3: Display list and tuple
print("List:", words_list)
print("Tuple:", words_tuple)

# Step 4: Write to file
filename = 'qn01_data.txt'
with open(filename, 'w') as file:
    file.write(f'List: {words_list}\n')
    file.write(f'Tuple: {words_tuple}\n')

# Step 5: Read back and display
with open(filename, 'r') as file:
    print("\nData read from file:")
    for line in file:
        print(line.strip())
        

'''Problem 2
Write a Python program that:

Reads a line of integers from the user (separated by spaces).
Stores them in a list and calculates the sum and average.
Saves the list, sum, and average into a text file named numbers_data.txt.
Reads the contents of the file and prints them back to the user.
'''

def process_numbers(user_input):
    numbers = [int(num) for num in user_input.split()]
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return numbers, total, average

user_input = input("Enter a line of integers (space-separated): ")

numbers, total, average = process_numbers(user_input)

filename = 'numbers_data.txt'
with open(filename, 'w') as file:
    file.write(f'Numbers List: {numbers}\n')
    file.write(f'Sum: {total}\n')
    file.write(f'Average: {average:.2f}\n')

print("\nData read from file:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())
        
'''   
Problem 3
Write a Python program that:

Accepts a sentence from the user.
Splits the sentence into words and stores them in a list.
Converts all words to uppercase and stores them in a tuple.
Saves both the list and tuple into a file named sentence_data.txt.
Reads back the data from the file and displays it on the screen.'''

def process_sentence(sentence):
    word_list = sentence.split()
    word_tuple = tuple(word.upper() for word in word_list)
    return word_list, word_tuple

sentence = input("Enter a sentence: ")
words_list, words_tuple = process_sentence(sentence)


print("Word List:", words_list)
print("Uppercase Word Tuple:", words_tuple)


filename = 'sentence_data.txt'
with open(filename, 'w') as file:
    file.write(f"Word List: {words_list}\n")
    file.write(f"Uppercase Word Tuple: {words_tuple}\n")

print("\nData read from file:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())


'''Problem 4
Write a Python program that:

Reads a list of names from the user (separated by spaces).
Sorts the names alphabetically and stores them in a list.
Converts the list into a tuple.
Saves the sorted list and tuple into a file named names_data.txt.
Reads and prints the saved data from the file.
'''


def process_names(input_line):
    name_list = sorted(input_line.split())
    name_tuple = tuple(name_list)
    
    return name_list, name_tuple

names_input = input("Enter a list of names (space-separated): ")

sorted_list, sorted_tuple = process_names(names_input)

print("Sorted List of Names:", sorted_list)
print("Sorted Tuple of Names:", sorted_tuple)

filename = 'names_data.txt'
with open(filename, 'w') as file:
    file.write(f"Sorted List: {sorted_list}\n")
    file.write(f"Sorted Tuple: {sorted_tuple}\n")

print("\nData read from file:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())



'''Problem 5
Write a Python program that:

Accepts a sequence of numbers from the user.
Stores the numbers in a list and finds the maximum and minimum values.
Stores the results (list, max, min) in a file named minmax_data.txt.
Reads and prints the saved data from the file.'''

def process_numbers(input_line):
    number_list = [int(num) for num in input_line.split()]
    max_val = max(number_list) if number_list else None
    min_val = min(number_list) if number_list else None
    
    return number_list, max_val, min_val

user_input = input("Enter a sequence of numbers (space-separated): ")
numbers, max_num, min_num = process_numbers(user_input)

print("Number List:", numbers)
print("Maximum:", max_num)
print("Minimum:", min_num)

# Step 4: Save to file
filename = 'minmax_data.txt'
with open(filename, 'w') as file:
    file.write(f"Number List: {numbers}\n")
    file.write(f"Maximum: {max_num}\n")
    file.write(f"Minimum: {min_num}\n")

print("\nData read from file:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())
