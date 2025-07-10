# PakWheels Car Listings Scraper

This project scrapes car listings from PakWheels and exports the data to an Excel file. It uses Selenium, BeautifulSoup,
and pandas.

## Features

- Scrapes car details (name, price, location, year, mileage, seller, images, etc.)
- Handles multiple pages and filters by city/province
- Exports results to a timestamped Excel file

## Requirements

- Python 3.8+
- Firefox or Chrome browser

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Levelcoder123/pakwheels_scraper.git
    cd pak_wheels_scraper
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Download the appropriate WebDriver for your browser (
   e.g., [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox).

## Usage

1. Run the main script:
    ```
    python scraping_with_beautiful_soup/main.py
    ```

2. Enter the PakWheels search URL when prompted.

3. The script will scrape all car listings and save the data to an Excel file named like
   `pak_wheels_data_YYYY_MM_DD_HH_MM.xlsx`.

## Notes

- Make sure your browser and WebDriver versions match.
- The script runs headless by default.
- For large searches, scraping may take several minutes.
