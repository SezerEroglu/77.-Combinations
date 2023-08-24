from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        returnArray = []
        arrayToAppend = [None] * k

        def arrayMaker(depth, nIndex):
            if depth + 1 >= k:
                returnArray.append(arrayToAppend.copy())
                return
            for number in range(nIndex, n + 1):
                arrayToAppend[depth + 1] = number
                arrayMaker(depth + 1, number + 1)

        for number in range(1, n + 1):
            arrayToAppend[0] = number
            arrayMaker(0, number + 1)

        return returnArray


Solution.combine(Solution, 5, 2)
