def hourglassSum(arr):
    max_sum = float('-inf')
    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
            # make the hour glass relative to the array (len-2 because an hour glass i len(2)_
            hourglass_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                arr[i + 1][j + 1] +
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            )
            # recursively iterate through all arrays using the max function until the biggest hour glass is found
            max_sum = max(max_sum, hourglass_sum)

    return max_sum