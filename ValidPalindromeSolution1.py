def is_palindrome(s) -> bool:
    newStr = "" #we need to remove all spaces and non-alphanumeric characters from the original string
    for c in s:
        if c.isalnum():
            newStr += c.lower()

    return newStr == newStr[::-1] #original string same as reversed string? Then yes, is a palindrome

print(is_palindrome("racecar")) #true
print(is_palindrome("tabby")) #false
print(is_palindrome("d abc cbaD")) #true
print(is_palindrome("A man a plan a canal Panama")) #true