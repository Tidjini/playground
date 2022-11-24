from concurrent.futures import ThreadPoolExecutor
import time
import asyncio


# if __name__ == "__main__":
start = time.perf_counter()


def do_something():
    while True:
        n = input(f"Enter your name: ")
        print(f"NAME {n}")


async def do_sleep():
    print("DO SLEEP for 10")
    while True:
        await asyncio.sleep(10)
        print("EVENT LISTENER")


with ThreadPoolExecutor(max_workers=2) as executer:
    # stuffs = [("read", 2), ("delete", 1), ("write", 5), ("update", 3)]
    k = executer.submit(asyncio.run, do_sleep())
    f = executer.submit(do_something)
    print(f.result())
    print(k.result())
    # futures = [executer.submit(do_something, name, sec) for name, sec in stuffs]
    # for f in futures:
    #     print(f.result())

end = time.perf_counter()

print(f"End with, {end - start} sec")
