class MortgageObservation:
    # Holds important data for single instance.

    borrower_id = 0
    observation_time = 0
    balance = 0
    ltv = 0
    interest_rate = 0
    gdp_time = 0
    uer_time = 0
    status = 0

    # ID, time index, remaining balance, remaining LTV, current interest rate, GDP growth,
    # unemployment, default(1), payoff(2), neither (0)

    def __init__(self, borrower_id, observation_time, balance, ltv, interest_rate, gdp_time, uer_time, status):
        self.borrower_id = borrower_id
        self.observation_time = observation_time
        self.balance = balance
        self.ltv = ltv
        self.interest_rate = interest_rate
        self.gdp_time = gdp_time
        self.uer_time = uer_time
        self.status = status
        pass

    def get_timestamp(self):
        return self.observation_time