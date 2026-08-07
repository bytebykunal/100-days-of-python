# Blog Capstone Project - Part 1

A Flask-based blog website built as part of Day 57 of Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

The project fetches blog post data from an external API, converts the data into Python `Post` objects, and displays the posts using Flask and Jinja templates.

## Features

- Flask web application
- Fetches blog posts from an external API
- Displays all blog posts on the homepage
- Individual blog post pages
- Dynamic URL routing
- Jinja templating
- Object-oriented programming using a custom `Post` class
- Bootstrap styling

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
Day-57-Blog-Capstone-Part-1/
│
├── main.py
├── post.py
├── templates/
│   ├── index.html
│   └── post.html
├── static/
├── requirements.txt
└── README.md
```

## How It Works

1. The application sends a request to an external API to retrieve the blog post data.
2. Each blog post is converted into an instance of the `Post` class from `post.py`.
3. The homepage displays all available blog posts.
4. Each post can be opened using its dynamic URL.
5. Flask passes the selected `Post` object to the appropriate Jinja template.

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

## Note

This project was created as part of Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

This is the standalone blog project completed on Day 57 and is separate from the blog project completed later in the course.