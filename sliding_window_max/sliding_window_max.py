'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    results: [int] = []

    for index in range(0, (len(nums) - 1)):
        front_slice = index
        back_slice = index + k
        max = 0
        print(f'index: {index}')
        print(f'max set to: {max}')
        print(f'front slice value: {front_slice}')
        print(f'back slice value: {back_slice}')

        if index == 0:

            max = nums[index]
            for number in nums[:back_slice]:
                print(f'{nums[:back_slice]}')
                if nums[number] > max:
                    max = nums[number]
                    print(f'updated max with: {max}')
                    

        else:
            for number in nums[front_slice : back_slice]:

                if len(nums[front_slice : back_slice]) == k:
                    print(f'{nums[front_slice:back_slice]}')
                    if number == front_slice:
                        max = nums[number]
                        print(f'updated max with: {max}')
                    if nums[number] > max:
                        max = nums[number]
                        print(f'updated max with: {max}')
                else:
                    return results
            
        print(f'with max: {max}\n \n')
        results.append(max)
    return results
    


# You can only interact with the `k` numbers in the window. 
# Return an array consisting of the maximum value of each window of elements.

# ## Example
# ```
# Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Expected Output: [3,3,5,5,6,7] 
# Explanation: 

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  ```



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
