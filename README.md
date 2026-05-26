# E14 - NEXT-GEN TECH & MASSIVE DATA PIPELINE

## Project Overview

This project focuses on building a large-scale enterprise data pipeline combined with AI-powered automation systems.

Main objectives:

- Collect and process 100,000+ Vietnamese business records
- Store clean data on cloud infrastructure
- Build business analytics dashboards
- Develop a simple AI Multi-Agent workflow
- Demonstrate AI-assisted development (Vibe Coding)

---

# Features

## Large-Scale Data Collection

- Async web crawling
- Multi-threaded processing
- Retry & logging mechanisms
- User-Agent rotation
- Large-scale scraping pipeline

## Data Engineering

- Data cleaning
- Duplicate removal
- Phone normalization
- Email validation
- Cloud database integration

## Cloud Infrastructure

- Supabase PostgreSQL
- Batch insertion
- Indexed queries
- Scalable architecture

## AI Agent System

- Classification Agent
- Response Agent
- Validation Agent
- CRM/LMS automation demo

## Dashboard & Analytics

- Business density analysis
- District-level statistics
- Business category visualization
- Power BI / Looker dashboards

---

# Tech Stack

## Backend & Crawling

- Python
- AsyncIO
- aiohttp
- BeautifulSoup4
- pandas

## Database

- Supabase PostgreSQL

## AI

- Gemini API / OpenAI API
- CrewAI / LangChain

## Visualization

- Power BI
- Looker Studio

---

# Project Structure

```text
e14-nextgen-data-pipeline/
│
├── crawler/
├── cleaner/
├── database/
├── dashboard/
├── ai_agents/
├── docs/
├── reports/
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
