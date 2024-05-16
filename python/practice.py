def sorted_string(string):
    words=string.split()
    words.sort()
    new_sorted=" , ".join(words)
    return new_sorted

input_string=input("Enter:")
print(sorted_string(input_string))


def with_commas(string):
    result=""
    for character in string:
        result+= character+","
    return result[:-1]

input_string=input("Enter:")
print(with_commas(input_string))