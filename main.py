import datetime as dt
#The applicacion does not have tests
#Split the main.py file in three files, record.py, calculator.py and calories_calculator.py, cash_calculator.py

#It must be replace with a dataclass
class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount  # Validate amount is posive number.
        #Validate the correct date format. strptime throws an exception when formt is not correct
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())#Create a method to set the correct
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit # Validate limit is posive number.
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        #Create a variable today and use it
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount #User += operator
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):#remove extra perentesis. it does not clarify the operation.
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Documment class and its methods.
    def get_calories_remained(self):  # Gets the remaining calories for today
        x = self.limit - self.get_today_stats() # Use other name for this variable.
        if x > 0:
            #Do not use backslash
            return f'You can eat something else today,' \
                   f' but with a total calorie content of no more than {x} kcal'
        else:
            return('Stop eating!')


class CashCalculator(Calculator):
    # Documment class and its methods.
    # Create an enumeration with those values.

    USD_RATE = float(60)  # US dollar exchange rate.
    EURO_RATE = float(70)  # Euro exchange rate.
    
    #USD_RATE and EURO_RATE does not need as parameters. 
    #Those variables are memebers of the object.
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE): 
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00
            currency_type = 'rub'
        if cash_remained > 0:
            # Do not use functions inside a f-string.
            return (
                f'Left for today {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'No money, keep it up!'
        elif cash_remained < 0:
            return 'No money, keep it up:' \
                   ' your debt is - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)
    # This overwriting method does not need it.
    def get_week_stats(self):
        super().get_week_stats()
