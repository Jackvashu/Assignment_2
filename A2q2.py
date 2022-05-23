dict = {}  # New Dictionary

# range for 97 which is a ascii value 
# from 113 z value
for i in range(97, 123):  
    dict[chr(i)] = i   # changing range value to a-z
print(dict)  #printing dict 
