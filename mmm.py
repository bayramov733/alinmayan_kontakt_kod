import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Define URL (iphone listings)
url = "https://kontakt.az/search/?q=iphone"

# Request page
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Prepare Excel
wb = Workbook()
ws = wb.active
ws.title = "iphone Listings"
ws.append(["Title", "Prices"])

# Scrape listings
phones = soup.find_all("div", class_="prodItem")

for telefon in phones:
    title_tag = telefon.find("div", class_="prodItem__title")
    prices_tag = telefon.find("div", class_="prodItem__prices") 
     
     
    title = title_tag.get_text(strip=True) if title_tag else ""
    prices = prices_tag.get_text(strip=True) if prices_tag else ""   
    
    if title and prices:
         ws.append([title,prices])

# Save Excel
wb.save("iphone_listings.xlsx")
print("Done: iphone_listings.xlsx")