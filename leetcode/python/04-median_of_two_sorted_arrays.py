def findMedian(nums1,nums2):
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    if len_nums1 > len_nums2:
        #asume nums2 is bigest nums1
        return findMedian(nums2, nums1)
    up = len_nums1
    down = 0
    h = 0
    while (down <= up):
        #begin set index
        i = (down + up) // 2
        j = (len_nums1 + len_nums2 + 1)//2 - i
        if i == 0: #out of range
            left_nums1 = nums2[0] 
        else:
            left_nums1 = nums1[i-1]   

        if i == len_nums1: #out of range
            right_nums1 = nums2[len_nums2 - 1] 
        else:
            right_nums1 = nums1[i]    

        if j == 0: #out of range
            left_nums2 = nums1[0] 
        else:
            left_nums2 = nums2[j-1]   

        if j == len_nums2: #out of range
            right_nums2 = nums1[len_nums1 - 1] 
        else:
            right_nums2 = nums2[j]    
        #end set index   

        #match condition to stop    
        if (left_nums1 <= right_nums2 and left_nums2 <= right_nums1):
            # len is even
            if (len_nums1 + len_nums2) % 2 == 0:
                return (max(left_nums1, left_nums2) + min(right_nums1, right_nums2))/2.0
            # len is odd
            else:
                return(max(left_nums1, left_nums2)/1.0)
        elif left_nums1 > right_nums2:
            step = (up - i) // 2
            if step == 0:
                up = i - 1
            else:
                up = i - step    
        else: 
            step = (i - down) // 2
            if step == 0:
                down = i + 1    
            else:
                down = i + step    


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return findMedian(nums1,nums2)




def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);
            
            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
