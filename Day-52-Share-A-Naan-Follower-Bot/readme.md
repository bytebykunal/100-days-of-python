# Share-A-Naan Follower Bot

A Python automation script that logs into the App Brewery Share-A-Naan demo website, opens another user's followers list, and automatically follows their followers.

## Features

- Logs into the Share-A-Naan demo platform
- Opens a target user's followers list
- Automatically scrolls to load more followers
- Follows available accounts
- Handles already-followed accounts gracefully
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
USERNAME=your_username
PASSWORD=your_password
```

4. Update the target account in `main.py` if desired:

```python
SIMILAR_ACCOUNT = "chefsteps"
```

5. Run the script:

```bash
python main.py
```

## Notes

- This project uses the App Brewery Share-A-Naan demo website instead of Instagram.
- Google Chrome must be installed.
- Selenium Manager automatically downloads the appropriate ChromeDriver for recent Selenium versions.