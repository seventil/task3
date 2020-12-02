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


def scheduler(queue: queue.Queue, function_to_schedule, arg=None):
    if arg is None:
        queue.put(function_to_schedule)
    else:
        for _ in range(arg):
            queue.put(function_to_schedule)


def main():
    mock_object = MockOperation()
    q = queue.Queue()

    scheduler(q, mock_object.function, 5)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(5):
            executor.submit(q.get())

    print("----------------------", mock_object.value())


main()
