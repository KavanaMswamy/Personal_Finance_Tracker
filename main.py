transactions=[]

def add_transactions():
    amount=float(input("Enter amount->"))
    category=input("enter category->")
    type=input("Enter Income/Expences->")
    #creating a dictionary
    transaction={
        "Amount":amount,
        "Category":category,
        "Input type":type}
        
    transactions.append(transaction)

def view_transactions():
    if len(transactions)==0:
        print("No transactions found")
        return
    print("Viewing Transactions")
    for transaction in transactions: #using the loop to take the dictionaries out of loop and print it seperately
    #print(transactions) # directly printing the list
        print("Amount : ",transaction["Amount"])
        print("Category : ",transaction["Category"])
        print("Input : ",transaction["Input type"])
        print("---------------------")   

def show_summary():
    if len(transactions)==0:
        print("No transactions found")
        return
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

while True:
    print("Welcome to Personal Finance Tracker")
    choice=input("Choose the service required from below options: 1.Enter Transactions 2.View Transactions 3.Show summary 4.Exit-> ")

    if choice=='1':
        print("Adding Transactions")
        add_transactions()
        
    elif choice=='2':
        view_transactions()
        
    elif choice=="3":
        show_summary()

    elif choice=='4':
        print("Exiting")
        break
    else:
        print("Enter valid Choice")

    