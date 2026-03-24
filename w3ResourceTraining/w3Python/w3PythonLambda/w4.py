# Write a Python program to sort a list of dictionaries using Lambda.
#
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

# @overload def sorted(__iterable: Iterable[SupportsRichComparisonT],
#            *,
#            key: None = None,
#            reverse: bool = False) -> list[SupportsRichComparisonT]
#
# Return a new list containing all items from the iterable in ascending order.

items =  [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_items = sorted(items, key= lambda x : x['color'])

print(items)
print(sorted_items)