import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup

url = "https://masothue.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

companies = soup.find_all("h3")

for company in companies:
    a_tag = company.find("a")

    if a_tag:
        company_name = a_tag.text.strip()
        company_link = "https://masothue.com" + a_tag["href"]

        print("Company:", company_name)
        print("Link:", company_link)
        print("-" * 50)