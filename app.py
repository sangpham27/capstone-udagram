from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    this
    right
    return "<h1 style='text-align: center; font-size: 30px;'>Hello World, my name is SangPT4</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)