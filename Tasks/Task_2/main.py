from bs4 import BeautifulSoup
import pandas as pd

data = {'title' : [], 'price' : []}

with open('/data/flipkart.html', 'r', encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

mobiles = soup.select("div._4rR01T")
prices = soup.select("div._1_WHN1")

print("Len = ", len(mobiles))
print("Len of mobiles price = ", len(prices))

for mobile in mobiles:
    data['title'].append(mobile.string)

for price in prices:
    data['price'].append(price.string)

df = pd.DataFrame.from_dict(data)
df.to_excel("Task_2/output/products.xlsx", index=False)

print("Done Scraping the Data from Flipkart Website...")