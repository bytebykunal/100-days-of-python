# Zillow Data Entry Bot

A Python automation script that scrapes property listings from the App Brewery Zillow Clone website and automatically submits the property information into a Google Form.

## Features

- Scrapes property addresses
- Scrapes rental prices
- Scrapes property links
- Automatically fills and submits a Google Form
- Uses BeautifulSoup for web scraping
- Uses Selenium WebDriver for browser automation

## Technologies

- Python
- BeautifulSoup4
- requests
- Selenium WebDriver
- ChromeDriver

## Setup

1. Clone the repository.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Replace the Google Form URL in `main.py` with your own form if needed.

4. Run the script:

```bash
python main.py
```

## Notes

- This project uses the App Brewery Zillow Clone website.
- Google Chrome must be installed.
- Selenium Manager automatically downloads the appropriate ChromeDriver for recent Selenium versions.