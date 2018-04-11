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

def get_column(data, column_index):
    column = []
    for row in data:
        column.append(row[column_index])
    return column

def count(values):
    counts = {}
    for value in values:
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1
    return counts

def dict_max_value(d):
    max_value = max(d.values())
    for key in d:
        if d[key] == max_value:
            return [key, max_value]

def mean(numbers):
    return sum(numbers)/len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    index = len(numbers)/2
    int_index = int(index)

    if index == int_index:
        return (sorted_numbers[int_index-1] + sorted_numbers[int_index])/2
    else:
        return sorted_numbers[int_index]
