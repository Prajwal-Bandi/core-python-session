# # Data type :
# # File handling : input and output operation


# words_str = input("Words (space separated):")
# words_list = words_str.split()
# words_tuple = tuple(words_list)
# print(words_str)
# print(words_list)
# print(words_tuple)

# file_name = 'words.txt'
# with open(file_name, 'w') as writer:
#     writer.write(f'List: {words_list}\n')
#     writer.write(f'Tuple: {words_tuple}')

# with open(file_name, 'r') as reader:
#     line_list = reader.readline()
#     line_tuple = reader.readline()
#     print(line_list)
#     print(line_tuple)
    
# numbers_str = input("Numbers (space separated):")
# numbers_list = [int(num_str) for num_str in numbers_str.split()]
# print(numbers_list)
# num_sum = sum(numbers_list)
# num_avg = num_sum / len(numbers_list)
# print(num_sum)
# print(num_avg)

# file_name = 'numbers_data.txt'
# with open(file_name, 'w') as writer:
#     writer.write(f'List: {numbers_list}\n')
#     writer.write(f'Sum: {num_sum}\n')
#     writer.write(f'Average: {num_avg}')

# with open(file_name, 'r') as reader:
#     line_list = reader.readline()
#     line_sum = reader.readline()
#     line_avg = reader.readline()
#     print(line_list)
#     print(line_sum)
#     print(line_avg)
    


# sentence = input("Sentence:")
# sentence_list = sentence.split()
# sentence_tuple = tuple(string.upper() for string in sentence_list)

# file_name = "sentence.txt"
# with open(file_name,'w') as writer:
#   writer.write(f'list: {sentence_list}\n')
#   writer.write(f'tuple: {sentence_tuple}\n')
# with open(file_name,'r') as reader:
#   list_line = reader.readline()
#   tuple_line = reader.readline()




# names_str = input("Please enter names separated by spaces: ")
# names_list = names_str.split()
# names_list.sort()
# names_tuple = tuple(names_list)


# file_name = 'names_data.txt'
# with open(file_name, 'w') as writer:
#  writer.write(f'Sorted Names List: {names_list}\n')
#  writer.write(f'Names Tuple: {names_tuple}\n')
#  print(f"\nData successfully saved to '{file_name}'.")


# with open(file_name, 'r') as reader:
#  read_list_line = reader.readline().strip()
#  read_tuple_line = reader.readline().strip()
#  print(read_list_line)
#  print(read_tuple_line)





# #  Funtion : default and positonal arguments

# def find_salary_sum(first, second, **salaries):
#     result = first + second
#     for key in salaries:
#         result += salaries[key]
#     return result

# print(find_salary_sum(100, 200, John=500, Mary=300))  # Output: 1100



# def find_salary_sum(first, second, *salaries):
#     result = first + second
#     for salary in salaries:
#         result += salary
#     return result

# print(find_salary_sum(100, 200))                  # Output: 300
# print(find_salary_sum(100, 200, 300, 400, 500))   # Output: 1500


# # default arguments
# def find_salary_sum(first,second,bonus=500):
#     result=(first+bonus)+(second+bonus)
#     return result

# print(find_salary_sum(200,400))



# def find_min(salaries):
#     min_salary = salaries[0]
#     for salary in salaries:
#         if salary < min_salary:
#             min_salary = salary 
#     return min_salary 

# def find_max(salaries):
#     max_salary = salaries[0]
#     for salary in salaries:
#         if salary > max_salary:
#             max_salary = salary 
#     return max_salary

# def find_total(salaries):
#     total = 0
#     for salary in salaries:
#         total += salary 
#     return total 
 
# driver code
# salaries = [1000, 3000, 4000, 1500, 2200, 3500]
# min_salary = find_min(salaries)
# max_salary = find_max(salaries)
# total_salary = find_total(salaries)
# print(salaries)
# print(min_salary)
# print(max_salary)
# print(total_salary)


# serialization : Converting python object into a format that can be used or saved 
# Deserialization : reverse process of serialization 


# pickle : Machine readable file  in Binary mode : (0,1)
# Json : Human readable file 


# pickle file 
flight={'Flight_number':123,
        'Airline':'Indigo',
        'Source':'Banglore',
        'Destination':'Hyderabad'}


print('Before serialization:',flight)
import pickle
with open('flight.pkl','wb')as file:
    content=pickle.dump(flight,file)
    print(f'After Serialization:Success',content)
    
# read file 
with open('flight.pkl','rb')as file :
    reader=pickle.load(file)
    print(f'After reading:',reader)
    
    

# Json file 
student={'Name':'Prajwal',
         'Location':'Banglore',
         'salary':40000,
         'Company':'Cisco'}

import json
with open('student.json','w')as file :
    content=json.dump(student,file)
    print(content)    
    
    
# read json file 
with open('student.json','r')as reader:
    content=json.load(reader)
    print(content)
    


