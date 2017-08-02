#! /usr/bin/env python3 

from functools import reduce

import operator


class Solution:
    def generate(self, numRows):        
        def bin_coefficient(n, k):
            # @return c(n, k)
            if k == 0 or n==k:
                return 1
            elif k == 1 :
                return n
            return pascal_triangle[n-1][k]+ pascal_triangle[n-1][k-1]
                                                    
        pascal_triangle =[]
        for n in range(numRows):
            temRow=[]
            for k in range(n+1):
                temRow.append(bin_coefficient(n, k))
            pascal_triangle.append(temRow)

        return pascal_triangle

print (Solution().generate(991)[990][33])
