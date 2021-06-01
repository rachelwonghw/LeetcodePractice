# to be optimized since it exceeded time limit
class Solution:
    def numSquares(self, n: int) -> int:
        
        def helper(n: int, perfect_squares: [], arr: {}):
            if n <= 0:
                return 0
            
            if n in arr:
                return arr[n]
            elif n in perfect_squares:
                arr[n] = 1
                return arr[n]
            
            
            index2 = len(perfect_squares) - 1
            count = math.inf
            while index2 >= 0:
                if perfect_squares[index2] <= n:
                    count = min(1 + helper(n-perfect_squares[index2], perfect_squares, arr), count)
                index2 -= 1
            
            arr[n] = count
            return arr[n]
        
        
        perfect_squares = []
        index = 1
        while pow(index,2) <= n:
            perfect_squares.append(pow(index, 2))
            index += 1
        
        arr = {}
        return helper(n, perfect_squares, arr)