from services import add_transactions,view_transactions,show_summary,save_to_file,load_from_file
load_from_file()
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

    