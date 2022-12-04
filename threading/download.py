import time
import requests

start = time.perf_counter()
urls = [
    "https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1476&q=80",
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=874&q=80",
    "https://images.unsplash.com/photo-1579710758949-3ab36db30f1b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80",
    "https://images.unsplash.com/photo-1433086966358-54859d0ed716?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80",
]

for index, url in enumerate(urls):
    img_bytes = requests.get(url).content
    img_name = f"image_{index + 1}.jpg"
    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downoalded")

end = time.perf_counter()

print("Downloads end with {:.2f}".format(end - start), "second(s)")
