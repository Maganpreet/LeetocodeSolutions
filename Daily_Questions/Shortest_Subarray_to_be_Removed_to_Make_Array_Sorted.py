class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr)-1
        while right >= 1:
            if arr[right] < arr[right-1]:
                break
            right -= 1
        shortest = right

        while left < right and (left == 0 or arr[left-1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            shortest = min(shortest, right-left-1)
            print(shortest,left,right)
            left += 1

        return shortest
    
sol = Solution()
inp = [
    [1,2,3,10,4,2,3,5],
    [5,4,3,2,1],
    [1,2,3],
    [2,3,5,4,2,2,3,3,4,4,5,6],
    [2,2,2,1,1,1]
]

for i in inp:
    print(f"length of shortest subarray to be removed {i} : ", sol.findLengthOfShortestSubarray(i))


