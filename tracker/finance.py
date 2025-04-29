from datetime import datetime 
from .utils import load_from_file, save_to_file, delete_from_file

from . decorators import log

class finance:

    @log        
    @classmethod
    def balance(cls):
        bal=0
        for i in load_from_file("transaction.json"):
            if i["typee"]=="debit":
                bal=bal-int(i["amount"])
            else:
                bal=bal+int(i["amount"])
        return bal 
       
    @classmethod
    def sort_by_months(cls):
        c=0
        bal=0
        count=0
        g=0
        data=load_from_file("transaction.json")
        l=len(data[0])
        date=input("for which date you want the history  : ")
        month=input("for which month you want the history  : ")
        year=input("for which year you want the history  : ")
        date_time=f"{year}-{month}-{date}"
            # print(date_time)
        date_time1=datetime.strptime(date_time,"%Y-%m-%d")
        date_time2=int(date_time1.timestamp())       
        for j in load_from_file("category.json"):
            d=0
            cr=0
            for i in load_from_file("transaction.json"):
                    if int(i["date"])>date_time2 and int(i["date"]<date_time2+86400) and i["category"]==j:
                        g+=1
                        if i["type"]=="debit":
                                count+=1
                                bal=bal-int(i["amount"])
                                d+=int(i["amount"])
                                c+=1
                                    # print(f"you spend {d} in {i['category']} category")
                        elif i["type"]=="credit":
                                count+=1
                                bal=bal+int(i["amount"])
                                cr+=int(i["amount"])
                                c+=1
                                    # print(f"you spend {cr} in {i['category']} category")

            if(count==g and count!=0 and g!=0 ):
                if d==0:
                     print(f"you gained {cr} in {j} category") 
                elif cr==0:
                     print(f"you spend {d} in {j} category")
                else:
                     print(f"you gained {cr} in {j} category")
                     print(f"you spend {d} in {j} category")
                          
                             

            

        # for i in load_from_file("transaction.json"):
        #     if int(i["date"])>date_time2 and int(i["date"]<date_time2+86400):
        #         print(f"you spend {i['amount']} in {i['category']} category")

        return f"there are total {c} transactions and current balance is {bal} for this month"
    
    @log
    @classmethod
    def sort_by_month(cls):
        s=""
        c=0
        bal=0
        date=input("Enter date in YYYY-MM-DD format: ")
        date=int(datetime.strptime(date,"%Y-%m-%d").timestamp())
        filtered_transactions = [
            t for t in load_from_file("transaction.json")
            if t["date"] > date and t["date"] < date + 86400
        ]
        category_credit_map = {}
        category_debit_map = {}
        for transaction in filtered_transactions:
            if(
                transaction["typee"] == "credit"
                and transaction["category"] not in category_credit_map
            ):
                 category_credit_map[transaction["category"]]=int(transaction["amount"])
            elif(
                 transaction["typee"] == "credit"
                 and transaction["category"] in category_credit_map
            ):
                #  category_credit_map[transaction["category"]]=category_credit_map[transaction["category"]]+transaction["amount"]
                 category_credit_map[transaction["category"]] = int(category_credit_map[transaction["category"]]) + int(transaction["amount"])
            elif(
                transaction["typee"] == "debit"
                and transaction["category"] not in category_debit_map
            ):
                 category_debit_map[transaction["category"]]=int(transaction["amount"])
            elif(
                 transaction["typee"] == "debiit"
                 and transaction["category"] in category_debit_map
            ):
                 category_debit_map[transaction["category"]]=int(category_credit_map[transaction["category"]])-int(transaction["amount"])

        for key,value in category_credit_map.items():
             s+=f"you have credited {value} in {key} category\n"
             bal+=value
        for key,value in category_debit_map.items():
             s+=f"you have debited {value} in {key} category\n" 
             bal-=value
        s+=f"there are total {len(filtered_transactions)} transactions and current balance is {bal} for this month"      
        return s              
        
                
                
                  
                             


# date=input("for which date you want the history  : ")
# month=input("for which month you want the history  : ")
# year=input("for which year you want the history  : ")
# date_time=f"{year}-{month}-{date}"
#         # print(date_time)
# date_time1=datetime.strptime(date_time,"%Y-%m-%d")
# date_time2=int(date_time1.timestamp())       
# for j in load_from_file("category.json"):
#     for i in load_from_file("transaction.json"):
#             if int(i["date"])>date_time2 and int(i["date"]<date_time2+86400):
#                 if i["type"]=="debit" and i["category"]==j:
#                         bal=bal-int(i["amount"])
#                         d+=int(i["amount"])
#                         print(f"you spend {d} in {i['category']} category")
#                 else:
#                         bal=bal+int(i["amount"])
#                         cr+=int(i["amount"])
#                         print(f"you earned {cr} in {i['category']} category") 

# c=0
#         bal=0
#         d=0
#         cr=0
#         date=input("for which date you want the history  : ")
#         month=input("for which month you want the history  : ")
#         year=input("for which year you want the history  : ")
#         date_time=f"{year}-{month}-{date}"
#         # print(date_time)
#         date_time1=datetime.strptime(date_time,"%Y-%m-%d")
#         # print(date_time1)
#         date_time2=int(date_time1.timestamp())
#         for i in load_from_file("transaction.json"):
#             if int(i["date"])>date_time2 and int(i["date"]<date_time2+86400): 
#                 # print(f"you spend {i['amount']} in {i['category']} category")
#                 c+=1
#                 for j in load_from_file("category.json"):
#                     if i["type"]=="debit" and i["category"]==j:
#                         bal=bal-int(i["amount"])
#                         d+=int(i["amount"])
#                         print(f"you spend {d} in {i['category']} category")
#                     else:
#                         bal=bal+int(i["amount"])
#                         cr+=int(i["amount"])
#                         print(f"you earned {cr} in {i['category']} category")

#         # for i in load_from_file("transaction.json"):
#         #     if int(i["date"])>date_time2 and int(i["date"]<date_time2+86400):
#         #         print(f"you spend {i['amount']} in {i['category']} category")

#         return f"there are total {c} transactions and current balance is {bal} for this month"                         


