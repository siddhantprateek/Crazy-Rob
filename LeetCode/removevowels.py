s = "leetcodeisacommunityforcoders"

new_string = list(s)

for letter in s:
    if letter == "a":
        new_string.remove("a")
    if letter == "e":
        new_string.remove("e")
    if letter == "i":
        new_string.remove("i")
    if letter == "u":
        new_string.remove("u")
    if letter == "o":
        new_string.remove("o")
result = ""
for char in range(len(new_string)):
    result += new_string[char]
print(result)
