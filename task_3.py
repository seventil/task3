import concurrent.futures
import itertools
        

class MockOperation():
    
    def __init__(self):
        self.a = itertools.count()
        
    def function(self, arg):        
        for i in range(arg):                
            next(self.a)
            
    def value(self):
        return self.a
                
mock_object = MockOperation()


def main():    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(5):
            executor.submit(mock_object.function, 1000000)
   
    print("----------------------", mock_object.value())


main()
