

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # Keep track of the numbers that have been seen before to detect cycles
#         seen = set()
        
#         while n != 1:
#             # If we've seen this number before, it means we're in a cycle
#             if n in seen:
#                 return False
#             seen.add(n)
            
#             # Calculate the sum of the squares of the digits
#             new_n = 0
#             while n > 0:
#                 digit = n % 10
#                 new_n += digit * digit
#                 n //= 10
#             n = new_n
        
#         return True