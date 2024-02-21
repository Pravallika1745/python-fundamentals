class BiggestNumber:
    def biggest_number(self, a, b, c):
        if a > b and a > c:
            print("a is bigger")
        elif b > c:
            print("b is bigger")
        else:
            print("c is bigger")


if __name__ == "__main__":
    # x = input("Enter the first number:")
    # y = input("Enter the second number:")
    # z = input("Enter the third number:")
    biggest_number = BiggestNumber()

    biggest_number.biggest_number(1, 2, 3)
