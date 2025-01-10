
def subarrays(arr):
    result = []
    def backtrack(start,path):
        result.append(path)
        for i in range(start,len(arr)):
            backtrack(i+1,path + arr[i])

    return result
