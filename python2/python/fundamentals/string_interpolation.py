first_name = 'Zen'
last_name = 'Coder'
age = 27
# f strings
print(f'My name is {first_name} {last_name} and I am {age} years old.')

# string.format

print('My name is {} {} and I am {} years old.'.format(first_name, last_name, age))
# output: My name is Zen Coder I am 27 years old

print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
