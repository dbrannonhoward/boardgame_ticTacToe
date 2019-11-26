from math import log

num_list = []
for i in range(2, 9):
    num_list.append(i)

for i in num_list:
    log_base = 2
    log_exponent = log(i, log_base)
    if i == 2:  # first loop
        log_exponents = []
    log_exponents.append(log_exponent)

print(num_list)
print(log_exponents)

# end
