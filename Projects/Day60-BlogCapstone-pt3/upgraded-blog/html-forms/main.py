from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5003)

    # @app.route("/post/<int:index>")
    # def show_post(index):
    #     requested_post = None
    #     for blog_post in posts:
    #         if blog_post["id"] == index:
    #             requested_post = blog_post
    #     return render_template("post.html", post=requested_post)
    #
    #
    # @app.route("/about")
    # def about():
    #     return render_template("about.html")
    #
    #
    # @app.route("/contact")
    # def contact():
    #     return render_template("contact.html")
