# DAY 3 REPORT — DETAIL CRAWLER & DATABASE PIPELINE

## Overview
Ngày 3 tập trung vào việc xây dựng pipeline crawl dữ liệu hoàn chỉnh từ website doanh nghiệp và đẩy dữ liệu trực tiếp lên Supabase cloud database.

---

# Completed Tasks

## 1. Detail Page Crawling
- Crawl danh sách company links từ homepage
- Truy cập vào từng company detail page
- Parse HTML bằng BeautifulSoup

### Technologies Used
- requests
- BeautifulSoup4

---

## 2. Data Extraction
Đã extract thành công các trường dữ liệu:

- Company Name
- Tax Code
- Address
- Phone Number

### Example Extracted Data

```python
{
    "company_name": "CHI NHÁNH 4 CÔNG TY TNHH CƠ KHÍ ĐẠI GIA",
    "tax_code": "0313001097-004",
    "address": "Số 90/45, tổ 1...",
    "phone": "0934872889"
}