import datetime
import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    this_year = datetime.datetime.now().year
    return render_template("index.html", year='this_year')


@app.route("/guess/<name>")
def guess(name):
    # Gender API
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data['gender']

    # Age API
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', gender=gender, age=age, name=name)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
