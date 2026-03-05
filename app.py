from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<html><head><title>Demo App</title></head><body>Demo App Running</body></html>"

if __name__ == "__main__":
    app.run(port=5000)