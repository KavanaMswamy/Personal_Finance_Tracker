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
    for index,transaction in enumerate(transactions): #using the loop to take the dictionaries out of loop and print it seperately
    #print(transactions) # directly printing the list
        print("Transaction ID : ",index)
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
    #income = sum(t["amount"] for t in transactions if t["type"] == "income")
    #expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    for transaction in transactions:
        if transaction["Input type"].lower()=="income":
            total_income+=transaction["Amount"]
        else:
            total_expence+=transaction["Amount"]

    print("Income=",total_income)
    print("Expence=",total_expence)
    print("Balance=",total_income-total_expence)

def update_transactions():
    view_transactions()

    try:
        index=int(input("Enter the Transaction ID to update: "))

        if index < 0 or index>= len(transactions):
            print("Invalid ID")
            return
        
        print("Leave blank/ just give enter - to keep old values")

        while True:
            try:
                amount=float(input("Enter amount->"))

                if amount <=0:
                    print("Amount must be greater than 0-")
                    continue

                break
            except ValueError:
                print("Please enter valid number")

        category=input("enter category->").strip()
           
        input_type=input("Enter Income/Expence->").strip().lower()

        if amount:
            transactions[index]["Amount"]=float(amount)
        if category:
            transactions[index]["Category"]=category
        if input_type in ["income","expence"]:
            transactions[index]["Input type"]=input_type

        save_to_file()
        print("Transaction updated successfully")

    except ValueError:
        print("Invalid Input")

def delete_transactions():
    view_transactions()

    try:
        index=int(input("Enter the Transaction ID to delete: "))

        if index < 0 or index>= len(transactions):
            print("Invalid ID")
            return
        
        print("Leave blank/ just give enter - to keep old values")

        transactions.pop(index)

        save_to_file()
        print("Transaction deleted successfully")

    except ValueError:
        print("Invalid Input")