
class Car: 
    def __init__(self) -> None:
        self.color = None    
    

# pay attension this extern function can assecc to all fields of the delivered object  !!??!!
def change_to_any_given_color(vehicle, new_color="Blue"):    
    vehicle.color = new_color


def main():
    car_obj = Car() 
    print(f"car before setting colores: {car_obj.color}")    
    change_to_any_given_color(car_obj, # Car obj
                 "Red")   # color
    print(f"car after setting colores: {car_obj.color}")       
    
    print(f"car before setting colores: {car_obj.color}")
    change_to_any_given_color(car_obj)
    print(f"car after setting colores: {car_obj.color}")

   
    # --------------------
    # class EvenStream(object):
    #     def __init__(self):
    #         self.current = 0

    #     def get_next(self):
    #         to_return = self.current
    #         self.current += 2
    #         return to_return


    # class OddStream(object):
    #     def __init__(self):
    #         self.current = 1

    #     def get_next(self):
    #         to_return = self.current
    #         self.current += 2
    #         return to_return


    # def print_from_stream(n, stream=EvenStream):
    #     # Create an instance of the stream
    #     stream_instance = stream()
    #     for _ in range(n):
    #         print(stream_instance.get_next())


    # if __name__ == "__main__":
    #     print_from_stream(3)
    #     print_from_stream(3, stream=OddStream)

if __name__ == '__main__':
    main()




