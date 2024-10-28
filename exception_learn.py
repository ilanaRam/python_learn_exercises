
def main(): 
    while True:
        try: 
            num_test_cases = input("Please enter number of test cases: ")
            if not num_test_cases.isnumeric():
                raise Exception(f"The input not numeric: {num_test_cases}")           
            
            num_test_cases = int(num_test_cases)
            if num_test_cases == 0 or num_test_cases < 0:
                raise Exception(f"The input is 0 or negative") 
            break    
        except Exception as ee:
            print(ee)
        finally: 
            continue
    print(f"Please enter {num_test_cases} of pairs (a b) folowed by enter ")
    while num_test_cases: 
        a , b = input().split()
        try: 
            res = int(a) / int(b)        
        except ZeroDivisionError as ee: 
            print(f"Error Code: {ee}") 
        except ValueError as ee:
            print(f"Error Code: {ee}") 

if __name__ == '__main__':
    main()