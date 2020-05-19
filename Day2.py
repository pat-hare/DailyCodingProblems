# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

import math

# with division
def prod_arr_without_i(input_list):
    output = list()
    total = math.prod(input_list)
    for i in input_list:
        sub_total = total / i
        output.append(int(total))

    return output

# without division
def prod_arr_without_i_no_div(input_list):
    output = list()
    for index, item in enumerate(input_list):
        # shallow copy list to remove index
        temp_arr = input_list.copy()
        temp_arr.pop(index)

        # get product of shallow array and add to output
        sub_total = math.prod(temp_arr)
        output.append(sub_total)

    return output

# input = [1, 2, 3, 4, 5]
# expected output = [120, 60, 40, 30, 24]
print(prod_arr_without_i_no_div([1,2,3,4,5]))

# input = [3, 2, 1]
# expected output = [2, 3, 6]
print(prod_arr_without_i_no_div([3, 2, 1]))