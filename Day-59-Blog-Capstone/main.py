from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/b7a4be0e01cd8db85f31").json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts= posts)

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def get_post(index):
    for blog in posts:
        if(blog["id"]==index):
            required_blog = blog
            break
            
    return render_template("post.html", post=required_blog)


if __name__ == "__main__":
    app.run(debug=True)