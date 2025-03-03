def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("racecar")) #true
print(is_palindrome("tabby")) #false
print(is_palindrome("d abc cbaD")) #true
print(is_palindrome("A man a plan a canal Panama")) #true