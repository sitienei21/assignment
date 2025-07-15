class DateCalculator:
    def _init_(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.adjust_date()

    def adjust_date(self):
        # Adjust month and year for January and February
        if self.month < 3:
            self.month += 12
            self.year -= 1

    def calculate_weekday(self):
        # Calculate K and J
        K = self.year % 100
        J = self.year // 100

        # Zeller's Congruence formula
        h = (self.day + (13 * (self.month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

        # Mapping the result to the corresponding day of the week
        # 0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday
        days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days_of_week[h]

# Example usage
if __name__ == "_main_":
    date_calculator = DateCalculator(2025, 5, 19)
    day_of_week = date_calculator.calculate_weekday()
    print(f"The day of the week for the given date was: {day_of_week}")