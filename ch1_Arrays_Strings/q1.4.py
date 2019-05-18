# Question
# Given a string, write a function to check if it is a permutation of a palin­ drome. 
# A palindrome is a word or phrase that is the same  rwards and backwards. 
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

# Runtime: O(n) using extra data structure
def isPermPalindrome(str):
    # Initialize a char list with 0 count
    charList = [0] * 256

    # Loop over the str and track the count
    # for each occurence of character
    for i in str:
        if(i != ' '):
            charList[ord(i)] += 1

    odd_count = 0

    # If we find more than 1 count of
    # odd count than it is not a permutation of 
    # palindrome
    for i in range(256):
        if charList[i] > 0:
            # print('Current Character: ',chr(i))
            # print('Count: ',charList[i])
            if charList[i]%2 > 0 and odd_count == 0:
                odd_count += 1
            elif charList[i]%2 > 0:
                return False
        
    return True

print(isPermPalindrome('t aa'))
