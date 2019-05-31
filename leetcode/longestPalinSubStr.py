# Given two strings ‘X’ and ‘Y’, find the length of the 
# longest common substring.

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
        
    length = len(s)
    
    if s == None or length < 2:
        return s
    
    isPalindrome = [[False for x in range(length)] for y in range(length)]

    #print(isPalindrome)

    left = 0
    right = 0

    for j in range(1, length):
        for i in range(0, j):
            isInnerWordPalindromic = isPalindrome[i+1][j-1] or j-i <= 2

            if s[i] == s[j] and isInnerWordPalindromic:
                isPalindrome[i][j] = True

                if j - i >  right - left:
                    left = i
                    right = j
    
    return s[left:right+1]


print(longestPalindrome("eabcb"))
