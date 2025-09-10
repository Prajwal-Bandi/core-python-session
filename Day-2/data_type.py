# Data type :
# File handling : input and output operation


words_str = input("Words (space separated):")
words_list = words_str.split()
words_tuple = tuple(words_list)
print(words_str)
print(words_list)
print(words_tuple)

file_name = 'words.txt'
with open(file_name, 'w') as writer:
    writer.write(f'List: {words_list}\n')
    writer.write(f'Tuple: {words_tuple}')

with open(file_name, 'r') as reader:
    line_list = reader.readline()
    line_tuple = reader.readline()
    print(line_list)
    print(line_tuple)
    
numbers_str = input("Numbers (space separated):")
numbers_list = [int(num_str) for num_str in numbers_str.split()]
print(numbers_list)
num_sum = sum(numbers_list)
num_avg = num_sum / len(numbers_list)
print(num_sum)
print(num_avg)

file_name = 'numbers_data.txt'
with open(file_name, 'w') as writer:
    writer.write(f'List: {numbers_list}\n')
    writer.write(f'Sum: {num_sum}\n')
    writer.write(f'Average: {num_avg}')

with open(file_name, 'r') as reader:
    line_list = reader.readline()
    line_sum = reader.readline()
    line_avg = reader.readline()
    print(line_list)
    print(line_sum)
    print(line_avg)
    


sentence = input("Sentence:")
sentence_list = sentence.split()
sentence_tuple = tuple(string.upper() for string in sentence_list)

file_name = "sentence.txt"
with open(file_name,'w') as writer:
  writer.write(f'list: {sentence_list}\n')
  writer.write(f'tuple: {sentence_tuple}\n')
with open(file_name,'r') as reader:
  list_line = reader.readline()
  tuple_line = reader.readline()




names_str = input("Please enter names separated by spaces: ")
names_list = names_str.split()
names_list.sort()
names_tuple = tuple(names_list)


file_name = 'names_data.txt'
with open(file_name, 'w') as writer:
 writer.write(f'Sorted Names List: {names_list}\n')
 writer.write(f'Names Tuple: {names_tuple}\n')
 print(f"\nData successfully saved to '{file_name}'.")


with open(file_name, 'r') as reader:
 read_list_line = reader.readline().strip()
 read_tuple_line = reader.readline().strip()
 print(read_list_line)
 print(read_tuple_line)

