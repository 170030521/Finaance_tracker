from datetime import datetime

def log(func):
    def wrapper(*args,**kwargs):
        print(f"calling {func.__name__} with {args}, {kwargs} in this date {datetime.now().date()}")
        return func(*args,**kwargs)
    return wrapper 



# selection=log(selection)
# selection=wrapper

# selection()=wrapper()
# retutn 
# @log
# def test(arg):
#     return arg




# test = log(test)
# test = wrapper
