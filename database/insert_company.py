from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

data = {
    "tax_code": "123456789",
    "company_name": "Test Company",
    "city": "Hanoi"
}

response = supabase.table("companies").insert(data).execute()

print(response)