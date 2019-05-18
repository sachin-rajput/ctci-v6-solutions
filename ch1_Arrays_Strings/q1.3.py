# Question
# Write a method to replace all spaces in a string with '%20 
# You may assume that the string has suf cient space at the end to hold the additional characters,and that you are given the "true" length of the string. 
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"

#Runtime: O(n) time | O(1) space
def encodeSpace(str, str_len):
    if str == '' or str.strip() == '':
        return ''

    #Count the number of spaces 
    spaces = 0
    for i in range(len(str)):
        if (str[i] == ' '):
            spaces += 1

    #Eliminate spaces at the end count
    while(str[i] == ' '):
        spaces -= 1
        i -= 1

    #Let's create an index to fill from end
    totalLength = i + spaces * 2 + 1
    index = totalLength - 1
    
    for j in range(i,-1, -1):
        if(str[j] == ' '):
            str = str[:index-2] + '%20' + str[index+1:]
            index -= 3
        else:
            if(totalLength - 1 == index):
                str = str[:index] + str[j]
            else:
                str = str[:index] + str[j] + str[index+1:]
            index -= 1

    #print(len(str))
    return ''.join(str)


print(encodeSpace("My Name is sachin      ", 17))


