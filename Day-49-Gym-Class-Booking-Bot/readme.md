# Gym Class Booking Bot

A Python automation script that logs into the App Brewery Gym website, automatically books Tuesday and Thursday 6:00 PM classes, joins the waitlist when classes are full, and verifies all bookings.

## Features

- Automatically logs into the gym website
- Books Tuesday and Thursday 6:00 PM classes
- Joins the waitlist if a class is full
- Detects already booked and waitlisted classes
- Uses explicit waits for reliable automation
- Retries failed operations automatically
- Verifies all bookings on the **My Bookings** page
- Displays a summary of booked, waitlisted, and verified classes

## Technologies

- Python
- Selenium WebDriver
- ChromeDriver
- python-dotenv

## Setup

1. Clone the repository.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file using `.env.example` and add your login credentials:

```env
ACCOUNT_EMAIL=your_email@example.com
ACCOUNT_PASSWORD=your_password
```

4. Run the script:

```bash
python main.py
```

## Notes

- This project is built for the App Brewery Gym demo website.
- Google Chrome must be installed.
- Selenium Manager automatically downloads the appropriate ChromeDriver for recent Selenium versions.