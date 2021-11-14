from flask import Flask, render_template, request
from werkzeug.utils import redirect
import pymongo
import db

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    all_skills = db.db.collection.find({})

    if request.method == 'POST':
        if request.form.get('Add') == 'Add':
            db.db.collection.insert_one({"name": request.form['name'], "category": request.form['category'], "date": request.form['date'], "description": request.form['description'], "icon": request.form['icon']})
            return render_template("index.html", skills=all_skills) 
        else:
            return render_template("index.html", skills=all_skills)
    elif request.method == 'GET':
        return render_template("index.html", skills=all_skills)

@app.route("/newform", methods=['GET'])
def newform():
    if request.method == 'GET':
        return render_template("newform.html")

@app.route("/editform", methods=['GET'])
def editform():
    if request.method == 'GET':
        return render_template("editform.html")

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT'])
def skill(path):
    found_skill = db.db.collection.find_one({"name": path})

    if request.method == 'GET':
            return render_template("skill.html", skill=found_skill)
    if request.method == 'POST':
        if request.form.get('Delete') == 'Delete':
            db.db.collection.delete_one({"name": path})
            return redirect("/")



    # elif request.method == 'PUT':
    #     if request.form.get('Edit') == 'Edit':
    #         db.db.collection.update_one({"name": request.form['name'], "category": request.form['category'], "date": request.form['date'], "description": request.form['description'], "icon": request.form['icon'], })
    #         return redirect("/")


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')