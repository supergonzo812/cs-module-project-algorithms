'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
# Write a function that 
# takes an array of integers and 
# moves each non-zero integer to the left side of the array, 

    for (index, value) in enumerate(arr):
        popped = False

        if value == 0:
            arr.append(0)
            arr.pop(index)
            popped = True
        
        if popped:
            for (index2, value2) in enumerate(arr):
                if value2 == 0:
                    arr.append(0)
                    arr.pop(index2)
                    popped = False
    return arr


# then returns the altered array. 
# The order of the non-zero integers does not matter in the mutated array.

# ## Examples
# ```
# Sample input: [0, 3, 1, 0, -2]
# Expected output: 3
# Expected output array state: [3, 1, -2, 0, 0]
# ```

# ```
# Sample input: [4, 2, 1, 5]
# Expected output: 4
# Expected output array state: [4, 2, 1, 5]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

    arr2 = [0, 0, 0, 0, 3, 2, 1] 
    
    print(moving_zeroes(arr2))