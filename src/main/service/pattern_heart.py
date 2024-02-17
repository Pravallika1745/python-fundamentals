class PatternHeart:
    def print_heart_formation(self, row_val, col_val):
        for row in range(row_val):
            for col in range(col_val):
                if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


if __name__ == "__main__":
    pattern_heart = PatternHeart()
    pattern_heart.print_heart_formation(6, 7)
