# TC: O(N(N+1)/2) => O(N^2)
# SC: O(1)
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        is_swap = False
        for j in range(0, i):
            if nums[j] < nums[j+1]:
                is_swap = True
                nums[j], nums[j+1] = nums[j+1], nums[j] 
        if is_swap == False:
            print(is_swap)
            break
    return nums

if __name__ == "__main__":
    # nums = [1,9,2,8,3,7,7,6,4,6,5,0]
    nums = [9,8,7,6,5,4,3,2,1,0]
    print(bubble_sort(nums))