'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):

    return_values: [int] = []
    #  If the array is only two elements, you can swap them
    if len(arr) == 2:
        return_values.append(arr[1])
        return_values.append(arr[0])

    else:
        # Loop through the arr
        for index in arr:
            # If it is the first index, just grab the product of everything (1..lenghth -1)
            if index == 0:
                temp_value = 1

                for number in (1, len(arr) - 1):
                    value = arr[number] * temp_value
                    temp_value = value

                return_values.append(temp_value)
                print(return_values)

            else:
                right_side: [int] = arr[:index]
                left_side: [int] = arr[index:]
                right_temp = 1
                left_temp = 1

                for number in (0, len(right_side) - 1):
                    value = right_side[number] * right_temp
                    right_temp = value
                    
                for number in (0, len(left_side) - 1):
                    value = left_side[number] * left_temp
                    left_temp = value

                return_values.append(right_temp * left_temp)
    return return_values

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
