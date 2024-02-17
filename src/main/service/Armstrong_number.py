class ArmstrongNumber:
    def armstrong_num(self, number):
        n = int(input("Enter the given number: "))
        m = n
        sum_val = 0
        while n > 0:
            r = n % 10
            sum_val = sum_val + (r * r * r)

            n = n // 10
        if sum_val == m:
            print("Given number is a Armstrong number:")
        else:
            print("Given number is not an Armstrong number:")


if __name__ == "__main__":
     Armstrong_number= ArmstrongNumber()
     Armstrong_number.armstrong_num(34)




