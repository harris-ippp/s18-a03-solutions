# Q3: How many part-time employees are there?
import helper

data = helper.read_salaries()

count = 0
for row in data:
    if row[4] == 'P':
        count = count + 1

print(count)

