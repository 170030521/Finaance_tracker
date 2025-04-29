import time
# print("Welcome to your Finance Tracker")
# income=int(input("please enter your monthly income"))
# choose=input("please enter which section do you want " \
# "if you want to add transcation type add_transcation" \
# "iif you want to delete transcation type delete_transcation" \
# "if you want to view transcation type view_transcation")
from tracker.transaction import Transactions
from tracker.finance import finance
from tracker.category import categories
from tracker.utils import write_csv_file

print("Welcome to Finance Tracket")

new=input("if you are new to the tracker, say \"new user\" or say \"old user\" : ")
if new=="new user":
    print("Can you please provide the pre defined category in the next section ex:shopping,food etc\nby this you can use it later for your transactions\nyou no need to enter everytime during the transactions\n")
    categories.add_new_category()
elif new=="old user":
    choice=input("do you want to add/delete particular category if not say \"no\" : ")
    if choice=="no":
        pass 
    elif choice=="add":
        categories.add_new_category()
    elif choice=="delete":
        categories.del_category()
    else:
        pass    


print("\nnow we will go to transactions")


choose=input("please enter \"add\" or \"delete\" or \"view\" or \"balance\"  or \"sort by month\"  or \"do you want transcations files in csv format then type csv\" :")
if choose=="add":
    c=categories.selection_category()
    Transactions.add_transaction("debit",500,c,"milk packets",int(time.time()))
elif choose=="delete":
    Transactions.remove_transcation()
elif choose=="view":
    all_transactions=Transactions.view()
    # print(Transactions.view())
    write_csv_file("all_transactions.csv",all_transactions)
elif choose=="balance":
    print(finance.balance()) 
elif choose=="sort by month":
    print(finance.sort_by_month())    
    
