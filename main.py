import math
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    print("Ok")
    x = 0.0001
    for i in range(1000000):
        x = math.sqrt(x)
    return "Load"    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
