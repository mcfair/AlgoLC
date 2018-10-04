def search(self, nums, target):
      if not nums: return -1
      l, r = 0, len(nums)
      while l<r:
          mid = (l+r)//2

          if nums[mid]==target:
              return mid
          if nums[mid]<target:
              l= mid+1
          else:
              r = mid
      return -1
