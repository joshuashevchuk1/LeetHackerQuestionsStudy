

def ArrayList():
    array = []
    for i in range(5):
        array.append(i)
    return array

def ArrayWithListComprehensionExample2():
    array = [i for i in "hello"]
    return array

def ArrayWithListComprehension():
    array = [i for i in range(5)]
    return array

def returnOdds():
    return [i for i in range (20) if i % 2 != 0]

def returnEvens():
    return [i for i in range (20) if i % 2 == 0]

print(ArrayList())
print(ArrayWithListComprehension())
print(ArrayWithListComprehensionExample2())
print(returnOdds())
print(returnEvens())
