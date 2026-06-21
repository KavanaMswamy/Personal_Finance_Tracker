import json
transactions=[]
FILENAME="transactions.json"


def save_to_file():
    with open(FILENAME,'w') as file:
        json.dump(transactions,file,indent=4)

def load_from_file():
    global transactions
    try:
        with open(FILENAME,'r') as file1:
            transactions=json.load(file1)
    except FileNotFoundError:
        transactions=[]


def add_transactions():
    while True:
        try:
            amount=float(input("Enter amount -"))

            if amount <=0:
                print("Amount must be greater than 0-")
                continue

            break
        except ValueError:
            print("Please enter valid number")


    while True:
        category=input("enter category->").strip()
        #type=input("Enter Income/Expences->").strip()
        if not category:
            print("Please enter the category - it should not be empty")
        else:
            break
    
    while True:
        input_type=input("Enter Income/Expence->").strip().lower()

        if input_type not in ['income','expence']:
            print("Select Either Income/Expence")
        else:
            break
    
    #creating a dictionary
    transaction={
        "Amount":amount,
        "Category":category,
        "Input type":input_type}
        
    transactions.append(transaction)
    save_to_file()

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