"""
    "1" => 땅
    "0" => 물
    동서남북 4가지 방향으로 물에 둘러쌓여야 섬
    섬의 개수 출력
"""
from typing import List

class Solution:

    # DFS BFS
    # grid의 모든 행을 순차적으로 돌면서
    # 행의 값이 1일 경우
    # 1. 지나온 행들은 0으로 바꾸고
    # 2. dfs() 함수를 호출해 상하좌우에 1이 있는지 확인.
    # 2-1. 1이 존재한다면 다시 dfs() 함수를 호출
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int):
            # if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            #     return

            grid[i][j] = "0"

            if i > 0 and grid[i-1][j] == '1':
                dfs(i-1, j)
            if j > 0 and grid[i][j-1] == '1':
                dfs(i, j-1)
            if i < len(grid)-1 and grid[i+1][j] == '1':
                dfs(i+1, j)
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                dfs(i, j+1)

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island += 1

        return island

    exam_1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    print(numIslands(exam_1))

    # print(numIslands(exam_1))
