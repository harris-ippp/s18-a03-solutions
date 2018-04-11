# Q7: How big is the largest department? Which one is it?
import helper

data = helper.read_salaries()
departments = helper.get_column(data, 3)
counts = helper.count(departments)

print(helper.dict_max_value(counts))
