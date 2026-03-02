def reverseArray(nums, left, right):
    if left >= right:
        return 
    nums[left], nums[right] = nums[right], nums[left]
    reverseArray(nums, left+1, right-1)

if __name__ == "__main__":
    nums = [2,4,1,7,6,3,8,9,5]
    reverseArray(nums, 2, 5)
    print(nums)