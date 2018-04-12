# Q2: How many full time employees are there?
import helper

data = helper.read_salaries()

employee_type = helper.get_column(data, 4) # get employee type (full or part-time)
print(helper.count(employee_type, 'F'))    # print full-time count

