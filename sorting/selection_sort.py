# TC: O(N(N-1)/2) => O(N^2)
# SC: O(1)
def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        max_index = i
        for j in range(i+1, n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums
        
if __name__ == "__main__":
    nums = [1,9,2,8,3,7,7,6,4,6,5,0]
    print(selection_sort(nums))