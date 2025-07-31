from pprint import pprint


def l1():
    return lambda a: a + 10

def l2():
    return lambda a, b: a * b

def printList():
    return lambda a: [print(item) for item in a]

def printUrls():
    return lambda a: [print(f'url : {item[0]}') for item in a]

add_l1 = l1()
add_l2 = l2()
print(add_l1(5))
print(add_l2(5,2))

pl = printList()

a =[1,2,3]
pl(a)
