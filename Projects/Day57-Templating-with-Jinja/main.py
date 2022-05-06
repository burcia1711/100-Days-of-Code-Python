from flask import Flask, render_template
import random
from datetime import date
import requests


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, CURRENT_YEAR=current_year, NAME="Burcu")


@app.route('/guess/<name>')
def guess(name):
    responseGender = requests.get(url=f"https://api.genderize.io/?name={name}")
    responseGender.raise_for_status()
    dataGender = responseGender.json()
    gender = dataGender["gender"]

    responseAge = requests.get(url=f"https://api.agify.io/?name={name}")
    responseAge.raise_for_status()
    dataAge = responseAge.json()
    age = dataAge["age"]

    return render_template("guess.html", name=name.title(), gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url="https://api.npoint.io/75f8a2492e59ec0b2837"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True, port=5001)


