# Amazon Price Tracker

A Python script that tracks the price of an Amazon product and automatically sends an email notification when the price falls below a user-defined threshold.

## Features
- Sends an email only when the price drops below your target price
- Scrapes product title and price using BeautifulSoup
- Uses custom HTTP headers
- Sends email alerts with SMTP
- Stores credentials securely using a `.env` file

## Technologies
- Python
- requests
- BeautifulSoup4
- smtplib
- python-dotenv

## Setup

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Update `PRODUCT_URL` and the HTTP request headers in `main.py` for the Amazon product you want to track.

4. Create a `.env` file using `.env.example` and add your credentials:

```env
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_gmail_app_password
SMTP_ADDRESS=smtp.gmail.com
```

5. Run:

```bash
python main.py
```