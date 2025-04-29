from datetime import datetime
from .utils import load_from_file, save_to_file, delete_from_file,write_csv_file
import time
from .decorators import log

class Transactions:

    # choose=input("what do you want debit/credit")
    # if choose == "credit":
    #     amount=int(input("enter the amount:"))
    #     d_amount=input("how the amount is credited, just for your idea")
    # elif choose == "debit":
    #     c=input("please say you want to spend in which type of category")

    def __init__(self,typee,amount,category,description,date=None):
        self.typee=typee
        self.amount=amount
        self.category=category
        self.description=description
        self.date=date

    @log
    def to_dict(self):
        return {
            "typee":self.typee,
            "amount":self.amount,
            "category":self.category,
            "description":self.description,
            "date":self.date
        }
    
    @classmethod
    @log
    def add_transaction(cls,typee,amount,category,description,date):
        transaction=cls(typee,amount,category,description,date)
        transaction_data=transaction.to_dict()
        save_to_file("transaction.json",transaction_data)

    
    @classmethod 
    @log  
    def remove_transcation(cls):
        delete_from_file("transaction.json")

    @classmethod 
    @log
    def view(cls):
        s=""
        s+="typee     amount     category     description      date \n"
        s+="----------------------------------------------\n"
        for i in load_from_file("transaction.json"):
            total_date=datetime.fromtimestamp(i["date"])
            total_datee=total_date.strftime("%B %d %Y, %H:%M")
            i["date"]=total_datee
            # i["date"]=datetime.now().strftime("%B %d %Y, %H:%M")
            for key,value in i.items():
                s+=f"{value}     "
            s+="\n"
        # return s 
        # print(s) 
        data_lines = s.strip().split("\n")
        # print(data_lines)
        list_of_lists = [line.strip().split("     ") for line in data_lines] 
        # print("====================================") 
        return list_of_lists

      

        # write_csv_file("view_transcations.csv",)

            # for txn in i:    
            #     print(*txn.values())
    


    def __str__(self):
        return f"the amount is {self.samount}"
    

   
   
        
      

        
       
