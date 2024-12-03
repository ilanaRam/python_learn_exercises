class EvenStream(object):
    def __init__(self):
            self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
            self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

# non class function - that gets a number and class object and can access to any method of the class
def print_from_stream(n, stream_obj=EvenStream()):
        # isinstance - get name of the class without ()        
        if isinstance(stream_obj,EvenStream): 
             print("will be called fuctionality of EvenStream()")
        elif isinstance(stream_obj, OddStream): 
             print("will be called fuctionality of OddStream()")

        for _ in range(n): # from 0 till n-1
            res = stream_obj.get_next()
            print(f"number after get_next() is: {res}")

if __name__ == '__main__':

    queries = [('odd', 2),
               ('even', 3),
               ('odd', 5)]
        
    for stream,number in queries:
        if stream == "even":            
            print_from_stream(number) # call EvenStream by default
        
        elif stream =="odd": 
            print_from_stream(number, OddStream()) # here we deliver arguments: number and class object
