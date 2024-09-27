https://leetcode.com/problems/palindrome-number/

#This could have been smaller, lol

class Solution(object):
    def isPalindrome(self, x):
        array_ori = []
        for char in str(x):
            array_ori.append(char)

        array_inv = array_ori[::-1]

        if array_ori == array_inv:
            return True
        else:
            return False
