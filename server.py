from flask import Flask # type: ignore
app = Flask(__name__)
@app.route('/')
def hello():
    return "hello world"

app.run(host="0.0.0.0", port=50100, debug=True)