# A.1: Parse the included salaries.csv file.
# Your parser should split each line on ',' and return a nested list 
# where each element is itself a list of fields. 
# Additionally you should ignore/remove the first (header) line.
def read_salaries():
    data = []
    first = True
    for line in open('salaries.csv'):
        if not first:
            line = line[:-1]
            row = line.split(',')
            salary = row[-2]
            if len(salary) > 0:
                row[-2] = float(salary[1:])

            row[0] = row[0][1:]
            row[1] = row[1][2:-1].split(' ')[0]

            data.append(row)
        else:
            first = False
    return data

# A.2: Given a 2d list data and an integer column_index 
# return a 1d list of values for that column.
def get_column(data, column_index):
    column = []
    for row in data:
        column.append(row[column_index])
    return column

# A.3: Given a 1d list of `values` (e.g. the result of get_column), 
# return the number of elements that are equal to `search_value`.
def count(values, count_value):
    count = 0
    for value in values:
        if value == count_value:
            count = count + 1

    return count

# A.4: Given a 1d list values (e.g. the result of get_column),
# return a dictionary of value-count pairs.
def counts(values):
    d = {}
    for value in values:
        if value in d:
            d[value] = d[value] + 1
        else:
            d[value] = 1
    return d

# A.5: Given a dictionary d with numeric values, return a list [key, value] of two elements,
# where key is the the key in d with the largest value, and value is it's value. 
def dict_max_value(d):
    max_value = max(d.values())
    for key in d:
        if d[key] == max_value:
            return [key, max_value]

# A.6: Given a list of numbers use the built-in functions sum and len to return their mean.
def mean(numbers):
    return sum(numbers)/len(numbers)

# A.7: Given a list of numbers calculate the median.
def median(numbers):
    sorted_numbers = sorted(numbers)
    index = len(numbers)/2
    int_index = int(index)

    if index == int_index:
        return (sorted_numbers[int_index-1] + sorted_numbers[int_index])/2
    else:
        return sorted_numbers[int_index]
