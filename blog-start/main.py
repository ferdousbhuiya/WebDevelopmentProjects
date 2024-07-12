from flask import Flask, render_template
from post import Post

app = Flask(__name__)
url = 'https://api.npoint.io/c790b4d5cab58020d391'

post = Post(url=url)

@app.route('/')
def home():
    data = post.blog_post()
    return render_template("index.html", data=data)

@app.route("/blog/<int:id>")
def get_blog(id):
    data = post.blog_post()
    blog_post = next((item for item in data if item["id"] == id), None)
    return render_template('post.html', post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)
