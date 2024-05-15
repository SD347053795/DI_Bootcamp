import requests
import time

def get_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    if response.status_code == 200:
        return end_time - start_time
    else:
        return None

# Test the function with multiple sites
sites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for site in sites:
    load_time = get_page_load_time(site)
    if load_time is not None:
        print(f"Page load time for {site}: {load_time:.2f} seconds")
    else:
        print(f"Failed to load {site}")
