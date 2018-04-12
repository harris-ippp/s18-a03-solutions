# Q3: How many part-time employees are there?
import helper

data = helper.read_salaries()

employee_type = helper.get_column(data, 4) # get employee type (full or part-time)
print(helper.count(employee_type, 'P'))    # print full-time count
