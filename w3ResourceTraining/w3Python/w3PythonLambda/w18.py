# @overload def __new__(cls,
#             __function: None,
#             __iterable: Iterable[_T | None]) -> Self
#
# Create and return a new object. See help(type) for accurate signature.

# @overload def __init__(self, __sequence: Reversible[_T]) -> None
#
# Return a reverse iterator over the values of the given sequence

texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]

result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
