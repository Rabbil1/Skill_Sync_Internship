import requests

def fetchSaveFile(url, path):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)

    with open(path, "w",encoding="utf-8") as f:
        f.write(r.text)

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

fetchSaveFile(url, "/data/flipkart.html")

print("Done Getting Contents from the Website...")