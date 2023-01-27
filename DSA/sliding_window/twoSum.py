
def two_Sum(nums: list[int], target: int) -> list[int]:
    has_map = {}
    for i in range(len(nums)):
        if nums[i] in has_map:
            return [i, has_map[nums[i]]]
        else:
            has_map[target - nums[i]] = i

print(f"Two Sum: {two_Sum([1,4,10,-3], target = 14)}")


def removeDuplicates(numberArray: list[int]):
    start, nextIndex= 1, 1
    for start in range(len(numberArray)):
        if numberArray[nextIndex-1] != numberArray[start]:
            numberArray[nextIndex] = numberArray[start]
            nextIndex += 1
    return nextIndex


print(f"Results Remove Duplicate: {removeDuplicates([2,3,3,4,5,6,9,9])}")



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


"""
Write a program thats return the pait target sum of an unsorted list containing duplicates 
"""
