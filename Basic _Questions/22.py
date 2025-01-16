input_numbers = input("Enter numbers separated by space: ")
num_list = [int(x) for x in input_numbers.split()]

length = len(num_list)
half_length = length // 2

for i in range(half_length):
    temp = num_list[i]
    num_list[i] = num_list[-i-1]
    num_list[-i-1] = temp

print("Reversed List:", num_list)
