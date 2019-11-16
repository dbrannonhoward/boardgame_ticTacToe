one_dim_list = ['a', 'b']
two_dim_list = [one_dim_list, one_dim_list]
tre_dim_list = [two_dim_list, two_dim_list]
for_dim_list = [tre_dim_list, tre_dim_list]

print(one_dim_list)  # has 1 "a"
print(two_dim_list)  # has 2 "a"
print(tre_dim_list)  # has 4 "a"
print(for_dim_list)  # has 8 "a"

print(one_dim_list.count("a"))
print(one_dim_list.count("a"))
print(tre_dim_list.count(two_dim_list))
print(for_dim_list.count(tre_dim_list))
