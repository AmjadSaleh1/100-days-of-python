from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
posts = []
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()
for post in all_posts:
    new_post = Post(post['id'], post['title'], post['subtitle'], post['body'])
    posts.append(new_post)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:iid>')
def get_post(iid):
    print(iid)
    return render_template("post.html", posts=posts, id=iid)


if __name__ == "__main__":
    app.run(debug=True)
