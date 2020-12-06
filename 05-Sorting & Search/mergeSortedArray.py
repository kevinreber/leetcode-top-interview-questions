''' 88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:
    Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]
 
Constraints:
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n

'''

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if not nums1:
        return nums2

    if not nums2:
        return nums1

    i = 0
    j = 0

    results = []

    # build results list to copy
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            results.append(nums1[i])
            i += 1
        else:
            results.append(nums2[j])
            j += 1

    # append rest
    while i < m:
        results.append(nums1[i])
        i += 1

    while j < n:
        results.append(nums2[j])
        j += 1

    # replace original
    for k in range(n + m):
        nums1[k] = results[k]

    return nums1