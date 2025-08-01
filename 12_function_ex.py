def ps_str(str):
    print(str)

ps = ps_str("Hello world")
print(ps)

def custom_func(cust_id, cust_name):
    print("This function prints Customer id and Name")
    print("customer id:", cust_id)
    print("customer name:", cust_name)
    return 

cd = custom_func(101, "Peter Parker")
custom_func(cust_name="Mary Jane", cust_id=102)

def cust_bio(cust_name, cust_age=62):
    print("This function prints Customer Name and Age")
    print("customer name:", cust_name)
    print("customer age:", cust_age)
    return
cust_bio("Aunt May")

def cust_meta(cust_name, *var_tup):
    print("This fuction prints customer Names and lenth of the tuple")
    print("lenth of the tuple",len(var_tup))
    print("customer name:", cust_name)
    for var in var_tup:
        print(var)
        
    return
cust_meta("Peter Parker","Uncle Ben", "Mary Jane", "Aunt May")
