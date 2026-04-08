# arrays are used to store a collection of data
# in particular, arrays are a collection of the same data type
# arrays can be one dimensional or multi dimensional
# can be up to n dimensional

def oneDtest():
    return [x for x in range(5)]

def twoDTest():
    return [[x for x in range(5)],[y for y in range(5)]]

print(oneDtest())
print(twoDTest())

x = oneDtest()
xy = twoDTest()

print(x[0])

# for i in range(len(x)):
#     print(x[i])
#
# for i in range(len(xy)):
#     for j in range(len(xy[i])):
#         print(xy[i][j])

def middle(lst):
    return [lst[0],lst[len(lst)-1]]

print(middle(oneDtest()))
print(x[0])
print(x[len(x)-1])

def middle(lst):
    lst.pop()
    lst.remove(lst[0])
    return lst

print(middle(oneDtest()))