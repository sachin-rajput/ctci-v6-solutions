# Question:
## Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

## Without additional data structures, will only work for a-z / A-Z 
def isUniqueChars1(str):

  # create a bit mask to store each 
  # appearance of the character
  checker = 0

  for x in str:
    x = x.lower()
    bitCheck = ord(x) - ord('a')
    # Use bit 'AND' to check if 
    # current character already exist
    if(checker & (1 << bitCheck) > 0):
      return False
    
    # Continue to update the bit for 
    # current character by
    # using bit 'OR'
    checker = checker | (1 << bitCheck)

  return True

## With additional data structures
def isUniqueChars2(str):
  # create a list of booleans for 
  # all 256 chars
  charList = [False] * 256

  for x in str:
    # convert current character to it's 
    # equivalent int value and check if 
    # it's already marked as 'True'
    if charList[ord(x)] == True:
      return False
    
    # Lets mark current character as visited
    charList[ord(x)] = True
  
  return True

# Driver code to run above methods

print(isUniqueChars1('AiYhIn'))

print(isUniqueChars2('sachin'))