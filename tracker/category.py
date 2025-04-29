import json
from .utils import load_from_file, save_to_file, delete_from_file
from .decorators import log

class categories:
    
    @classmethod
    @log
    def add_new_category(cls):
        total=int(input("how many categories do you want, please provide me in count"))
        for i in range(total):
            provide_category=input("please provide the category : ")
            save_to_file("category.json",provide_category)

    @classmethod 
    @log
    def selection_category(cls):
        c=True
        data=load_from_file("category.json")
        while c:
            choose=input("please provide which category do you want from the list for transcation : ")
            if choose in data:
                break
            else:
                print("please provide me the correct category as you provided in the list")
                c=True  
        return choose
    
    @classmethod 
    @log
    def del_category(cls):
        del_par=input("please enter which category do you want to delete : ")
        data=load_from_file("category.json")
        for i in data:
            if i==del_par:
                data.remove(del_par)
        
        with open("category.json","w") as f:
            json.dump(data,f,indent=4)
                


                                  
                              



            
             
                  



       
