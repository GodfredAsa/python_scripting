"""
GET THE MAXIMUM SUM FROM SEQUENCE FOLLOWING EACH OTHER 
"""
def getMaxSum(array, target):
    windowSum, start, maxSum = [0,0,0]  
    for i in range(len(array)):
        windowSum +=array[i]
        if i - start + 1 == target:
            maxSum = max(maxSum, windowSum)
            windowSum -= array[start]
            start += 1
    return maxSum


def getMaxMinDIFF(array, target):
    windowSum, start, maxSum, minSum = [0,0,0,float('inf')]  
    for i in range(len(array)):
        windowSum +=array[i]
        if i - start + 1 == target:
            maxSum = max(maxSum, windowSum)
            minSum = min(minSum, windowSum)
            
            windowSum -= array[start]
            start += 1
    return (maxSum - minSum) /2

print(f"Max Min Difference: {getMaxMinDIFF([3, 8, 9, 15], 2)}")


print(f"Maximum Sum: {getMaxSum([3, 5, 2,10, 1, 7], 2)}")

"""
Difference between the maximum and minimum average of all k-length continuous subarrays
Input: arr[ ] = {3, 8, 9, 15}, K = 2
Output: 6.5
Explanation: All subarrays of length 2 are {3, 8}, {8, 9}, {9, 15} and their averages are (3+8)/2 = 5.5, (8+9)/2 = 8.5, and (9+15)/2 = 12.0 respectively.

Therefore, the difference between the maximum(=12.0) and minimum(=5.5) is 12.0 -5.5 = 6.5.

THE FUNCTION BENEATH FINDS DIFFERENCE BETWEEN 
THE SUM OF MAXIMUM AND MINIMU VALUES
"""
def getMinMaxDiff(arr, k):
    currSum = 0
    minSum = float("inf")
    maxSum = 0
    start = 0
    
    for i in range(len(arr)):
        currSum += arr[i]
        
        if (i - start + 1 == k):
            avg = currSum / k
            maxSum = max(avg, maxSum)
            minSum = min(maxSum, minSum)
            currSum -= arr[start]
            start += 1
    
    diff = maxSum - minSum
    return diff


"""
Find duplicates within a range ‘k’ in an array
Input: nums = [5, 6, 8, 2, 4, 6, 9]
k = 2
Ouput: False
"""

def getDuplicates(nums, k):
    d = {}
    
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k:
            return True
        else:
            d[nums[i]] = i
    print(d)
    return False   

print(f'Duplicate: {getDuplicates([5, 6, 8, 2, 4, 6, 9], 2)}')


"""
Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise
In other words, return true if one of s1’s permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

def checkInclusion(self, s1, s2):
    numbers = [0]*26
    numbers2 = [0]*26
    
    for c in s1:
        numbers[ord(c) - ord('a')] += 1
        
    for index in range(0, len(s2)):
        numbers2[ord(s2[index]) - ord('a')] += 1
        
        if index >= len(s1) - 1:
            if numbers == numbers2:
                return True
                
            numbers2[ord(s2[index - len(s1) + 1]) - ord('a')] -= 1
                
    return False



"""
Length of the longest substring that doesn’t contain any vowels
Input: s = "codeforintelligents"
Output: 3
Explanation: 'nts' is the longest substring that doesn't contain any vowels.
"""
def getLongestSubstring(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    maxResult = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            result += s[i]
            print(result)
            if len(result) > len(maxResult):
                maxResult = result
        else:
            result = ""
    
    return len(maxResult)