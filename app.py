from flask import Flask, render_template, request
import db

app = Flask(__name__)



# @app.route('/')
# def flask_mongodb_atlas():
#     skills = db.db.collection.find()
#     for skill in skills:
#           print(skill)

#     return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            db.db.collection.insert_one({"name": "Izhak"})
            print("Added new skill to database")
            return render_template("index.html")
        elif  request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            print("Decrypted")
            return render_template("index.html")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        return render_template("index.html")


# @app.route("/test")
# def test():
#     db.db.collection.insert_one({"name": "John"})
#     return "Connected to the data base!"



if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')