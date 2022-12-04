# work with context, and pool executor, and submiting a function
# this executor.submit return a future object
# you can get the return values by future_object.result()

import time
from concurrent.futures import ThreadPoolExecutor

start = time.perf_counter()


def do_something(name, second):
    print(f"Do something in {second} second(s)...")
    time.sleep(second)
    return f"{name} is Done."


# here introduce the context
with ThreadPoolExecutor(max_workers=1) as executor:
    t = executor.submit(do_something, "name", 1.5)
    print(t.result())

end = time.perf_counter()

print("Program end with {:.2f}".format(end - start), "second(s)")
