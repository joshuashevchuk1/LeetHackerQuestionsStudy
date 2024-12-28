
#Backtracking is an algorithmic technique used for solving problems incrementally,
# where you build a solution piece by piece and backtrack whenever you
# determine that the current partial solution cannot lead to a valid
# complete solution. It’s widely used for combinatorial problems,
# like generating permutations, subsets, solving puzzles (e.g., Sudoku),
# and finding paths in a maze.

def find_all_subsets(nums):
   result = []
   def backtrack(start,path):
       result.append(path)
       for i in range (start,len(nums)):
            backtrack(i+1,path + nums[i])
   backtrack(0,[])
   return result

nums = [[1,2],[1]]

print(find_all_subsets(nums))
