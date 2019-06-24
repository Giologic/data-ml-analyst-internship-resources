

from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
  return "Test"

@app.route('/test2')
def test2():
  return "Test2"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)