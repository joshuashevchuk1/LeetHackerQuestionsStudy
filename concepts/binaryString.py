# Python code for above approach

# function to calculate the Hamming distance between two binary strings
def hammingDistance(s1, s2):
    hamming_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            hamming_dist += 1
    return hamming_dist

# create binary strings
binary_str1 = "10101010"
binary_str2 = "01010101"

# Length of binary string
print("Length of binary string 1:", len(binary_str1))

# Concatenation of binary strings
concatenated_str = binary_str1 + binary_str2
print("Concatenation of binary strings:", concatenated_str)

# Substring of binary string
substring = binary_str1[2:6]  # starting index and ending index (exclusive)
print("Substring of binary string 1:", substring)

# Prefix of binary string
prefix = binary_str1[:3]  # starting index and ending index (exclusive)
print("Prefix of binary string 1:", prefix)

# Suffix of binary string
suffix = binary_str2[4:]  # starting index
print("Suffix of binary string 2:", suffix)

# Hamming distance between two binary strings
hamming_dist = hammingDistance(binary_str1, binary_str2)
print("Hamming distance between binary strings 1 and 2:", hamming_dist)

# Regular Language of binary strings (ends with '0')
has_regular_language = binary_str1[-1] == '0'
print("Does binary string 1 have a regular language?", "Yes" if has_regular_language else "No")

# Binary Arithmetic (addition)
binary_num1 = int(binary_str1, 2)
binary_num2 = int(binary_str2, 2)
Sum = bin(binary_num1 + binary_num2)[2:].zfill(8)
print("Binary addition of", binary_str1, "and", binary_str2 + ":", Sum)

# This code is contributed by Utkarsh Kumar