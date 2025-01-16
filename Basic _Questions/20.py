input_numbers = input("Enter numbers separated by spaces: ")
num_list = list(map(int, input_numbers.split()))

list_sum = sum(num_list)

print("Sum of the list is:", list_sum)
