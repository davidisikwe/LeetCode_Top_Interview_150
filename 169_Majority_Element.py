class Solution:
    def return_key(self, myDict, max):
        for key, value in myDict.items():
            if value == max:
                return key

    def majorityElement(self, nums: List[int]) -> int:
        myDict= {}
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        majorElem= max(myDict.values())
        key= self.return_key(myDict, majorElem)
        return key

# Time Complexity- O(n)
# Space Complexity- O(n)

## Folow up using Boyle moore's voting algorithm 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate= 0
        count= 0
        for i in nums:
            if count == 0:
                candidate= i
                count += 1
            elif i == candidate:
                count += 1
            else:
                count -= 1
        return candidate

# Time Complexity- O(n)
# Space Complexity- O(1)
