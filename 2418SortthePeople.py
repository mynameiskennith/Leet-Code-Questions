class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for _, n in sorted(zip(heights, names), reverse=True)]

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict ={}
        n=len(heights)
        for i in range(n):
            dict[heights[i]]=names[i]
        
        heights.sort(reverse=True)
        for i in range(n):
            names[i] = dict[heights[i]]
        
        return names

        print(dict)