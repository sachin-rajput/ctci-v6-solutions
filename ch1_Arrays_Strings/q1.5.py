# Question
# There are three types of edits that can be performed on strings: insert a character, remove a character, 
# or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# ple, pale -> true palss, pale -> true pale, bale -> true pale, bake -> false

# Runtime: O(n) time | O(1) space
def ifOneEditAway(str1, str2):

    edit_count = 0
    j = 0

    #base case
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    # let's swap if str1's len is > str2's len
    if len(str1) > len(str2):
        tmp = str1
        str1 = str2
        str2 = tmp
    
    # print(str1)
    # print(str2)

    # str1 is always shorter string
    for i in range(len(str1)):
        
        if edit_count > 1:
            return False
        
        # removed a character, increase count
        if str1[i] != str2[j] and str1[i] == str2[j+1]:
            edit_count += 1
            j += 2
            continue
        # removed or replaced a character, increase count
        elif str1[i] != str2[j]:
            edit_count += 1
        j += 1

    # this case also handles, adding a character add end
    if edit_count == 0:
        return True
    elif edit_count == 1 and j == len(str2):
        return True
    
    return False
    
print(ifOneEditAway('pale','ple'))

print(ifOneEditAway('palss','pale'))

print(ifOneEditAway('paleas','pale'))

print(ifOneEditAway('pales','pale'))

print(ifOneEditAway('pale','bale'))

print(ifOneEditAway('pale','bake'))
        




