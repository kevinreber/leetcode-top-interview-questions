''' 387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode"
    return 2.

Note: You may assume the string contains only lowercase English letters.
'''

def firstUniqChar(s):
    # create dictionary containing count of each char in s
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

print(firstUniqChar('leetcode')) # 0
print(firstUniqChar('loveleetcode')) # 2