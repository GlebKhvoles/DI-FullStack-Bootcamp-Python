import time
import requests
def time_to_load(url):
    before = time.time()
    requests.get(url)
    return time.time()-before
print(time_to_load("https://ynet.com"))
print(time_to_load('https://google.com'))