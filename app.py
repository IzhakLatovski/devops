from flask import Flask, render_template, request
import db

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    all_skills = db.db.collection.find({})

    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # db.db.collection.insert_one({"name": "Bash", "category": "Scripting", "date": "8/21", "description": "Basic scripting on Linux, using Bash", "icon": "https://e7.pngegg.com/pngimages/330/276/png-clipart-bash-shell-script-bourne-shell-scripting-language-unix-shell-shell-rectangle-logo.png"})
            # db.db.collection.insert_one({"name": "Flask", "category": "Development", "date": "9/21", "description": "Python programming language, Flask specificly", "icon": "https://miro.medium.com/max/800/1*Q5EUk28Xc3iCDoMSkrd1_w.png"})
            return render_template("index.html", skills=all_skills)
        elif  request.form.get('Decrypt') == 'Decrypt':
            return render_template("index.html", skills=all_skills)
        elif request.form.get('Delete') == 'Delete':
            db.db.collection.delete_one({"name": "Bash"})
            return render_template("index.html", skills=all_skills)
        else:
            return render_template("index.html", skills=all_skills)
    elif request.method == 'GET':
        return render_template("index.html", skills=all_skills)

@app.route("/newform", methods=['GET', 'POST'])
def newform():
    all_skills = db.db.collection.find({})

    if request.method == 'GET':
        return render_template("newform.html")
    elif request.method == 'POST':
        db.db.collection.insert_one({"name": request.form['name'], "category": request.form['category'], "date": request.form['date'], "description": request.form['description'], "icon": request.form['icon'], })
        return render_template("index.html", skills=all_skills) 

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')