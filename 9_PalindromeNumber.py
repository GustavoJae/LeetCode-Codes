'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    a=str(x)
    return a == a[::-1]