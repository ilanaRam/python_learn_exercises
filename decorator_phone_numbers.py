
# decorator
def check_format_phone_numbers(func):

    def wrapper(*args):
        # here the *args is a tuple where the input is first param - so we neet to extract it by [*args][0]
        # each param from input is string so need to convert to int
        # my_nums = [int(item) for item in [*args][0]]

        print("\n\nBefore calling 'func'")
        print(f"\n\nStart formating nums ....")
        formated_nums = []

        my_nums = [*args][0]
        # add here formating
        for num in my_nums:
            if len(num) < 10:
                print(f"The orig number is: {num},the number isn't valid {num}")
                formated_nums.append(None)
                continue
            if len(num) == 10:
                print(f"The orig number is: {num}, the formated number is:  +91 {num[:5]} {num[5:]}")
                formated_nums.append(f"+91 {num[:5]} {num[5:]}")
            elif len(num) == 11:
                if num[0] == '0':
                    print(f"The orig number is: {num}, the formated number is: +91 {num[1:6]} {num[6:]}")
                    formated_nums.append(f"+91 {num[1:6]} {num[6:]}")
                else:
                    print(f"The orig number is: {num},the number isn't valid {num}")
                    formated_nums.append(None)
                    continue
            elif len(num) == 12:
                if num[:2] == '91':
                    print(f"The orig number is: {num}, the formated number is: +{num[:2]} {num[2:7]} {num[8:]}")
                    formated_nums.append(f"+{num[:2]} {num[2:7]} {num[8:]}")
                else:
                    print(f"The orig number is: {num},the number isn't valid {num}")
                    formated_nums.append(None)
                    continue
            elif len(num) == 13:
                if num[:3] == '+91':
                    print(f"The orig number is: {num}, the formated number is: {num[:3]} {num[3:8]} {num[8:]}")
                    formated_nums.append(f"{num[:3]} {num[3:8]} {num[8:]}")
                else:
                    print(f"The orig number is: {num},the number isn't valid {num}")
                    formated_nums.append(None)
                    continue
        print(f"\n\nFinished formating nums ....")


        func(formated_nums)


        print("After calling 'func'")
    return wrapper

@check_format_phone_numbers
def print_phone_numbers(phone_nums_list):
    print(*phone_nums_list, sep='\n')


if __name__ == '__main__':
    phone_nums = ['7895',
                  '7895462130',
                  '07895462130',
                  '919875641230',
                  '+919875641230',
                  '9195969878']

    # decorated function
    print(f"\n\nOriginal nums are:")
    print(*phone_nums, sep='\n')

    print_phone_numbers(phone_nums)