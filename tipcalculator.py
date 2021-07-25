print("Welcome to tip calculator")
bill=float(input("what was the total bill: "))
tip=int(input("what % would you like to give ?like 10% ,12%,15% : "))
people=int(input("how many people are gonna split the bill : "))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=total_tip_amount+bill
bill_per_person=total_bill/people
bill_to_pay=round(bill_per_person,2)
print(f"each have to pay {bill_to_pay}")