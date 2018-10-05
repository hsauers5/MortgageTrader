class MortgageData:

    observations = []
    borrower_id = ""
    origination_time = 0
    is_investor = 0
    fico = 900
    ltv_orig = 0
    interest_orig = 0

    ever_defaulted = False
    distressed_success = False

    is_valid = True

    def __init__(self, borrower_id, origination_time, is_investor, fico, ltv_orig, interest_orig):
        self.borrower_id = borrower_id
        self.origination_time = origination_time
        self.is_investor = is_investor
        self.fico = fico
        self.ltv_orig = ltv_orig
        self.interest_orig = interest_orig
        pass

    def add_observation(self, observation):
        self.observations.append(observation)
        pass

    def invalidate(self):
        self.is_valid = False

    default = False


    def has_defaulted(self):
        for i in range(0, len(self.observations)):
            if self.observations[i].status == 1:
                self.ever_defaulted = 1
                self.default = True
            pass
        return self.default
