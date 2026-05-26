# Day 1 Report – Planning & Infrastructure Setup

## Project Name

E14 – NEXT-GEN TECH & MASSIVE DATA PIPELINE

---

# 1. Objectives Completed

During Day 1, the following foundational tasks were completed:

- Project architecture planning
- Development environment setup
- GitHub repository initialization
- Supabase cloud database setup
- Database schema design
- Python dependency installation
- Initial project documentation
- Technical roadmap preparation

---

# 2. Development Environment

## Python Environment

A dedicated Python virtual environment was created and activated for dependency management.

Installed libraries:

- aiohttp
- beautifulsoup4
- pandas
- sqlalchemy
- asyncpg
- psycopg2-binary
- python-dotenv
- supabase

---

# 3. Cloud Database Setup

## Platform

Supabase PostgreSQL

## Completed Tasks

- Created Supabase project
- Generated API keys
- Connected Python application to cloud database
- Tested successful connection

---

# 4. Database Schema Design

## Main Table: companies

Designed fields:

- tax_code
- company_name
- founded_year
- phone
- email
- address
- district
- city
- business_category
- created_at

Indexes were added for:

- city
- district
- business_category

---

# 5. System Architecture

```text
Data Sources
     ↓
Async Crawler
     ↓
HTML Parser
     ↓
Data Cleaner
     ↓
Deduplicator
     ↓
Supabase Database
     ↓
Dashboard & Analytics