def generate_subsequences_bit_mask(arr):
    n = len(arr)
    subsequences = []

    for mask in range(1 << n):  # 2^n combinations
        subseq = []
        for i in range(n):
            if (mask >> i) & 1:
                subseq.append(arr[i])
        subsequences.append(subseq)

    return subsequences


def generate_subsequences_by_backtrack(arr):
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

a = ['a','b','c','b','d','a','b']
b = ['b','d','c','a','b','a']
c=[1,2,3]
d=[1,2,3,4]


subs_a = generate_subsequences(a)
subs_b = generate_subsequences(b)

subs_abt = generate_subsequences_by_backtrack(a)
subs_bbt = generate_subsequences_by_backtrack(b)

subs_c = generate_subsequences_by_backtrack(c)
subs_d = generate_subsequences_by_backtrack(d)

print('done')