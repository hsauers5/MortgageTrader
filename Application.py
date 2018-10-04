import csv
from MortgageData import MortgageData
from MortgageObservation import MortgageObservation

# format as id:Mortgage
mortgages = {}


def main():
    print "Beginning mortgage trader."
    read_data()
    pass


def read_data():
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
                #print('\t' + row[0] + ' works in the ' + row[1] + ' department.')
                if row[0] != mortgage_id:
                    mortgage_id = row[0]
                    mortgages[mortgage_id] = MortgageData(row[0], row[2], row[14], row[16], row[17], row[18])

                print "Mortgage FICO = " + str(mortgages[mortgage_id].fico) + " = " + str(row[16])
                print "Mortgage Interest Rate = " + str(mortgages[mortgage_id].interest_orig) + " = " + str(row[18])
                observation = MortgageObservation(row[0], row[1], row[5], row[6], row[7], row[9], row[10], row[22])
                mortgages[mortgage_id].add_observation(observation)

                line_count += 1
        print('Processed ' + str(line_count) + ' lines.')
    pass


main()