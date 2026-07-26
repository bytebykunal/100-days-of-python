# TinDog Swiping Bot

A Selenium automation script that logs into the TinDog demo website, handles popups, and automatically swipes through dog profiles.

## Features

- Logs into TinDog using Facebark authentication
- Handles multiple browser windows
- Accepts location, notifications, and cookies popups
- Automatically likes profiles
- Handles match popups
- Uses explicit waits for reliable automation

## Technologies

- Python
- Selenium WebDriver
- ChromeDriver
- python-dotenv

## Setup

1. Clone the repository.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file using `.env.example`:

```env
EMAIL=your_email@example.com
PASSWORD=your_password
```

4. Run:

```bash
python main.py
```

## Notes

- This project is built for the App Brewery TinDog demo website.
- Google Chrome must be installed.
- Selenium Manager automatically downloads the required ChromeDriver.