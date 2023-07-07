number_of_inputs = input("How many values do you want to add? ")
i = 0
prev_value = 0
cur_value = 0
total_so_far = 0
while i < int(number_of_inputs):
    prev_value = cur_value
    values = input("Value " + str(i) + ": ")
    print(prev_value)
    cur_value = int(values)
    total_so_far = total_so_far + cur_value
    print(total_so_far)
    i += 1