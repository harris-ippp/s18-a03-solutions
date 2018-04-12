# Q8: What are the minimum, mean, median, and maximum salaries?
import helper

data = helper.read_salaries()

salaries = []
# get non-empty salaries from the data
for row in data:
    if row[-2] != '':
        salaries.append(row[-2])

print('Minimum:', min(salaries))
print('Mean:', helper.mean(salaries))
print('Median:', helper.median(salaries))
print('Maximum:', max(salaries))
