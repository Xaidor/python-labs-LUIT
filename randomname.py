import random

# Ask how many EC2 instances do the users want names for then ask for user input department name 
how_many = int(input('Enter how many EC2 names you\'d like generated: '))
department_name = input('What department are you in? ')

# Generate random characters and numbers to go with the department name
for a in range(how_many) :
     random_char = ''.join(random.choices(string.ascii_letters, k=2))
     new_names = department_name + '-' + random_char + str(random.randrange(0,200))
     
# Output the amount of EC2 instances names
     print(new_names)
