class LeapYearService:

    def is_leap(self, year):
        leap = False

        # Write your logic here
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

        return leap


if __name__ == "__main__":
    leap_year_service = LeapYearService()
    result = leap_year_service.is_leap(2024)
    print(result)
