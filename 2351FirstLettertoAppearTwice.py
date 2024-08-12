class Solution:
    def repeatedCharacter(self, s: str) -> str:
        di = []
        for i in s:
            if i in di:
                return i
            else:
                di.append(i)

# IN C++
# class Solution {
#     public char repeatedCharacter(String s) {
#         boolean[] arr = new boolean[26]; // Array to keep track
#         for(char x: s.toCharArray()) // Iterate through each character in the string
#             if(arr[x - 'a']) // Check if the character has been seen before
#                 return x;  // If yes, return it
#             else arr[x - 'a'] = true; // If no, mark it as seen

#         return ' '; // Fallback (will never reach here as per problem statement)
#     }
# }