def word_search(board, word):
    def backtrack(row, col, index):
        if index == len(word):
            return True

        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[0])
            or board[row][col] != word[index]
        ):
            return False

        # Mark the current cell as visited (to avoid revisiting it)
        temp, board[row][col] = board[row][col], "#"

        # Check neighbors in all four directions
        if (
            backtrack(row - 1, col, index + 1)
            or backtrack(row + 1, col, index + 1)
            or backtrack(row, col - 1, index + 1)
            or backtrack(row, col + 1, index + 1)
        ):
            return True

        # Restore the cell to its original value (backtrack)
        board[row][col] = temp
        return False

    for row in range(len(board)):
        for col in range(len(board[0])):
            if backtrack(row, col, 0):
                return True

    return False

# Example usage
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word1 = "ABCCED"  # Returns True
word2 = "SEE"    # Returns True
word3 = "ABCB"   # Returns False

print(word_search(board, word1))
print(word_search(board, word2))
print(word_search(board, word3))
