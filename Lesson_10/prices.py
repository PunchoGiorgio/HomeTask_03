from dataclasses import dataclass

from convert import convert

middle_currency = "CHF"


@dataclass
class Price:
    value: int
    currency: str

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(value=(self.value + other.value), currency=self.currency)

        left_in_middle: float = convert(
            value=self.value, currency_from=self.currency, currency_to=middle_currency
        )

        right_in_middle: float = convert(
            value=other.value, currency_from=other.currency, currency_to=middle_currency
        )

        total_in_middle: float = left_in_middle + right_in_middle
        total_in_left_currency: float = convert(
            value=total_in_middle,
            currency_from=middle_currency,
            currency_to=self.currency,
        )

        return Price(value=total_in_left_currency, currency=self.currency)


flight = Price(value=200, currency="USD")
hotel = Price(value=500, currency="EUR")

total: Price = flight + hotel
print(total)
