"""
This code scrapes from Eater's restaurant lists and adds it to a Google spreadsheet.
You can then import the sheet into a Google map!
"""

import google.auth
from google.oauth2.service_account import Credentials
import gspread
import requests
from bs4 import BeautifulSoup

# Webscraper code
# Replace the URL with your desired URL
URL = "https://www.eater.com/maps/best-restaurants-kuala-lumpur-malaysia"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

order = ['name', 'description', 'address', 'website', 'phone']
restaurants = [
    {
        'name': (''.join(tag.text for tag in restaurant.find_all('h1'))).replace(u'\xa0', ' '),
        'description': (''.join(tag.text for tag in restaurant.find_all('p'))).replace(u'\xa0', ' '),
        'address': ''.join([(tag.find("a")).text for tag in restaurant.find_all("div", class_="c-mapstack__address")]),
        'website': ''.join([tag['href'] for tag in restaurant.find_all("a", {'href': True}) if tag.text == "Visit Website"]),
        'phone': (''.join([(tag.find("a")).text for tag in restaurant.find_all("div", class_="c-mapstack__phone-url")])).replace('+', '\'+'),
    } for restaurant in soup.find_all("section", class_="c-mapstack__card")
]
values = [[o[e] for e in order] for o in restaurants]

# Accesses and writes to Google sheet
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Use google.oauth2.service_account.Credentials to create credentials
credentials = Credentials.from_service_account_file("eater-scraper-key.json", scopes=scopes)

# Authorize gspread with the new credentials
client = gspread.authorize(credentials)

# Open the Google Sheet and write the data
sheet = client.open("Eater Scraper").sheet1
sheet.append_rows(values, value_input_option='USER_ENTERED')


