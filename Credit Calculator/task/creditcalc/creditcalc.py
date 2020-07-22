import math
import argparse
import sys


class CreditCalculator:

    overpayment = 0

    def __init__(self, pay, prd, prn, inst):
        self.payment = pay
        self.periods = prd
        self.principal = prn
        self.interest = inst

    def cal_differentiate_payment(self):
        interest_rate = self.interest / (12 * 100)
        for m in range(1, self.periods + 1):
            differentiate_payment = (self.principal / self.periods) + interest_rate * (
                    self.principal - (self.principal * (m - 1)) / self.periods)
            differentiate_payment = math.ceil(differentiate_payment)
            self.overpayment = self.overpayment + differentiate_payment
            print(f"Month {m}: paid out {differentiate_payment}")
        print()
        self.overpayment = self.overpayment - self.principal
        return self.overpayment

    def cal_annuity_payment(self):
        if self.principal != 0 and self.periods != 0:
            interest_rate = self.interest / (12 * 100)
            annuity_payment = self.principal * (
                    interest_rate * (1 + interest_rate) ** self.periods) / (
                                      (1 + interest_rate) ** self.periods - 1)
            annuity_payment = math.ceil(annuity_payment)
            print(f"Your annuity payment = {annuity_payment}!")

            self.overpayment = (annuity_payment * self.periods) - self.principal
            return self.overpayment

        elif self.interest != 0 and self.periods != 0:
            interest_rate = self.interest / (12 * 100)
            credit_principal = self.payment * (
                    (1 + interest_rate) ** self.periods - 1) / (
                    interest_rate * (1 + interest_rate) ** self.periods)
            credit_principal = math.floor(credit_principal)
            print(f"Your credit principal = {credit_principal}!")

            self.overpayment = (self.payment * self.periods) - credit_principal
            return self.overpayment

        else:
            interest_rate = self.interest / (12 * 100)
            periods = math.log((self.payment / (self.payment - (interest_rate * self.principal))),
                               (1 + interest_rate))
            periods = math.ceil(periods)
            year = periods // 12
            month = periods % 12
            if month > 1 and year > 1:
                print(f"You need {year} years and {month} months to repay this credit!")
            elif year > 1 and month == 0:
                print(f"You need {year} year to repay this credit!")
            else:
                print(f"You need {month} months to repay this credit!")

            self.overpayment = (self.payment * periods) - self.principal
            return self.overpayment


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="to get type of calculation")
    parser.add_argument("--payment", help="to get monthly_payment", type=int, default=0)
    parser.add_argument("--periods", help="to get count of months", type=int, default=0)
    parser.add_argument("--principal", help="to get credit_principal", type=int, default=0)
    parser.add_argument("--interest", help="to get credit_interest", type=float, default=0.0)
    args = parser.parse_args()

    option = args.type
    payment = args.payment
    months = args.periods
    principal = args.principal
    interest = args.interest

    overpayment = 0

    if len(sys.argv) < 5 or interest < 0 or principal < 0 or months < 0 or payment < 0 or \
            option != "annuity" and option != "diff":
        print("Incorrect parameters")

    else:
        credit_cal = CreditCalculator(payment, months, principal, interest)
        if option == "diff":
            overpayment = credit_cal.cal_differentiate_payment()
        else:
            overpayment = credit_cal.cal_annuity_payment()
        print(f"Overpayment = {overpayment}")

# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'

# write your code here
# print(credit_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

# credit_principal = int(input("Enter the credit principal: ").strip())
# option = input("""What do you want to calculate?
# type "m" - for count of months,
# type "p" - for monthly payment:
# """).strip()
# if option == "m":
#     monthly_payment = int(input("Enter monthly payment: ").strip())
#     months = round(credit_principal / monthly_payment)
#     if months > 1:
#         print(f"It takes {months} months to repay the credit")
#     else:
#         print(f"It takes {months} month to repay the credit")
# else:
#     periods = int(input("Enter count of months: ").strip())
#     payment = math.ceil(credit_principal / periods)
#     last_payment = credit_principal - (periods - 1) * payment
#     if payment == last_payment:
#         print(f"Your monthly payment = {payment}")
#     else:
#         print(f"Your monthly payment = {payment} with last month payment = {last_payment}.")

# option = input("""What do you want to calculate?
# type "n" - for count of months,
# type "a" - for annuity monthly payment,
# type "p" - for credit principal:
# """).strip()
# if option == "n":
#     credit_principal = float(input("Enter the credit principal: ").strip())
#     monthly_payment = float(input("Enter monthly payment: ").strip())
#     credit_interest = float(input("Enter credit interest: ").strip())
#
#     interest_rate = credit_interest / (12 * 100)
#     months = math.log((monthly_payment / (monthly_payment - (interest_rate * credit_principal))), (1 + interest_rate))
#     months = math.ceil(months)
#     year = months // 12
#     month = months % 12
#     if month > 1 and year > 1:
#         print(f"You need {year} years and {month} months to repay this credit!")
#     elif year > 1 and month == 0:
#         print(f"You need {year} year to repay this credit!")
#     else:
#         print(f"You need {month} months to repay this credit!")
#
# elif option == "a":
#     credit_principal = float(input("Enter the credit principal: ").strip())
#     periods = int(input("Enter count of periods: ").strip())
#     credit_interest = float(input("Enter credit interest: ").strip())
#
#     interest_rate = credit_interest / (12 * 100)
#     annuity_payment = credit_principal * \
#                       (interest_rate * (1 + interest_rate) ** periods) / ((1 + interest_rate) ** periods - 1)
#     annuity_payment = math.ceil(annuity_payment)
#     print(f"Your annuity payment = {annuity_payment}!")
#
# else:
#     monthly_payment = float(input("Enter monthly payment: ").strip())
#     periods = int(input("Enter count of periods: ").strip())
#     credit_interest = float(input("Enter credit interest: ").strip())
#
#     interest_rate = credit_interest / (12 * 100)
#     credit_principal = monthly_payment * \
#                        ((1 + interest_rate) ** periods - 1) / (interest_rate * (1 + interest_rate) ** periods)
#     credit_principal = math.floor(credit_principal)
#     print(f"Your credit principal = {credit_principal}!")
