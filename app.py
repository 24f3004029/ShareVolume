from flask import Flask, render_template, url_for
from flask_frozen import Freezer
app = Flask(__name__)
@app.route('/')
def index():
    # Example: pass some data
    return render_template('index.html')
freezer = Freezer(app)
if __name__ == '__main__':
    app.run()

@freezer.register_generator
def index():
    yield {}
