from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/83c70c6226a3f27c158a"
posts = []
app = Flask(__name__)
response = requests.get(URL)
response_text = response.json()


for post in response_text:
    posts.append(post)


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
