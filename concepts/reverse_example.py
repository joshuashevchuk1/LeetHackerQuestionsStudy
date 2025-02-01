
nums = [1,2,3,4,5]
print(nums)
print(nums[::-1])

string = "apple"

print(string[::-1])

string = "catttttttttttttttac"

def check_palindrome(string):
    s = len(string)

    mid = s // 2

    lh = string[:mid]
    rh = string[-mid:]

    if lh == rh[::-1]:  # Reverse the right half for comparison
        return True
    return False


print(check_palindrome(string))