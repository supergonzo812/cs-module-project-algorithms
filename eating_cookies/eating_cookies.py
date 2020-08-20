'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
#     Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

# For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

#  1. He can eat 1 cookie at a time 3 times
#  2. He can eat 1 cookie, then 2 cookies 
#  3. He can eat 2 cookies, then 1 cookie
#  4. He can eat 3 cookies all at once. 

# Thus, `eating_cookies(3)` should return an answer of 4.

# 1, 1, 1, 1, 1
# 1, 1, 1, 2
# 1, 1, 3
# 1, 2, 2
# 1, 3, 1
# 1, 1, 2, 1
# 1, 2, 1, 1
# 2, 1, 1, 1
# 2, 1, 2
# 2, 2, 1
# 3, 1, 1
# 2, 3
# 3, 2


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
