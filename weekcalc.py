class DateCalculator:

    def __init__(self, year: int, month: int, day: int):

        self.year = year

        self.month = month

        self.day = day



    def calculate_weekday(self) -> int:

        year = self.year

        month = self.month

        day = self.day



        y_of_century = year % 100

        zb_century = year // 100



        if month < 3:

            month += 12

            year -= 1

        weekday = (day + (13 * (month + 1)) // 5 + y_of_century + (y_of_century // 4) + (zb_century // 4) + 5 * (

            zb_century)) % 7

        return weekday

    def weekday_name(self) -> str:

        weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        return (weekdays[self.calculate_weekday()])

date: DateCalculator = DateCalculator(2025, 4, 26)

print(date.calculate_weekday())

print(date.weekday_name())