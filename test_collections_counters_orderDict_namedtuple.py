#! C:\Users\PRIVATE_ILANA\PHYTHON_HOW_TO\pythonProject\venv\Scripts\python.exe
from collections import Counter
from collections import OrderedDict
from collections import namedtuple
from tabulate import tabulate

# Counter - is a container that stores elements as dictionary keys, 
# and their counts are stored as dictionary values.

# OrderedDict - is a dictionary that remembers the order of the keys that were inserted first.

# namedTuple - it is turns tuples into convenient containers for simple tasks.
# so you don’t have to use integer indices for accessing members of a tuple.

def collection_counter_with_dict_example():
    posible_profit = 0

    shoes_sizes_available_dict = Counter([2,3,4,5,6,8,7,6,5,18])
    print(f"available shoes sizes: {shoes_sizes_available_dict}")

    desired_shues_and_prices_list = [(6,55),(6,45),(6,55),(6,55),(4,40),(18,60),(10,50)]
    print(f"desired shoes: {desired_shues_and_prices_list}")

    for desired_shoe in desired_shues_and_prices_list:
        
        desired_shoe_size = desired_shoe[0]
        price             = desired_shoe[1]
        amount_available  = shoes_sizes_available_dict[desired_shoe_size]

        if desired_shoe_size in shoes_sizes_available_dict.keys(): 
            print(f"Desired shoe size: {desired_shoe_size}, price: {price}")
            print(f"Amount available: {amount_available}")
            
            posible_profit += price
            shoes_sizes_available_dict[desired_shoe_size] -= 1

            if shoes_sizes_available_dict[desired_shoe_size] == 0: 
                shoes_sizes_available_dict.pop(desired_shoe_size) # remove by key
        
        print(f"The profit: {posible_profit}")

def collection_ordered_dict_example():
    products_and_prices_ordered_dict = OrderedDict()
    
    # products_and_prices_list = [('cola',55),('bisli',45),('kinli',55),('gaga',40),('bisli',45), ('bisli',45),('banana',50),('cola',55)]
    while True: 
        number_of_products = input("Please enter number of products: ")
        
        if str(number_of_products).isnumeric(): 
            number_of_products = int(number_of_products)
            print(f"The number_of_products: {number_of_products}")
            break     

    print(f"Please enter -purchased products-, prices followed by enter")
    while number_of_products: 
        product, productname2, price = input().split()
        product += " " + productname2

        if product.isnumeric() or not price.isnumeric(): 
            break 
        
        price = int(price)
        
        number_of_products -=1        
        products_and_prices_ordered_dict[product] = price
        print(f"the product: {product}, price: {price}")
    
    print(f"the Ordered dict is: ")
    for product_name, price in products_and_prices_ordered_dict.items():
        print(f"{product_name} {price}")
    
def named_tuple_simple_example():
    # create tuple Point type. Thast has 2 fields: x,y and a name Point 
    Point = namedtuple('Point','x,y')

    # create 2 variables of this tuple Pint: p1, p2 (each will have 2 fields: x,y)
    pt1 = Point(x = 1, y = 2) 
    pt2 = Point(x = 3, y = 4)
    dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
    print(f"The result is {dot_product}")
    # The result is 11


    # create named tuple type Car, define fields: Price, Mileage, Colour, Class 
    Car = namedtuple('Car','Price, Mileage, Colour, Class')
    
    # create vareable of type Car
    xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
    print(f"We defined a namedtuple type: {Car}")
    print(f"We created the variable of Car type -> xyz: {xyz}")
    print(f"Now lets access the field of variable xvz.Price: {xyz.Price}")

    # We defined a namedtuple type: <class '__main__.Car'>
    # We created the variable of Car type -> xyz: Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
    # Now lets access the field of variable xvz.Price: 100000


def named_tuple_excersize():
    Student = namedtuple('Student',
                         'Name, Id, Class, Marks')

    students_list = []
    num_of_students = 0

    sum_all_marks = 0
    num_of_students_tmp = 0
    
    while True:
        num_of_students_tmp = input("Enter number of students: ")
        if num_of_students_tmp.isnumeric and int(num_of_students_tmp) != 0 and int(num_of_students_tmp) > 0:
            num_of_students_tmp = int(num_of_students_tmp)
            num_of_students = num_of_students_tmp
            break    
    
    # here I add very first raw to the table - that will hold headers
    students_list.append(Student(Name  = 'NAME', 
                                 Id    = 'ID', 
                                 Class = 'CLASS', 
                                 Marks = 'MARK'))
    while num_of_students_tmp: 
        st_name, st_id, st_class, st_mark = input("Student details: name, id, class, mark (can be entered in any order)\n:").split()
        
        if st_name.isnumeric() or not st_id.isnumeric() or st_class.isnumeric() or not st_mark.isnumeric():
            continue
        
        st_id = int(st_id)
        st_mark = int(st_mark)

        sum_all_marks += st_mark

        student = Student(Name  = st_name, 
                          Id    = st_id, 
                          Class = st_class, 
                          Marks = st_mark)
        
        print(f"Added a student to a list: {student}")
        students_list.append(student)
        num_of_students_tmp -= 1
    
    print(f"These are all students: ")    
    print(tabulate(students_list, tablefmt='fancy_grid'))

    # calc average
    average = sum_all_marks / num_of_students
    print(f"Average is: {average}")



def main():    
    # collection_counter_with_dict_example()
    # collection_ordered_dict_example()
    # named_tuple_simple_example()
    named_tuple_excersize()
            

if __name__ == '__main__':
    main()