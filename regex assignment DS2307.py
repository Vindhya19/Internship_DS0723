#!/usr/bin/env python
# coding: utf-8

# def replace_chars_with_colon(input_string):
#     replace_chars = [' ', ',', '.']
#     output_string = input_string
# 
#     for char in replace_chars:
#         output_string = output_string.replace(char, ':')
# 
#     return output_string
# 
# input_string = input("enter your string data: ")
# result = replace_chars_with_colon(input_string)
# print("expected output is:", result)

# In[21]:


import re

def find_words_starting_with_a_or_e(input_string):
    words = re.findall(r'\b[aeAE]\w+', input_string)
    return words

input_string = input("Enter a string to test: ")
result = find_words_starting_with_a_or_e(input_string)

if result:
    print("Words starting with 'a' or 'e' are as follows:")
    for word in result:
        print(word)
else:
    print("No words starting with 'a' or 'e' are found in the above string.")


# In[23]:


import re

def find_long_words(input_string):
    pattern = re.compile(r'\b\w{4,}\b')
    long_words = pattern.findall(input_string)
    return long_words

input_string = "my name is vindhya, simply tested"
result = find_long_words(input_string)
print(result)


# 

# In[25]:


import re

def find_long_words(input_string):
    pattern = re.compile(r'\b\w{3,5}\b')
    long_words = pattern.findall(input_string)
    return long_words

input_string = "my colleague names are Joe,larry and ishu"
result = find_long_words(input_string)
print(result)


# In[32]:


import re

def remove_parentheses(strings):   
    
    pattern = re.compile(r'\(|\)')
    
    final_strings = [pattern.sub('', s) for s in strings]

    return final_strings

input_strings = ['remove (parentheses)','tested (successfully)']
final_strings = remove_parentheses(input_strings)
print(final_strings)


# In[38]:


import re

items = ["comtronusa (.com)", "vindhyapasala (gmail.com)" ]

for item in items:
    
    print(re.sub(r" ?\([^)]+\)", "",item))


# In[39]:


import re

example_string = "Myself Vindhya is working at Comtron Company"
result = re.findall('[A-Z][^A-Z]*', example_string)
print(result)


# In[42]:


import re

def insert_spaces(string):
    modified_string = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', string)
    return modified_string
sample_string = "DataTrainednumber1institue"
output = insert_spaces(sample_string)
print(output)


# In[48]:


import re

def insert_spaces(string):
    pattern =r'([A-Z0-9][a-z]*)'
    words = re.findall(pattern, string)
    return ''.join(words)
sample_string = "DataTrainednumber1institue in our State"
output = insert_spaces(sample_string)
print(output)


# In[58]:


import re

text = " my name is vindhya and my email id is vindhyapasala@gmail.com"
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)


# 

# In[60]:


import re

def text_match(text):
    pattern = r'^[a-zA-Z0-9_]+$'
    if re.search(pattern, text):
        return 'matched'
    else:
        return 'Not matched'
print(text_match("Hello lazy girl."))
print(text_match("datatrained_number_1"))


# 

# In[75]:


import re

my_string = "5favnum"

reg = re.search('^\s*[0-9]' ,my_string)
print(reg)


# In[77]:


import re

ip="96.0.0.100"
string = re.sub('\.[0]*','.',ip)
print(string)


# In[83]:


import re

datestring = '07-19-1998'

str =re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)

print ("The first input date string is", str.group())

datestring = '1998-07-19'

str=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)

print ("Date not found in the required format")


# In[89]:


def search_words(text, words):
    found_words = []
    for word in words:
        if word in text:
            found_words.append(word)
    return found_words

sample_text = 'I am having pen, laptop and mobile in my hand now'
searched_words = ['pen', 'pencil', 'laptop']

found_words = search_words(sample_text, searched_words)

for word in found_words:
    print(f"Word '{word}' found in the text.")


# In[91]:


def search_and_locate(substring, text):
    index = text.find(substring)
    if index != -1:
        print(f"word found at index: {index}")
    else:
        print("word not found in the text")

sample_text = 'I am having pen, laptop and mobile in my hand now'
searched_word = 'laptop'

search_and_locate(searched_word, sample_text)


# In[94]:


import re

def find_substrings(text, pattern):
    matches = re.finditer(pattern, text)
    positions = [(match.start(), match.end()) for match in matches]
    return positions

sample_text = 'physical exercise, cardio exercise'
search_pattern = 'exercise'

substring_positions = find_substrings(sample_text, search_pattern)

for start, end in substring_positions:
    print(f"Substring is found at position {start}-{end}: {sample_text[start:end]}")


# In[96]:


def find_substring_occurrences(text, pattern):
    occurrences = []
    start = 0
    while start < len(text):
        pos = text.find(pattern, start)
        if pos == -1:
            break
        occurrences.append(pos)
        start = pos + 1
    return occurrences

sample_text = 'Pyscial exercises, cardio exercises'
search_pattern = 'exercises'

substring_occurrences = find_substring_occurrences(sample_text, search_pattern)
num_occurrences = len(substring_occurrences)

print(f"Pattern '{search_pattern}' occurs {num_occurrences} times at positions:")
for pos in substring_occurrences:
    print(pos)


# In[97]:


def convert_date_format(date):
    parts = date.split("-")
    if len(parts) != 3:
        return "Invalid date format. Please use yyyy-mm-dd."

    year = parts[0]
    month = parts[1]
    day = parts[2]

    new_date_format = f"{day}-{month}-{year}"
    return new_date_format

# Input date in yyyy-mm-dd format
input_date = input("Enter a date in yyyy-mm-dd format: ")

# Convert the date format
new_date_format = convert_date_format(input_date)

print("Converted date:", new_date_format)


# In[100]:


import re

def find_decimal_numbers(text):
    decimal_pattern = re.compile(r'\b\d+(\.\d{1,2})?\b')
    matches = decimal_pattern.findall(text)
    return matches

sample_string = "The temperature today at vizag is 28.3°C. and tomorrow it might be 45.2°C"
decimal_numbers = find_decimal_numbers(sample_string)
print(decimal_numbers)


# In[105]:


def separate_numbers_and_positions(text):

    numbers = []
    positions = []

    for idx, char in enumerate(text):
        if char.isdigit():
            num_start = idx
            while idx < len(text) and (text[idx].isdigit() or text[idx] == '.'):
                idx += 1
            num_end = idx
            numbers.append(text[num_start:num_end])
            positions.append(num_start)
            return numbers, positions

test_string = "The temperature today at vizag is 28.3°C. and tomorrow it might be 45.2°C"
numbers, positions = separate_numbers_and_positions(test_string)

for num, pos in zip(numbers, positions):
        print(f"Number: {num}, Position: {pos}")


# In[108]:


import re

def extract_max_numeric_value(text):
    numbers = re.findall(r'\d+', text)
    
    if numbers:
        max_value = max(map(int, numbers))
        return max_value
    else:
        return None
    
sample_text = 'My team employee codes are 1077, 1078, 1091, 1099, 1113'
max_value = extract_max_numeric_value(sample_text)

if max_value is not None:
    print(f"The maximum numeric value is: {max_value}")
else:
    print("No numeric values found in the text.")


# In[ ]:


import re

def insert_spaces_between_capital_words(text):
    spaced_text = re.sub(r'(?<=[a-z])([A-Z])', r' \1', text)
    spaced_text = re.sub(r'([a-z])([0-9])', r'\1 \2', spaced_text)
    return spaced_text

# Example usage
sample_text = "IamworkingasInterfaceAnalyst"
formatted_text = insert_spaces_between_capital_words(sample_text)
print(formatted_text)


# In[1]:


import re

pattern = r'[A-Z][a-z]+'
text = "She is Working as Interface Analyst"

matches = re.findall(pattern, text)
print(matches)


# In[ ]:


import re

def delete_continuous_duplicates(sentence):
    pattern = r'\b(\w+)(?:\s+\1)+\b'
    result = re.sub(pattern, r'\1', sentence, flags=re.IGNORECASE)
    return result
sample_text = "She she is in Visakhapatnam"
output = delete_continuous_duplicates(sample_text)
print(output)


# In[2]:


import re
    
def validate_string(input_string):
    reg_exp = r".*[a-zA-Z0-9]$"
    
    if re.match(reg_exp, input_string):
        return True
    else:
        return False
    
user_input = input("enter a string: ")

if validate_string(user_input):
    print("string is valid")
else:
    print("string is not valid")
                   


# In[13]:


import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags
 
sample_text = "My favorite symbol in watsup is: #hashtag I mean #vindhyasri"
hashtags = extract_hashtags(sample_text)
print(hashtags)


# In[14]:


import re

def remove_special_symbols(text):
    pattern = r'<U\+[A-F0-9]+>'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

sample_text = """sample text <U+1234>. Also, another symbol <U+ABCD> can also be found here."""

cleaned_text = remove_special_symbols(sample_text)
print(cleaned_text)


# In[17]:


import re, datetime 

str1 = "My Date of Birth is 1998-07-19" 

print("The given string is") 
print(str1) 

day = re.search('\d{4}-\d{2}-\d{2}', str1) 

date = datetime.datetime.strptime(day.group(), '%Y-%m-%d').date() 

print("The date present in the above string is")
print(date)


# In[19]:


import re

def delete_words_by_length(input_text):
    pattern = re.compile(r'\b\w{2,4}\b')
    modified_text = pattern.sub('', input_text)
    modified_text = re.sub(r'\s+', ' ', modified_text)  # Remove extra spaces
    return modified_text.strip()

sample_text = "vindhya is working in comtron company"
output = delete_words_by_length(sample_text)
print(output)


# In[ ]:




