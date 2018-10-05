import csv
from MortgageData import MortgageData
from MortgageObservation import MortgageObservation

# format as id:Mortgage
mortgages = {}

dates = {}


def main():
    print "Beginning mortgage trader."
    dates["max"] = 0
    dates["min"] = 999
    read_data()
    get_max_and_min()
    get_default_rate_by_score(815)
    pass


def get_default_rate_by_score(score):
    defaults = 0
    count = 0

    for i in range(1, len(mortgages)):
        mortgage = mortgages[str(i)]
        if int(mortgage.fico) >= score:
            count += 1
            if mortgage.ever_defaulted:
                defaults += 1

    print str(defaults) + " defaulted, at " + str(float(defaults) / float(count)*100) + "%"
    pass


def get_max_and_min():
    print "MAX: " + str(dates["max"])
    print "MIN: " + str(dates["min"])
    default_count = 0
    success_count = 0

    fico_avg = 0
    fico_no_default_avg = 0
    fico_default_avg = 0

    no_default_threshold = 0

    for i in range(1, len(mortgages)):
        mortgage = mortgages[str(i)]

        fico_avg += int(mortgage.fico)

        if mortgage.ever_defaulted:
            default_count += 1
            fico_default_avg += int(mortgage.fico)
            if mortgage.distressed_success:
                success_count += 1
            # print str(i) + " DEFAULTED; FICO: " + mortgages[str(i)].fico

            if int(mortgage.fico) > no_default_threshold:
                no_default_threshold = int(mortgage.fico)
        else:
            fico_no_default_avg += int(mortgage.fico)
        pass

    print str(default_count) + ", or " + str(float(default_count) / float(50000)*100) + "% defaulted."
    # print str(success_count) + ", or " + str(float(success_count) / float(default_count)*100) + "% came out of default."

    fico_avg /= len(mortgages)
    fico_default_avg /= default_count
    fico_no_default_avg /= (len(mortgages)-default_count)

    print "Average FICO: " + str(fico_avg) + ", for those in default: " + str(fico_default_avg)
    print "For those who never defaulted: " + str(fico_no_default_avg)
    print "To never default: " + str(no_default_threshold)
    pass


def read_data():
    min_date = 999
    max_date = 0
    """ Reads data from csv. """
    with open('mortgage.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        mortgage_id = 0
        for row in csv_reader:
            if line_count == 0:
                print('Column names are  ' + ", ".join(row))
                line_count += 1
            else:
                if row[0] != mortgage_id:
                    mortgage_id = row[0]

                    # if problem with original interest rate, make it first observation's rate
                    if str(row[18]) == str(0):
                        # print mortgage_id
                        row[18] = row[7]

                    mortgages[mortgage_id] = MortgageData(row[0], row[2], row[14], row[16], row[17], row[18])

                if str(mortgages[mortgage_id].interest_orig) == str(0):
                    # print str(mortgage_id) + " " + str(mortgages[mortgage_id].interest_orig) + " "
                    mortgages[mortgage_id].interest_orig = row[7]
                    pass
                # print "Mortgage FICO = " + str(mortgages[mortgage_id].fico) + " = " + str(row[16])
                # print "Mortgage Interest Rate = " + str(mortgages[mortgage_id].interest_orig) + " = " + str(row[18])
                observation = MortgageObservation(row[0], row[1], row[5], row[6], row[7], row[9], row[10], row[22])
                mortgages[mortgage_id].add_observation(observation)

                if row[22] == str(1):
                    mortgages[mortgage_id].ever_defaulted = True

                if mortgages[mortgage_id].ever_defaulted == True and row[22] != str(1):
                    mortgages[mortgage_id].distressed_success = True

                if int(row[1]) > int(dates["max"]):
                    dates["max"] = row[1]

                if int(row[1]) < int(dates["min"]):
                    dates["min"] = row[1]

                line_count += 1
        print('Processed ' + str(line_count) + ' lines.')

        for i in range(1, len(mortgages)):
            if str(mortgages[str(i)].interest_orig) == str(0):
                print str(i) + " BAD RATE, INVALIDATING. "
                mortgages[str(i)].invalidate()
            pass

main()