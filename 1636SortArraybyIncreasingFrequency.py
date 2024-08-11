class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        def get_element(element):
            return (count[element],-element)

        nums.sort(key=get_element)
        return nums
        