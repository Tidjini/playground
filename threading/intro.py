import time
from threading import Thread
from random import randrange

start = time.perf_counter()


def do_something(second, *args, **kwargs):
    print(f"Do something in {second} second ...")
    time.sleep(second)
    print("Done ...")


threads = []

for _ in range(1, 10):
    second = randrange(1, 10)
    t = Thread(target=do_something, args=(second,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# t1 = Thread(target=do_something)
# t2 = Thread(target=do_something)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

end = time.perf_counter()
print("Program done in {:.2f}".format(end - start), "second(s)")
