def printLine(n):
    s = "*"
    for i in range(n):
        s += 2 * "*"
    print(s.center(50))


print("*".center(50))
for i in range(1, 10):
    printLine(i)


def printLine(n):
    s = ['*']  # Use a list to accumulate stars
    for i in range(n):
        s.append('**')  # Append two stars
    print("".join(s).center(50))  # Join the list into a single string and center it

print("*".center(50))
for i in range(1, 10):
    printLine(i)
