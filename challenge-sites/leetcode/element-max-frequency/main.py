#!/usr/bin/env python3

"""
Goal: Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

Solved first in PHP. See that implementation for more in-depth goal details:
https://github.com/joneiros/php-sandbox/commit/4d4b8742bccebb6ca75b45f892c8c28ed4849fbe
"""

def main():
    #nums = [1,2,3,4,5]
    #nums = []
    nums = [1,2,2,3,1,4]
    # nums = [1, 1, 2, 2, 3, 3, 3, 1, 5, 5, 5]


    # print(maxFrequencyElements(nums))
    print(maxFrequencyElementsUsingArrays(nums))



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

"""
This next solution is a remix, based on this solution strategy:

- From the startingList, create a newList of unique values.
For each unique value, remove an instance of that value from the original list.
increment a countDuplicates counter.
Repeat this process until the startingList contains nothing, at which time you use newList as duplicatedNumbers
    - This one is less intuitive, and runs in O(n)^2, so even though I like it (it seems clever),
    it's not the best solution.

Because of Python's flexibility with remixing arrays, this solution may be quite elgant in Python,
though its time complexity still prevents it from being ideal.
"""

def maxFrequencyElementsUsingArrays(nums):
    numset = None
    countDuplicates = 0

    while nums != []:
        countDuplicates += 1
        numset = set(nums)

        for x in numset:
            nums.remove(x)

    return countDuplicates * (len(numset) if numset is not None else 0)

#---
main()