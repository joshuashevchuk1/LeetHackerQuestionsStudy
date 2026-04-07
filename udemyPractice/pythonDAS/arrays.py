# arrays are used to store a collection of data
# in particular, arrays are a collection of the same data type
# arrays can be one dimensional or multi dimensional
# can be up to n dimensional

def oneDtest():
    return [1,2,3]

def twoDTest():
    return [[x for x in range(5)],[y for y in range(5)]]

print(oneDtest())
print(twoDTest())

x = oneDtest()
xy = twoDTest()

print(x[1])

for i in range(len(x)):
    print(x[i])

for i in range(len(xy)):
    for j in range(len(xy[i])):
        print(xy[i][j])
