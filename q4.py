# Q4: How many employees in the police department?
import helper

data = helper.read_salaries()

count = 0
for row in data:
    if row[3] == 'POLICE':
        count = count + 1

print(count)

