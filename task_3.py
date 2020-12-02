import concurrent.futures
import itertools
import queue


class MockOperation():

    def __init__(self):
        self.a = itertools.count()

    def function(self):
        next(self.a)


    def value(self):
        return self.a


def main():
    mock_object = MockOperation()
    q = queue.Queue()

    for _ in range(6):
        q.put(mock_object.function)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(5):
            executor.submit(q.get())

    print("----------------------", mock_object.value())


main()
