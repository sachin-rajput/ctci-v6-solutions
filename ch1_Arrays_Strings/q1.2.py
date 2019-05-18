# Question:
# Given two strings, write a method to decide if one is a permutation of the other.

# Runtime: O(n * log n)
def isPermutation1(str1, str2):
    if len(str1) != len(str2):
        return False
    
    # Runtime for sorted here is O(n log n)
    if(''.join(sorted(str1)) != ''.join(sorted(str2))):
        return False
    return True

NO_OF_CHARS = 256

# Runtime: O(n)
def isPermutation2(str1, str2):
    if len(str1) != len(str2):
        return False

    # Let's keep a count of each 
    # character occurence
    charList1 = [0] * NO_OF_CHARS
    charList2 = [0] * NO_OF_CHARS

    # Increment counters for str1
    for x in str1:
        charList1[ord(x)] += 1
    
    # Increment counters for str2
    for x in str2:
        charList2[ord(x)] += 1

    # Loop over NO_OF_CHARS and check
    # if there is mismatch on counters
    for x in range(NO_OF_CHARS):
        if(charList1[x] != charList2[x]):
            return False
    
    return True

print(isPermutation1('scahin','sachin'))
print(isPermutation2('scahin','sachio'))