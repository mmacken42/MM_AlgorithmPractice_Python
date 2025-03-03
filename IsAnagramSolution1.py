def is_anagram(s: str, t: str) -> bool:
    #sort strings as arrays, then just check for =
    if len(s) != len(t):
        return False
    return sort_string(s) == sort_string(t)

def sort_string(s: str):
    return ''.join(sorted(s))

print(is_anagram("racecar", "carrace")) #true
print(is_anagram("blocks", "boxes")) #false