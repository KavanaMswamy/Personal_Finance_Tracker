transactions=[]
count=1

while count<=6:
    print("Welcome to Personal Finance Tracker")
    choice=input("Choose the service required from below options: 1.Enter Transactions 2.View Transactions 3.Show summary 4.Exit-> ")

    if choice=='1':
        print("Adding Transactions")
        amount=float(input("Enter amount->"))
        category=input("enter category->")
        type=input("Enter Income/Expences->")
        #creating a dictionary
        transaction={
            "Amount":amount,
            "Category":category,
            "Input type":type}
        
        transactions.append(transaction)
        
    elif choice=='2':
        print("Viewing Transactions")
        #print(transactions) # directly printing the list
        for transaction in transactions: #using the loop to take the dictionaries out of loop and print it seperately
            print("Amount",transaction["Amount"])
            print("Category",transaction["Category"])
            print("Input",transaction["Input type"])
            print("---------------------")

    elif choice=="3":
        if len(transactions)==0:
            print("No transactions found")
            continue
        print("Displaying the summary")
        total_income=0
        total_expence=0
        for transaction in transactions:
            if transaction["Input type"].lower()=="income":
                total_income+=transaction["Amount"]
            else:
                total_expence+=transaction["Amount"]

        print("Income=",total_income)
        print("Expence=",total_expence)
        print("Balance=",total_income-total_expence)

    elif choice=='4':
        print("Exiting")
        break
    else:
        print("Enter valid Choice")

    count=count+1