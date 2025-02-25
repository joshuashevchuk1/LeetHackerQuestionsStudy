
def convert(s):
    s = "".join(c.lower() for c in s if c.isalnum())  # convert to alphanumerics, useful for palindromes
    return s

s="Was it a car or a cat I saw?"
print(s)
print(convert(s))
