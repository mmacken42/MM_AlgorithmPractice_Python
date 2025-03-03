def is_palindrome(string):
    newStr = string.replace(" ", "").lower()  # this is required to remove spaces and upper case letters
    # let's use recursion this time
    # this is the recursive base cases so we know when to stop
    if len(newStr) == 1:
        return True  # odd numbered strings end here
    if len(newStr) == 2:
        return newStr[0] == newStr[1]  # even numbered strings end here
    # here is the actual recursive call
    # this checks if first and last letter are same, then calls itself
    # recursively on remaining "middle" string
    return newStr[0] == newStr[len(newStr) - 1] and is_palindrome(newStr[1:-1])


print(is_palindrome("racecar"))  # true
print(is_palindrome("tabby"))  # false
print(is_palindrome("d abc cbaD"))  # true
print(is_palindrome("A man a plan a canal Panama"))  # true
