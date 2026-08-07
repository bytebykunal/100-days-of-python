# Blog Website - Day 59

A Flask-based blog website built as part of Day 59 of Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

This project builds a more complete blog website using Flask, Jinja templates, Bootstrap, and data fetched from an external API.

## Features

- Flask web application
- Blog homepage displaying multiple posts
- Individual blog post pages
- Dynamic URL routing
- About page
- Contact page
- Jinja templating
- Blog data fetched from an external API
- Responsive web design using Bootstrap

## Technologies

- Python 3.14
- Flask
- Requests
- HTML5
- CSS3
- Bootstrap
- Jinja2

## Project Structure

```text
Day-59-Blog-Capstone/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── post.html
├── static/
│   └── ...
├── requirements.txt
└── README.md
```

## How It Works

1. The application fetches blog post data from an external API using the `requests` library.
2. The homepage displays all available blog posts.
3. Each blog post can be opened through a dynamic URL.
4. The About and Contact pages are available through their own routes.
5. Flask passes the selected blog post to the Jinja template for displaying its content.

## Setup

1. Clone the repository.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python main.py
```

4. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Available Pages

- `/` - Home page
- `/about` - About page
- `/contact` - Contact page
- `/post/<id>` - Individual blog post

## Note

This project was created as part of Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

This is a standalone project completed on Day 59 and is separate from the blog project completed on Day 57.