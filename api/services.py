from typing import List


def rotate_array(nums: List[int], k: int) -> List[int]:
    if not nums:
        return nums

    k = k % len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums


def find_kth_largest(nums: List[int], k: int) -> int:
    if not nums or k < 1 or k > len(nums):
        raise ValueError("Invalid input")

    def quickselect(nums: List[int], k: int) -> int:
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        if k <= len(left):
            return quickselect(left, k)
        elif k <= len(left) + len(mid):
            return pivot
        else:
            return quickselect(right, k - len(left) - len(mid))

    return quickselect(nums, k)


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp: dict[tuple[int, int], int] = {}

    def dfs(i: int, j: int, prev: float) -> int:
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= prev:
            return 0

        if (i, j) in dp:
            return dp[(i, j)]

        current = matrix[i][j]
        path = 1 + max(
            dfs(i + 1, j, current),
            dfs(i - 1, j, current),
            dfs(i, j + 1, current),
            dfs(i, j - 1, current),
        )
        dp[(i, j)] = path
        return path

    return max(dfs(i, j, float("-inf")) for i in range(rows) for j in range(cols))
