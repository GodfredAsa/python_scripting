url = "https://itnext.io/sliding-window-algorithm-technique-6001d5fbe8b3"
import math
import unittest



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

# =================  DATA STRUCTURES AND ALGORITHMS ============================

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
print(f"Maximum Sum: {getMaxSum([3, 5, 2,10, 1, 7], 2)}")

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
            if len(result) > len(maxResult):
                maxResult = result
        else:
            result = ""
     
    return len(maxResult)

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
    return False   

print(f'Duplicate: {getDuplicates([5, 6, 8, 2, 4, 6, 9], 2)}')

"""
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray 
whose sum is greater than or equal to ‘S’. Return 0, 
if no such subarray exists.
"""

def smallest_subarray(array: list, s: int):
    start = 0
    window_sum = 0
    min_sum = math.inf
    
    for i in range(0, len(array)):
        window_sum  += array[i]
        while window_sum >= s:
            min_sum = min(min_sum, i - start + 1)
            window_sum -=array[start]
            start += 1
    return 0 if min_sum == math.inf else min_sum

print("Smallest Sub Array: ", smallest_subarray([2,1,5,2,3,2], 7))

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

"""
Given an array of characters where each character represents a 
fruit tree, you are given two baskets and your goal is to put 
maximum number of fruits in each basket. The only restriction 
is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop 
when you have to pick from a third fruit type.
    
This problem follows the Sliding Window pattern and is quite 
similar to Longest Substring with K Distinct Characters. 
In this problem, we need to find the length of the longest 
subarray with no more than two distinct characters (or fruit types!). 
This transforms the current problem into Longest Substring with
K Distinct Characters where K=2.
========  SAMPLE ======

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

def fruits_into_basket(fruits: list):
    start, max_length = 0, 0
    fruit_freq = {}
    
    for i in range(len(fruits)):
        right_fruit = fruits[i]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] +=1
        
        while len(fruit_freq) > 2:
            left_fruit = fruits[start]
            fruit_freq[left_fruit] -=1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            start +=1
        max_length = max(max_length, i - start + 1)
    return max_length
            