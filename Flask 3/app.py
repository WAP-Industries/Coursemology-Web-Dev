import sys;sys.dont_write_bytecode = 1
from flask import Flask, render_template, request, redirect, url_for
from db_handler import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method=="POST":
        query_db(f"""INSERT INTO posting (username, email, message) VALUES {tuple(i.strip() for i in request.form.values())}""")
        return redirect(url_for("success"))
    
    else:
        return render_template("form.html")

@app.route("/success/")
def success():
    return render_template("success.html", records=query_db("SELECT * FROM posting"))

@app.route("/update/", methods=["POST"])
def update():
    id, message = request.get_json().values()
    return query_db(f'UPDATE posting SET message="{message}" WHERE id={id}')


@app.route("/delete/", methods=["POST"])
def delete():
    return query_db(f"DELETE FROM posting where id={request.get_json()['id']}")

if __name__=="__main__":
    app.run(debug=1)    