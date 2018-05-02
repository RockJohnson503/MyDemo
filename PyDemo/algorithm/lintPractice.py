# encoding: utf-8

"""
File: lintPractice.py
Author: Rock Johnson
"""
from itertools import combinations

# 第K大的数
def kthLargestElement(k, A):
    return quik_sort_helper(A, 0, len(A) - 1, k)


def quik_sort_helper(lst, left, right, k):
    if left <= right:
        pivot = partition(lst, left, right)
        if pivot + 1 == k:
            return lst[pivot]
        elif pivot + 1 > k:
            return quik_sort_helper(lst, left, pivot - 1, k)
        else:
            return quik_sort_helper(lst, pivot + 1, right, k)


def partition(lst, left, right):
    mid = (left + right) // 2
    lst[mid], lst[right] = lst[right], lst[mid]
    boundary = left
    for i in range(left, right):
        if lst[i] > lst[right]:
            lst[i], lst[boundary] = lst[boundary], lst[i]
            boundary += 1
    lst[right], lst[boundary] = lst[boundary], lst[right]
    return boundary


# 合并排序数组2
def mergeSortedArray1(A, B):
    for i in range(len(B)):
        if A[-1] <= B[0]:
            A.append(B.pop(0))
        elif A[0] >= B[0]:
            A.insert(0, B.pop(0))
        else:
            left = 0
            right = len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] == B[0] or (A[mid] < B[0] and A[mid + 1] > B[0]):
                    A.insert(mid + 1, B.pop(0))
                    break
                elif A[mid] > B[0]:
                    right = mid - 1
                else:
                    left = mid + 1
    return A

def mergeSortedArray2(A, B):
    new_lst = []
    A_point = 0
    B_point = 0
    while A_point < len(A) or B_point < len(B):
        if A_point == len(A):
            new_lst.append(B[B_point])
            B_point += 1
        elif B_point == len(B):
            new_lst.append(A[A_point])
            A_point += 1
        elif A[A_point] <= B[B_point]:
            new_lst.append(A[A_point])
            A_point += 1
        else:
            new_lst.append(B[B_point])
            B_point += 1
    return new_lst


# 中位数
def median(nums):
    mid = len(nums) // 2 if len(nums) % 2 != 0 else len(nums) // 2 - 1
    return median_helper(nums, 0, mid, len(nums) - 1)

def median_helper(nums, low, mid, height):
    if low <= height:
        pivot = partition2(nums, low, height)
        if pivot == mid:
            return nums[mid]
        elif pivot < mid:
            return median_helper(nums, pivot + 1, mid, height)
        else:
            return median_helper(nums, low, mid, pivot - 1)

def partition2(nums, low, height):
    mid = (low + height) // 2
    nums[mid], nums[height] = nums[height], nums[mid]
    boundary = low
    for index in range(low, height):
        if nums[index] < nums[height]:
            nums[index], nums[boundary] = nums[boundary], nums[index]
            boundary += 1
    nums[height], nums[boundary] = nums[boundary], nums[height]
    return boundary

def strStr(source, target):
    si, ti, ri = 0, 0, -1
    while si != len(source):
        if source[si] == target[ti]:
            if ti == 0:
                ri = si
            si += 1
            ti += 1
        else:
            if ti == 0:
                si += 1
            ri = -1
            ti = 0
        if ti == len(target):
            break
    if ti < len(target):
        ri = -1
    return ri

def flatten(nestedList):
    res = []
    if isinstance(nestedList, int):
        res.append(nestedList)
    else:
        flatten_helper(nestedList, res)

    return res

def flatten_helper(lst, res):
    for i in lst:
        if isinstance(i, int):
            res.append(i)
        else:
            flatten_helper(i, res)

def maxSubArray(nums):
    old_max = nums[0]
    now_max = 0

    for i in range(len(nums)):
        now_max += nums[i]
        if now_max > old_max:
            old_max = now_max
        if now_max < 0:
            now_max = 0
    return old_max

def mergeSortedArray(A, m, B, n):
    i1 = 0
    i2 = 0
    rA = A[:m]
    for i in range(m + n):
        if i1 > m - 1:
            A[i] = B[i2]
            i2 += 1
        elif i2 > n - 1:
            A[i] = rA[i1]
            i1 += 1
        elif rA[i1] > B[i2]:
            A[i] = B[i2]
            i2 += 1
        else:
            A[i] = rA[i1]
            i1 += 1

def singleNumber(A):
    ans = 0
    for i in A:
        ans ^= i
    return ans

def minDistance(height, width, tree, squirrel, nuts):
    count = 0
    sq_to_tree = None
    for i in range(len(nuts)):
        nuts_to_tree = dis(tree, nuts[i])
        count += nuts_to_tree
        temp = dis(squirrel, nuts[i]) - nuts_to_tree
        if sq_to_tree == None or temp < sq_to_tree:
            sq_to_tree = temp

    return count * 2 + sq_to_tree

def dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def getSingleNumber(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == nums[mid - 1]:
            if (mid - 1 - left) % 2 != 0:
                right = mid - 2
            else:
                left = mid + 1
        elif nums[mid] == nums[mid + 1]:
            if (mid - left) % 2 != 0:
                right = mid - 1
            else:
                left = mid + 2
        else:
            return nums[mid]

def kthSmallest( matrix, k):
    if len(matrix) == 1:
        return matrix[0][k - 1]
    elif len(matrix[0]) == 1:
        return matrix[k - 1][0]

    indexs = [0 for i in range(len(matrix))]
    res = []

    while len(res) < k:
        now_min = matrix[-1][-1]
        for i in range(len(matrix)):
            if indexs[i] > len(matrix[0]) - 1:
                continue
            if matrix[i][indexs[i]] < now_min:
                now_min = matrix[i][indexs[i]]
                min_i = i
        indexs[min_i] += 1
        res.append(now_min)
    return res.pop()


# 动态规划 数字三角形
def minimumTotal(triangle):
    if triangle is None or len(triangle) == 0:
        return 0
    tmp = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            tmp[j] = min(tmp[j], tmp[j + 1]) + triangle[i][j]
    return tmp[0]



def uniquePaths(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    dp = [[(1 if j == 0 or i == 0 else None) for i in range(m)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]

def find_one(self, matrix):
    for i in matrix:
        for j in i:
            if j == 1:
                return True
    return False

def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid is None or len(obstacleGrid) == 0:
        return 0
    elif len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
        if find_one(obstacleGrid):
            return 0
        return 1

    dp = [[None for i in range(len(obstacleGrid[0]))] for j in
          range(len(obstacleGrid))]
    for i in range(len(dp)):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    for i in range(len(dp[0])):
        if obstacleGrid[0][i] == 1:
            break
        dp[0][i] = 1
    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[i])):
            if obstacleGrid[i][j] != 1:
                if dp[i][j - 1] == None:
                    dp[i][j] = dp[i - 1][j]
                elif dp[i - 1][j] == None:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1] if dp[-1][-1] != None else 0


# 背包问题 1.0
def backPack(m, A):
    res = []
    for i in range(len(A), 0, -1):
        for s in combinations(A, i):
            if sum(s) <= m:
                res.append(sum(s))
        if res != []:
            return max(res)


if __name__ == '__main__':
    print(backPack(12, [2, 3, 5, 7]))
    pass