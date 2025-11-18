from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# Example route
@app.route('/')
def index():
    # Replace with your logic to get shared volume info
    volume_info = {"shared": 123, "used": 45, "free": 78}
    return render_template("index.html", volume=volume_info)

if __name__ == '__main__':
    app.run(debug=True)
