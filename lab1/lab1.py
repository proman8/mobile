import sys, csv

DEFAULT_NUMBER = "933156729"

def calculate(dictionary, phone_number):
    in_calls = 0
    sms = 0

    for row in dictionary:
        if row['msisdn_origin'] == phone_number:
            in_calls += float(row['call_duration'])
            sms += int(row['sms_number'])
    in_calls -= 20 if in_calls >= 20 else 0

    return (in_calls + sms) * 2

def main():
    csv_list = csv.DictReader(open("data.csv","r"))
    cost = calculate(csv_list, sys.argv[1] if len(sys.argv) == 2 else  DEFAULT_NUMBER)
    print('%.2f' % cost)

if __name__ == '__main__':
    main()