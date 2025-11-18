from flask import Flask, render_template
from flask_frozen import Freezer
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
freezer = Freezer(app)
if __name__ == '__main__':
    app.run(debug=True)
@freezer.register_generator
def index():
    yield {}
