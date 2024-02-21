class PyramidShape:
    def pyramid_shape(self, num):
        num = int(input("Enter the number of rows:"))
        for i in range(0, num):
            for j in range(0, num - i - 1):
                print(end=" ")
            for j in range(0, i + 1):
                print("*", end=" ")
            print()


if __name__ == "__main__":
    pyramid_shape = PyramidShape()
    pyramid_shape.pyramid_shape(5)
