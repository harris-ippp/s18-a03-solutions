# Q5: How many detectives?
import helper

data = helper.read_salaries()

positions = helper.get_column(data, 2) # get positions
print(helper.count(positions, 'POLICE OFFICER (ASSIGNED AS DETECTIVE)')) # print police detective count

