# Internet Speed Y Bot

A Python automation script that measures your internet speed using Speedtest and automatically posts a complaint on the App Brewery **Y** demo platform when your download or upload speed is lower than the speed you pay for.

## Features

- Measures download and upload speed using Speedtest
- Logs into the App Brewery Y demo platform
- Automatically posts a complaint when internet speed is below the promised speed
- Uses Selenium WebDriver for browser automation
- Stores login credentials securely using a `.env` file

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

3. Create a `.env` file using `.env.example` and add your credentials:

```env
Y_EMAIL=your_email@example.com
Y_PASSWORD=your_password
```

4. Update the following values in `main.py` if needed:

```python
PROMISED_DOWN = 1000
PROMISED_UP = 1000
```

Set these to the download and upload speeds provided by your internet service provider.

5. Run the script:

```bash
python main.py
```

## Notes

- This project uses the App Brewery **Y** demo website instead of the real X (Twitter) platform.
- Google Chrome must be installed.
- Selenium Manager automatically downloads the appropriate ChromeDriver for recent Selenium versions.
- Your personal Y login URL is stored in the `.env` file.