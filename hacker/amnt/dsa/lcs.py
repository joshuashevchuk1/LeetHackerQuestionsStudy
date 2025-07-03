
# easy ish dp way to do
def lcs(a,b):
    return



# super hard to do

def generate_subsequences_by_backtracl(arr):
    result = []

    def backtrack(index, path):
        if index == len(arr):
            result.append(path[:])
            return
        # Exclude current element
        backtrack(index + 1, path)
        # Include current element
        path.append(arr[index])
        backtrack(index + 1, path)
        path.pop()

    backtrack(0, [])
    return result

def generate_subsequences(arr):
    result = []
    result.append([])

    for element in arr:
        if element not in result:
            result.append(element)

    return result

def brute_lcs(a, b):
    subs_a = generate_subsequences(a)
    subs_b = generate_subsequences(b)

    set_b = set(tuple(x) for x in subs_b)
    common = []

    max_len = 0
    for seq in subs_a:
        t = tuple(seq)
        if t in set_b:
            if len(seq) > max_len:
                max_len = len(seq)
                common = [seq]
            elif len(seq) == max_len:
                common.append(seq)
    return common

a = ['a','b','c','b','d','a','b']
b = ['b','d','c','a','b','a']

brute_lcs(a,b)