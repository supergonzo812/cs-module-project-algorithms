'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    if len(arr) > 1:

        reference_value = arr[0]
        reference_index = 0

        while len(arr) > 1:
            
            for index, value in enumerate(arr): 
                if value == reference_value :
                    arr.pop(index)
                    arr.pop(reference_index)
                reference_index = index
                reference_value = value

    else:
        return arr
    return arr



    # # check if arr has more than one element, otherwise return the array
    # if len(arr) > 1:

    #     # loop through the array from the second indext to the last element
    #     for index in range(1, len(arr) - 1):

    #         if  arr[index] == arr[0]:
    #             arr.pop(index)
    #             single_number(arr)
    # else:
    #     return arr

    # return arr

# [ 4, 1, 2, 1, 2]

# [4, 1, 2, 1, 2]

# [4, 2, 2]

# [4]

# [ 4, 1, 2, 1, 2]

# [4, 1, 2, 1, 2]

# [4, 2, 2]

# [4]


# Given a non-empty array of integers where every element appears twice except for one. 
# Find that single number. 
# 
# You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.  

# ## Examples
# ```
# Sample input: [2, 2, 1]
# Expected output: 1
# ```

# ```
# Sample iput: [4, 1, 2, 1, 2]
# Expected output: 4
# ```

# Can you implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")