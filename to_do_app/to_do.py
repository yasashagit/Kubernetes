from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Welcome to the To-Do App!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

print("To-Do App is running on http://localhost:8080")
