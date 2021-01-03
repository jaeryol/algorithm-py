"""
자신을 제외한 배열의 곱
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

example)
input  -> [1, 2, 3, 4]
output -> [24, 12, 8, 6]

키 포인트
나눗셈을 하지 않고 O(n)에 풀이하라.
"""
import math
from typing import List


# 바로 떠올르는 문제 풀이 하지만, 나눗셈을 하지 않고 풀라는 문제의 조건이 있다.
def solving(nums: List[int]) -> List[int]:
    result = []
    total = math.prod(nums)
    for n in nums:
        result.append(int(total/n))

    return result


def product_except_self(nums: List[int]) -> List[int]:
    p = 1
    out = []
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
        print(p)


# print(solving([1, 2, 5, 6 ]))
print(product_except_self([1, 2, 5, 6]))
