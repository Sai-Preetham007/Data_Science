from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Home Page."

@app.route("/index")
def index():
    return "Welcome to the Index Page."

if __name__ == "__main__":
    app.run(debug=True)                 # debug = True ---> automatically restart the server and make changes when we save the file.