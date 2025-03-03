def is_palindrome(string):
    new_str = string.replace(" ", "").lower()  # this is required to remove spaces and upper case letters
    # let's use two pointers iterating in opposite directions this time
    l, r = 0, len(new_str) - 1
    while l < r:
        if new_str[l] != new_str[r]:
            return False
        else:
            l += 1
            r -= 1

    return True



print(is_palindrome("racecar"))  # true
print(is_palindrome("tabby"))  # false
print(is_palindrome("d abc cbaD"))  # true
print(is_palindrome("A man a plan a canal Panama"))  # true
