'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
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

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

    arr2 = [0, 0, 0, 0, 3, 2, 1] 
    
    print(moving_zeroes(arr2))