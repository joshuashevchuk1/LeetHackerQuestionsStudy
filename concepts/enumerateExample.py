my_list = ['apple', 'banana', 'cherry']

for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")

# Output:
# Index: 0, Item: apple
# Index: 1, Item: banana
# Index: 2, Item: cherry

# Example with a custom starting index
for index, item in enumerate(my_list, start=1):
    print(f"Index: {index}, Item: {item}")

# Output:
# Index: 1, Item: apple
# Index: 2, Item: banana
# Index: 3, Item: cherry