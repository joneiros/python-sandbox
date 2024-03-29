#!/usr/bin/env python3

"""
Goal: Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

Solved first in PHP. See that implementation for more in-depth goal details:
https://github.com/joneiros/php-sandbox/commit/4d4b8742bccebb6ca75b45f892c8c28ed4849fbe
"""

def main():
    #nums = [1,2,3,4,5]
    #nums = []
    #nums = [1,2,2,3,1,4]
    nums = [1, 1, 2, 2, 3, 3, 3, 1, 5, 5, 5]


    print(maxFrequencyElements(nums))


def maxFrequencyElements(nums):
    if nums == []:
        return 0

    countDuplicates = 1
    duplicatedNums = []

    #list.sort(nums) #also works, gets around the lack of type inferrence
    nums.sort()

    tmpCount = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            tmpCount = 1
            continue

        tmpCount += 1

        if tmpCount > countDuplicates:
            countDuplicates = tmpCount
            duplicatedNums = [nums[i]]
        elif tmpCount == countDuplicates:
            duplicatedNums.append(nums[i])

    #edge case where no numbers are repeated
    if len(duplicatedNums) == 0:
        return len(nums)

    return len(duplicatedNums) * countDuplicates

#---
main()