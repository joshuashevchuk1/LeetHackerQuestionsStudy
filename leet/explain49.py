from collections import defaultdict

# The log term comes from the divide-and-conquer nature of efficient sorting
# Each time the data is split in half, reducing the problem size logarithmically
# leading to a log(f(k)) factor

def grouper(str):
    """
    :param str:
    :return:
    """
    test = defaultdict(list)
    for string in str: # for the string in the list
        sorted_string = ''.join(sorted(string)) # sort the string # O(k log(k))
        # for the key found
        # append to a list
        # under key sorted string
        test[sorted_string].append(string) # O(1)
    return test # O(n⋅klogk) where n is the number of times inserted into the dictionary

def sort_check(str):
    """
    :param str:
    :return:
    """
    sorted_string = ''.join(sorted(str[0]))
    return sorted_string

str = ["tea","eat","not","new"]
print(list(grouper(str).values()))
print(grouper(str))
str2 = ["bac"]
print(sort_check(str2))
