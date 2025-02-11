
def reverseString(string):
    string = string[::-1]
    return string

def nextChar(char):
    return chr(ord(char) + 1)

def removeBackAndForceWhiteSpace(s):
    s.strip()
    return s

def iterateAtSpaceChar(s):
    s = s.split(" ")
    return s