def generatorExample():
    return [i for i in range(17)]

for i in range(len(generatorExample())):
    print(i*2)