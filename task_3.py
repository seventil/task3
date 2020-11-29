from threading import Thread
        

class MockOperation():
    def __init__(self):
        self.a = 0
    def function(self, arg):        
        for i in range(arg):                
            self.a += 1
                
mock_object = MockOperation()


def main():    
    threads = []
    for i in range(5):
        thread = Thread(target=mock_object.function, args=(100000,))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", mock_object.a)  # ???


main()
