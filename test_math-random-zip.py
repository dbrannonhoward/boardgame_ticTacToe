from math import log
import random

print("Log : The output of range(2, 9) is : ")
range_list = []
for i in range(2, 9):
    range_list.append(i)
print(range_list)

print("Log : The logarithms of log_base**i for range(2,9) are : ")
number_list = []
log_base = 2
for i in range(2, 9):
    number_list.append(log(i, log_base))
print(number_list)

print("Log : random.random() testing : ")
ran_num_list = []
for i in range(99999):  # suggest max value 9,999,999
    random_number = 4 * random.random()
    if random_number < 0.33333:
        random_number = 1
    elif random_number < 0.66666:
        random_number = 2
    elif random_number < 1:
        random_number = 3
    ran_num_list.append(int(random_number))
# print(ran_num_list)
print("There are " + str(ran_num_list.count(1)) + " ones.")
print("There are " + str(ran_num_list.count(2)) + " twos.")
print("There are " + str(ran_num_list.count(3)) + " threes.")

print("The output of a list, another list, then some zips of those two lists are : ")
first_list = [value for value in range(5)]
print(first_list)
second_list = [anything for anything in range(7)]
print(second_list)
zip_list = zip(first_list, second_list)
zip_set = set(zip_list)
print(zip_set)
# zip_list = zip(first_list, second_list)  # todo why did i have to add this duplicate line to avoid empty zip_dict?
zip_dict = dict(zip_list)
print(zip_dict)
print("Debug : Check comments to see why that was empty.")
# end
