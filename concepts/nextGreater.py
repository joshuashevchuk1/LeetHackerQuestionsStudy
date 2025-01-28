
# uses a monotonic stack to get the next greater element

def nextGreater(vals):
    answer = [0] * len(vals)
    stack = []
    for i in range(len(vals)):
        # at the first iteration stack is empty so just append(i)
        while stack and vals[i] > vals[stack[-1]]:  # shorthand top of list
            # if stack is not empty and the current i
            # (should be 2..n at the 2nd iteration)
            # is greater than the top of the stack
            # pop the top of the stack and append to answers
            index = stack.pop()
            answer[index] = vals[i]
        stack.append(i)