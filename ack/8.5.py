# recursive multiply


def add(a,b):
    a = a + b
    return a

def multiply(a,n):
    o = a
    for i in range(n):
        if i > 0:
            a = add(o,a)
    return a

print(multiply(1,1))
print(multiply(2,1))
print(multiply(2,2))
print(multiply(2,4))
print(multiply(2,6))
print(multiply(2,12))