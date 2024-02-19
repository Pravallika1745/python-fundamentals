class MathematicalOperations:
    def addition(self, number1, number2):
        sum_val = float(number1) + float(number2)
        print(sum_val)

    def average_marks(self, maths, science, physics):
        total_marks = float(maths) + float(science) + float(physics)
        average_marks = total_marks/3
        return average_marks


if __name__ == "__main__":
    mathematical_operations = MathematicalOperations()
    a = input('Enter the first number:')
    b = input('Enter the second number:')
    mathematical_operations.addition(a, b)
    x = input('enter the marks:')
    y = input('enter the marks:')
    z = input('enter the marks')
    result = mathematical_operations.average_marks(x, y, z)
    print(result)

