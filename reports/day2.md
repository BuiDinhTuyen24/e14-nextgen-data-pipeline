# Day 2 Report – Crawler Foundation & Async Processing

## Project Name

E14 – NEXT-GEN TECH & MASSIVE DATA PIPELINE

---

# 1. Objectives Completed

During Day 2, the core foundation of the web crawling system was successfully implemented and tested.

Main achievements:

- Tested HTTP requests to target websites
- Parsed HTML content using BeautifulSoup
- Inspected website structure
- Extracted company information
- Built initial async crawler
- Tested concurrent requests
- Connected crawler workflow with database infrastructure

---

# 2. Web Crawling Research

## Understanding HTML Structure

The structure of business listing pages was analyzed using browser developer tools.

Important HTML elements identified:

- `<h3>` tags containing company entries
- `<a>` tags containing:
  - Company names
  - Company detail links

---

# 3. Basic Crawler Implementation

## File

```text
crawler/basic_crawler.py