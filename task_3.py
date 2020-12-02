import concurrent.futures
import queue
from threading import Thread


class MockOperation:

    def __init__(self):
        self.a = 0

    def function(self):
        self.a += 1

    def value(self):
        return self.a


def scheduler(q: queue.Queue, function_to_schedule, arg=None):
    if arg is None:
        q.put(function_to_schedule)
    else:
        for _ in range(arg):
            q.put(function_to_schedule)


def worker(q: queue.Queue):
    while True:
        a = q.get()
        a()
        q.task_done()


def main():
    mock_object = MockOperation()
    q = queue.Queue()

    # потоки, которые исполняют воркеров
    for _ in range(5):
        t = Thread(target=worker, args=(q,))
        t.setDaemon(True)
        t.start()

    # потоки, которые добавляют функции, запланированные к исполнению в очередь
    with concurrent.futures.ThreadPoolExecutor() as master:
        for _ in range(5):
            master.submit(scheduler(q, mock_object.function, 100000))

    q.join()

    print("----------------------", mock_object.value())


main()
