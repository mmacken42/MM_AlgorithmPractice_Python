input_string = "Hello, World!"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string #prepend each char to end up with reversed string

print(reversed_string) #outputs reversed string

#one for loop so time complexity should be O(n) where n is length of string
#created a new string variable so space complexity should be O(n)? not sure about that