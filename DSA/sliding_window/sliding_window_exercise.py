def longestWord(s):
    result = ""
    maxResult = ""
    for i in range(len(s)):
        if s[i] not in ['a', 'e', 'i', 'o', 'u']:
            result += s[i]
            if len(result) > len(maxResult):
                maxResult = result 
        else:
            result = ""
    return f'Max consonant word in {s} is [{maxResult}] and of Characters: {len(maxResult)}'

print(longestWord('codeforintelligents'))


def getMinMaxDiff(array, target):
    start, windowSum, minSum, maxSum = 0, 0, float('inf'), 0
    for i in range(len(array)):
        windowSum += array[i]
        if i - start + 1 == target:
            maxSum = max(windowSum, maxSum)
            minSum = min(windowSum, minSum)
            windowSum -= array[start]
            start +=1
    print(f'Max: {maxSum}')
    print(f'Min: {minSum}')
    
    return (maxSum - minSum) / 2
    
print(getMinMaxDiff([3, 8, 9, 15], 2))

def findDuplicate(nums, target):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= target:
            return True
        else:
            d[nums[i]] = i
    return False
print(findDuplicate([5, 6, 2, 8, 2, 4, 4, 6, 9], 4))
