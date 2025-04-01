# Mate Academy Courses Scraper

This project is a web scraper designed to extract course information from the Mate Academy website using Selenium. The data is saved into a CSV file for further analysis.

## Features
- Scrapes course names, descriptions, durations, and module information.
- Supports both Full-Time and Flex course types.
- Outputs data to `mate_academy_courses.csv`.
- Uses Selenium for web automation and PostgreSQL for data analysis.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/AntonAKG/mate-academy-scraper.git
   cd mate_test_task
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Database Queries
This project also includes SQL queries to analyze lead data from a PostgreSQL database:
- Weekly lead count grouped by course type.
- Number of won FLEX leads per country since 2024-01-01.
- List of lost FLEX leads with email and lost reason since 2024-07-01.

## Requirements
- Python 3.8+
- Selenium
- PostgreSQL (for running the SQL queries)
