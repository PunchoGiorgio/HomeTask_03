currency_exchange = [
    {"EUR": None, "UAH": 40.92, "GBP": 0.85, "CHF": 0.94, "USD": 1.08},
    {"EUR": 0.024, "UAH": None, "GBP": 0.021, "CHF": 0.023, "USD": 0.026},
    {"EUR": 1.17, "UAH": 47.96, "GBP": None, "CHF": 1.11, "USD": 1.26},
    {"EUR": 1.06, "UAH": 43.35, "GBP": 0.9, "CHF": None, "USD": 1.14},
    {"EUR": 0.93, "UAH": 37.96, "GBP": 0.79, "CHF": 0.88, "USD": None},
]

currency_list = ["EUR", "UAH", "GBP", "CHF", "USD"]


class Price:
    def __init__(
        self,
        flight_value: int = None,
        curr_flight: str = None,
        hotel_value: int = None,
        curr_hotel: str = None,
    ):
        self.flight_value: int = flight_value
        self.curr_flight: str = curr_flight
        self.hotel_value: int = hotel_value
        self.curr_hotel: str = curr_hotel

    def check_flight(self):
        currencies = list(currency_exchange[0].keys())

        if self.curr_flight not in currencies:
            return "Not available currency"

        else:
            return self.flight_value

    def check_hotel(self):
        currencies = list(currency_exchange[0].keys())

        if self.curr_hotel not in currencies:
            return "Not available currency"

        elif self.curr_hotel == obj_f.curr_flight:
            return self.hotel_value

        else:
            return round(
                self.hotel_value
                * currency_exchange[currency_list.index(self.curr_hotel)][
                    obj_f.curr_flight
                ]
            )

    def __sub__(self, other):
        return self.check_flight() - other.check_hotel()

    def __add__(self, other):
        return self.check_flight() + other.check_hotel()


obj_f = Price(flight_value=125, curr_flight="USD")
obj_h = Price(hotel_value=270, curr_hotel="UAH")

print(f"Result of operation is {abs(obj_f - obj_h)} {obj_f.curr_flight}")

print(f"Total sum is {obj_f + obj_h} {obj_f.curr_flight}")
