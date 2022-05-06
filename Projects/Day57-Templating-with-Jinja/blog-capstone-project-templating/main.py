from flask import Flask, render_template
import requests

app = Flask(__name__)

URL = 'https://api.npoint.io/75f8a2492e59ec0b2837'
response = requests.get(URL)
all_blogs = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_blogs)


@app.route('/post/<int:num>')
def my_posts(num):
    current_blog = None
    print(num)
    for blog in all_blogs:
        if blog['id'] == num:
            current_blog = blog
    return render_template('post.html', post=current_blog)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
