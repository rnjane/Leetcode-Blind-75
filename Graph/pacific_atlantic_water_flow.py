import numbers


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        If the input is empty, immediately return an empty array.

        Initialize variables that we will use to solve the problem:

        Number of rows and columns in our matrix;
        2 queues, one for the Atlantic Ocean and one for the Pacific Ocean that will be used for BFS;
        2 data structures, again one for each ocean, that we'll use to keep track of cells we already visited, to avoid infinite loops;
        A small array [(0, 1), (1, 0), (-1, 0), (0, -1)] that will help with BFS.
        Figure out all the cells that are adjacent to each ocean, and fill the respective data structures with them.

        Perform BFS from each ocean. The data structure used to keep track of cells already visited has a double purpose - it also contains every cell that can flow into that ocean.

        Find the intersection, that is all cells that can flow into both oceans.

        DFS is very similar to BFS. Instead of using a queue and working iteratively, we'll use recursion. 
        Our dfs method will be called for every reachable cell. Note: we could also work iteratively with DFS, 
        in which case we would simply use a stack instead of a queue like in the Approach 1 code, with mostly everything else being identical to the BFS approach.
        """
        number_of_rows = len(heights)
        number_of_columns = len(heights[0])
        cells_visited_from_pacific_ocean = set()
        cells_visited_from_atlantic_ocean = set()

        def depth_first_search(row, column, visited_cells_set, previous_height_above_sea_level):
            if ((row, column) in visited_cells_set or 
               row < 0 or column < 0 or row == number_of_rows or column == number_of_columns or
               heights[row][column] < previous_height_above_sea_level):
                return
           
            visited_cells_set.add((row, column))
            depth_first_search(row + 1, column, visited_cells_set, heights[row][column])
            depth_first_search(row - 1, column, visited_cells_set, heights[row][column])
            depth_first_search(row, column + 1, visited_cells_set, heights[row][column])
            depth_first_search(row, column - 1, visited_cells_set, heights[row][column])

        for row_index in range(number_of_rows):
            depth_first_search(row_index, 0, cells_visited_from_pacific_ocean, 0)
            depth_first_search(row_index, number_of_columns - 1, cells_visited_from_atlantic_ocean, 0)

        for column_index in range(number_of_columns):
            depth_first_search(0, column_index, cells_visited_from_pacific_ocean, 0)
            depth_first_search(number_of_rows - 1, column_index, cells_visited_from_atlantic_ocean, 0)

        return list(cells_visited_from_pacific_ocean & cells_visited_from_atlantic_ocean)

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]: 
            return []
            
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return reachable
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))


class Solution:
    def pacificAtlantic(self, M):
        if not M or not M[0]: return []
        
        m, n = len(M[0]), len(M)
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited and M[dx][dy] >= M[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
                        
            return visited
        
        pacific  = [(0, i) for i in range(m)]   + [(i, 0) for i in range(1,n)]
        atlantic = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n-1)]
        
        return bfs(pacific) & bfs(atlantic)



"""
Complexity Analysis

Time complexity: O(M \cdot N)O(M⋅N), where MM is the number of rows and NN is the number of columns.

Similar to approach 1. The dfs function runs exactly once for each cell accessible from an ocean.

Space complexity: O(M \cdot N)O(M⋅N), where MM is the number of rows and NN is the number of columns.

Similar to approach 1. Space that was used by our queues is now occupied by dfs calls on the recursion stack.
"""