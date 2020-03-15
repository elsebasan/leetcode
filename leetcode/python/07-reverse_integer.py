class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = - pow(2,31) 
        MAX_INT = - MIN_INT - 1
        if x < 0:
            y = -x
        else:
            y = x
        reverse = 0
        while y > 0:
            reverse = reverse  * 10
            reverse = reverse + y % 10
            y = y // 10
        if x < 0:
            reverse = -reverse
        if MIN_INT <= reverse <= MAX_INT:
            return (reverse)
        else:
            return 0
