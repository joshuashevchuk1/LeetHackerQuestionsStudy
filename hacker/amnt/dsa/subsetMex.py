def get_subsequences(arr):
    result = []

    def dft(index, path):
        if index == len(arr):
            result.append(path[:])
            return
        dft(index + 1, path)  # Exclude current element
        path.append(arr[index])
        dft(index + 1, path)  # Include current element
        path.pop()

    dft(0, [])
    return result

def mex(subset):
    s = set(subset)
    i = 0
    while True:
        if i not in s:
            return i
        i += 1

arr = [0, 1, 2, 4, 5]

subsequences = get_subsequences(arr)

# Just print mex for original array
print(mex(arr))  # 3

# Or mex for each subsequence:
for subseq in subsequences:
    print(f"Subsequence: mex: {mex(subseq)}")