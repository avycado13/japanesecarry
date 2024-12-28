class Currency:
    def __init__(self, name: str, symbol: str, amount: float):
        self.name = name
        self.symbol = symbol
        self.amount = amount


class ExchangeRate:
    def __init__(self, currency1: Currency, currency2: Currency, rate: float, fee: float = 0.0, fee_type: str = 'percentage'):
        self.currency1 = currency1
        self.currency2 = currency2
        self.rate = rate
        self.fee = fee
        self.fee_type = fee_type

    def apply_fee(self, amount: float) -> float:
        """
        Apply the conversion fee to the amount.
        Fee can be either a fixed amount or a percentage.
        """
        if self.fee_type == 'fixed':
            return amount - self.fee
        elif self.fee_type == 'percentage':
            return amount * (1 - self.fee)
        else:
            raise ValueError("Unknown fee type. Use 'fixed' or 'percentage'.")

    def convert(self) -> float:
        """
        Converts amount from currency1 to currency2 based on the exchange rate,
        applying the conversion fee and the carry function of the target currency.
        """
        # Apply the fee before conversion
        amount_after_fee = self.apply_fee(self.currency1.amount)
        
        # Convert the amount
        converted_amount = amount_after_fee * self.rate
        self.currency2.amount = converted_amount
        return converted_amount
    
class MarketReturn:
    def __init__(self, currency: Currency, return_rate: float):
        self.currency = currency
        self.return_rate = return_rate

    def calculate_return(self, years: int) -> float:
        """
        Calculate the market return based on principal amount, return rate, and duration.
        """
        # Assuming simple interest for demonstration
        return self.currency.amount * (1 + (self.return_rate / 100) * years)

class Loan:
    def __init__(self, currency: Currency, principal: float, annual_interest_rate: float, duration_years: int):
        self.currency = currency
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.duration_years = duration_years

    def calculate_total_repayment(self) -> float:
        """
        Calculate the total repayment amount for the loan.
        Using simple interest for demonstration.
        """
        return self.principal * (1 + (self.annual_interest_rate / 100) * self.duration_years)


yen = Currency(name='Japanese Yen', symbol='¥',amount=(1.5*10**6))
usd = Currency(name='US Dollar', symbol='$',amount=0)
print(f"start with {yen.amount} Yen")

exchange_rate = ExchangeRate(currency1=yen, currency2=usd, rate=0.1, fee=0.02, fee_type='percentage')
exchange_rate.convert()
print(f"Post Conversion USD: {usd.amount}")

# Loan
loan = Loan(currency=yen, principal=(1.5*10**6), annual_interest_rate=3.0, duration_years=1)
total_repayment = loan.calculate_total_repayment()
print(f"Total repayment amount for the loan is {total_repayment} Yen")

# Market Return
market_return = MarketReturn(currency=usd, return_rate=7.0)
years = 1
return_on_investment = market_return.calculate_return(years)
print(f"Investment of ${usd.amount} USD will grow to ${return_on_investment} USD in {years} years")
usd.amount = return_on_investment
print(f"USD Amount: {usd.amount}")

exchange_rate = ExchangeRate(currency1=usd, currency2=yen, rate=10.00, fee=2.0, fee_type='percentage')
exchange_rate.convert()
print(f"Post Conversion yen {yen.amount}")

profit = total_repayment - return_on_investment
print(profit)