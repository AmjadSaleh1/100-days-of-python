from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<username>')
def generate(username):
    agify = requests.get(f"https://api.agify.io?name={username}")
    agify_json = agify.json()
    name_of_person = agify_json['name']
    age_of_person = agify_json['age']
    genderiz = requests.get(f"https://api.genderize.io?name={username}")
    genderiz_json = genderiz.json()
    gender_of_person = genderiz_json['gender']
    return render_template("guess.html", name=name_of_person, age=age_of_person, gender=gender_of_person)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
