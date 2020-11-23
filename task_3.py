from threading import Thread, Lock

a = 0


def function(arg, lock):
    global a
    with lock:
	    for _ in range(arg):
	        a += 1


def main():
    lock = Lock()
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000, lock))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)  # ???


main()
