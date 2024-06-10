class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(a+2,len(nums)):
                    for d in range(a+3,len(nums)):
                        if d > c and c > b and b > a:
                            if (nums[a] + nums[b] + nums[c]) == nums[d]:
                                count += 1
        return count
