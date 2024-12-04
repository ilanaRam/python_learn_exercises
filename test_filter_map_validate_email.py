import re

def simple_filter_try(): 

    list_items = list(range(10))
    print(f"list of items 0:10: {list_items}")
    
    list_items = list(map(lambda x:x*x, list_items))
    print(f"list of items x*x: {list_items}")

    # filter delivers items that answers the condition/s = True 
    list_items = list(filter(lambda x: x > 10 and x < 80, 
                             list_items))
    print(f"list of only x> 10 and  x< 80: {list_items}")

def validation_func(email_str): 
    if email_str is None: 
        return False
    elif len(email_str) == 0: 
        return False
    elif '@' not in email_str: 
        return False
    elif '.' not in email_str: 
        return False
    
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_str):                                                
        return True    
    return False

def filter_email(all_emails):
    return list(filter(validation_func, all_emails))
    


if __name__ == '__main__': 
    emails = ["lara@hackerrank.com",
              "brian-23@hackerrank.com",
              "britts_54@hackerrank.com",
              "koko",
              "@",
              ".",
              ""]
    
    # n = int(input("Enter"))

    # for _ in range(n): 
    #     emails.append(input("enter email address: "))
    # print(f"The emails are: {emails}")
    
    emails = filter_email(emails)
    print(f"The filtered emails are: {emails}")

