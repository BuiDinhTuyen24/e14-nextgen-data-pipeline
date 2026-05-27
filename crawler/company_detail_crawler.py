from supabase import create_client, Client
from dotenv import load_dotenv
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

url = "https://masothue.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

companies = soup.find_all("h3")

links = []

for company in companies:
    a_tag = company.find("a")

    if a_tag:
        company_link = "https://masothue.com" + a_tag["href"]

        links.append(company_link)

print(links[:5])

for company_url in links[:10]:

    response = requests.get(company_url)

    detail_soup = BeautifulSoup(response.text, "html.parser")

    # Company name
    company_name_tag = detail_soup.find("h1")

    company_name = (
        company_name_tag.text.strip()
        if company_name_tag
        else "N/A"
    )

    # Tax code
    tax_td = detail_soup.find("td", itemprop="taxID")

    if tax_td:
        tax_span = tax_td.find("span", class_="copy")
        tax_code = tax_span.text.strip() if tax_span else "N/A"
    else:
        tax_code = "N/A"

    # Address
    address_td = detail_soup.find("td", itemprop="address")

    address = (
        address_td.text.strip()
        if address_td
        else "N/A"
    )

    # Phone
    phone_td = detail_soup.find("td", itemprop="telephone")

    if phone_td:
        phone_span = phone_td.find("span")

        phone = (
            phone_span.text.strip()
            if phone_span
            else phone_td.text.strip()
        )

        phone = phone.replace("Ẩn số điện thoại", "").strip()

    else:
        phone = "N/A"

    print(company_name)
    print(tax_code)
    print(address)
    print(phone)

    company_data = {
        "company_name": company_name,
        "tax_code": tax_code,
        "address": address,
        "phone": phone
    }

    print(company_data)

    response = supabase.table("companies").upsert(company_data).execute()

    print(response)