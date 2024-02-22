class RightTriangleShape:
    def right_triangle_shape(self, num):
        num = int(input("enter the number of rows:"))
        for i in range(1, num+1):
            for j in range(1, i + 1):
                print(i, end="")
            print()


if __name__ == "__main__":
    right_triangle_shape = RightTriangleShape()
    right_triangle_shape.right_triangle_shape(5)
