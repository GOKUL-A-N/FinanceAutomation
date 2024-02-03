import csv

file = f"budget.csv"

transactions = []

def finance(file):
        
    with open(file , mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)


        global transactions

        

        for row in csv_reader:
            date = row[0]
            reason = row[1]
            creditamount = int(row[2])
            debitamount = int(row[3])

            reason = row[1].lower()

            transaction = ((date,reason,creditamount,debitamount))

            transactions.append(transaction)

        return transactions
    
def debit_and_credit(file):
    with open(file , mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        totalDebitedAmout = 0

        totalCreditedAmout = 0

        for row in csv_reader:
            creditamount = int(row[2])
            debitamount = int(row[3])
            totalDebitedAmout += debitamount

            totalCreditedAmout += creditamount

        return [totalCreditedAmout,totalDebitedAmout]

    
def category(file , categoryName = "credited"):
    with open(file , mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        categoryTotalAmount = 0

        for row in csv_reader:
            reason = row[1]
            debitamount = int(row[3])

            if reason == categoryName:
                categoryTotalAmount += debitamount
        
        return categoryTotalAmount


        
# print("Transaction History:",finance(file))

# print("Credit History:",debit_and_credit(file)[0])

# print("Debit History:",debit_and_credit(file)[1])

# print("Rent : " , category(file, "rent"))

   
def main():
    print("1 - Transaction History")
    print("2 - Total Amout Credit")
    print("3 -  Total Amout Debited")
    print("4 - Total amount spent on particular reason")

    option = int(input("Enter your Option"))



    match option:
        case 1:
            print("Transaction History:",finance(file))

        case 2:
            print("Credit History:",debit_and_credit(file)[0])

        case 3:
            print("Debit History:",debit_and_credit(file)[1])
    
        case 4:
            categoryName = input("Enter the category")
            result = category(file, categoryName.lower())  # Assuming `category` is a function
            print(categoryName , " is : ", result)

    to_continue =input("Would You like to continue yes or no ")

    if(to_continue.lower() == "yes"): main()    

main()