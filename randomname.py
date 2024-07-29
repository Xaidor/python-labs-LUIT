import random

# Ask how many EC2 instances do the users want names for
how_many = int(input('How many EC2 names would you like generated? '))

# Ask for user input department name v 
user_input = input('What department are you in? ')

# Generate random characters and numbers to go with the department name
for a in range(how_many) :
  
# Output the amount of EC2 instant names, Should list them off
     print(user_input + str(random.randrange(0,200)))