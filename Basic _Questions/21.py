input_numbers = input("Enter numbers separated by space: ")
num_list = [int(x) for x in input_numbers.split()]

min_value = num_list[0]
max_value = num_list[0]

for num in num_list:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print("Minimum:", min_value)
print("Maximum:", max_value)
