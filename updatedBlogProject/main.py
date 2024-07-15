from flask import Flask, render_template
import requests

api_url = 'https://api.npoint.io/9424430201af096183d7'

# Fetch data from API with error handling

response = requests.get(api_url)
response.raise_for_status()
posts = response.json()


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", allposts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
