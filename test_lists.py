# some list testing

print("Log : Init list of 10 None")
ten_nones = [None] * 10
print(ten_nones)

print("Log : Overwrite range(9) values")
for i in range(9):
    ten_nones[i] = i
print(ten_nones)

print("Log : Stop value and append example")
for i in range(1000, 1002):
    stop_val = i
    print("Log : start_val = 100 and stop_val = " + str(stop_val) + ", appended list is : ")
    test_list = []
    for i in range(100, stop_val, 100):
        test_list.append(i)
    print(test_list)
