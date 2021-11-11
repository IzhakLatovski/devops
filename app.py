from flask import Flask, render_template
import db

app = Flask(__name__)



@app.route('/')
def flask_mongodb_atlas():
    skills = db.db.collection.find()
    for skill in skills:
          print(skill)

    return render_template("index.html")

#test to insert data to the data base
@app.route("/test")
def test():
    db.db.collection.insert_one({"name": "John"})

    return "Connected to the data base!"



if __name__ == '__main__':
    app.run(port=8000)