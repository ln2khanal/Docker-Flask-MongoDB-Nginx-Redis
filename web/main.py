from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    message = "<p>Hello, World!</p>"
    con = None
    try:
        from pymongo import MongoClient
        con = MongoClient("localhost", 27017)
    except Exception as e:
        message = str(e)
    finally:
        return ("%s - %s (%s)" % (message, con))

def main():
    app.run("0.0.0.0", port=3000, debug=True)

if __name__ == "__main__":
    main()