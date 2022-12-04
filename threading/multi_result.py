import time
from random import randrange
from concurrent.futures import ThreadPoolExecutor, as_completed

start = time.perf_counter()


def do_something(second):
    print(f"start do something with {second} seconds(s)")
    time.sleep(second)
    return f"{second} is Done"


with ThreadPoolExecutor() as executor:
    secs = [randrange(1, 10) for _ in range(10)]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in as_completed(results):
        print(f.result())

    # we can use the executor.map to return the result directly
    print("With map function")
    results = executor.map(do_something, secs)
    for result in results:
        print(f"{result}")

    # with the 'with' operator the program wait until this threads are done without waiting
    # for join to be called

end = time.perf_counter()

print("Program ends with {:.2f}".format(end - start), "second(s)")
