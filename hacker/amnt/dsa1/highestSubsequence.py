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

def get_max(subs):
    max_sum = float('-inf')
    for subsequence in subs:
        max_sum = max(max_sum, sum(subsequence))
    return max_sum

a = [1, 2, 3, 4, 3, 2]

subs_a = get_subsequences(a)
print(subs_a)
print(get_max(subs_a))
