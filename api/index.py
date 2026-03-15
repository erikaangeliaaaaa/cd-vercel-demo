from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Python on Vercel 🚀</h1>"

def handler(request):
    return app(request.environ, lambda *args: None)