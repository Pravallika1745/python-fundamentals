class PrimeNumberService:

    def is_prime(self, number):
        count = 0
        for i in range(2, number):
            if (number % 2) == 0:
                count = count + 1
                break
        if count == 0:
            print("The given is prime number")
        else:
            print("The given is not a prime number")


if __name__ == "__main__":
    number = 4
    prime_number_service = PrimeNumberService()
    prime_number_service.is_prime(number)
