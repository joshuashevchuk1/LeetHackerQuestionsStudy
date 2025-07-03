from hacker.amnt.dsa.subsequences import subs_a

a = ['a','b','c','b','d','a','b']
b = ['b','d','c','a','b','a']
c=[1,2,3]
d=[1,2,3,4]

def get_subsequences(arr):
    result = []

    def dfs(i, path):
        if i == len(arr):
            result.append(path[:])
            return
        dfs(i + 1, path)  # exclude
        path.append(arr[i])  # include
        dfs(i + 1, path)
        path.pop()

    dfs(0, [])
    return result


print(get_subsequences(a))
print(get_subsequences(b))
print(get_subsequences(c))
print(get_subsequences(d))