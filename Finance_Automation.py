import csv

file = f"budget.csv"

transactions = []

totalDebitedAmout = 0.0

totalCreditedAmout = 0.0

categoryTotalAmount = 0.0

def finance(file):
        
    with open(file , mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        global totalDebitedAmout

        global categoryTotalAmount

        global totalCreditedAmout

        for row in csv_reader:
            date = row[0]
            reason = row[1]
            creditamount = float(row[2])
            debitamount = float(row[3])

            # totalDebitedAmout += debitamount

            # totalCreditedAmout += creditamount

            transaction = ((date,reason,creditamount,debitamount))

            transactions.append(transaction)

            totalCreditedAmout += creditamount

            totalDebitedAmout += debitamount

        finance = [transactions, totalDebitedAmout , totalCreditedAmout]

        return finance
        
print("Transaction History:",finance(file)[0])

print("Debit History:",finance(file)[1])

print("Credit History:",finance(file)[2])

   

        
        