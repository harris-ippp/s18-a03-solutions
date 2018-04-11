# Q5: How many detectives?
import helper

data = helper.read_salaries()

count = 0
for row in data:
    if row[2] == 'POLICE OFFICER (ASSIGNED AS DETECTIVE)':
        count = count + 1

print(count)

