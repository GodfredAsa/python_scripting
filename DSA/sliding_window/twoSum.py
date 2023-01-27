

def two_Sum(nums: list[int], target: int) -> list[int]:
    has_map = {}
    for i in range(len(nums)):
        if nums[i] in has_map:
            return [i, has_map[nums[i]]]
        else:
            has_map[target - nums[i]] = i

print(f"Two Sum: {two_Sum([1,4,10,-3], target = 14)}")
print(two_Sum([1,4,10,-3], target = 14))

def removeDuplicates(numberArray: list[int]):
    start, nextIndex= 1, 1
    for start in range(len(numberArray)):
        if numberArray[nextIndex-1] != numberArray[start]:
            numberArray[nextIndex] = numberArray[start]
            nextIndex += 1
    return nextIndex


print(f"Results Remove Duplicate: {removeDuplicates([2,3,3,4,5,6,9,9])}")


"""Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target. 
Write a function to return the indices of the two numbers 
(i.e. the pair) such that they add up to the given target.
"""
def pairWithTargetSum(arr: list[int], target: int ):
    endIndex = len(arr) - 1
    for startIndex in range(len(arr)):
        if arr[startIndex] + arr[endIndex] == target:
            return arr[startIndex], arr[endIndex]
        elif arr[startIndex] + arr[endIndex] > target:
            endIndex -= 1
        else:
            startIndex +=1

print("Pair With Target Sum: ", pairWithTargetSum([2,3,4,5,6,9], 11))
print("Pair With Target Sum: ", pairWithTargetSum([2,3,4,5,6,9], 11))


"""
Write a program thats return the pair target sum 
of an unsorted list containing duplicates 
"""

"""
1. sort the array in place 
2. grap the start and end index
3. loop the sorted array 
4. compare the sum of the values at the indices
5. return the result if the meet the target
"""
def pairTargetSum(arr: list[int], target: int) -> list[int]:
    arr.sort()
    endIndex = len(arr) - 1
    for start in range(len(arr)):
        if arr[start] + arr[endIndex] == target:
            return [arr[start], arr[endIndex]]
        elif arr[start] + arr[endIndex] > target:
            endIndex -= 1
        else:
            start +=1
            
print(f"pairtarget sum: {pairTargetSum([-3, 5, 4, 2, 3],2)}")
    
